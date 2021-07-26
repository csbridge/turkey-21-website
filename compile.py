#!/usr/bin/env python

'''
FILE: compile.py
----------------
Template compiler that compiles all .html and .mdown template files in the 
TEMPLATE_DIR directory below (excluding .ptl files, which are partial templates), 
and outputs with the same filenames to the OUTPUT_DIR directory, but ending in
.html.

Example usage:

> python3 compile.py --output_dir docs

Compiles all template files using local paths, and outputs the compiled files to
the docs directory.  The compiled files in docs/ have the same directory structure
as in the TEMPLATE_DIR directory.

> python3 compile.py

Compiles all template files and outputs the compiled files to
the OUTPUT_DIR below.
----------------
'''

from util.bottle.bottle import SimpleTemplate
import configparser
import json
import os
import sys
import markdown


TEMPLATE_DIR = 'templates'
CONFIG_FILE = 'config/config.ini'

# Use the --output_dir flag to optionally specify where compiled files go
if '--output_dir' in sys.argv:
    OUTPUT_DIR = sys.argv[sys.argv.index('--output_dir') + 1]
else:
    OUTPUT_DIR = 'docs'

# Verbose mode
VERBOSE = '--verbose' in sys.argv

'''
FUNCTION: compile
-----------------
Parameters: NA
Returns: NA

This function compiles all the html files (recursively)
from the templates dir into the output folder. Folder
hierarchy is preserved.
-----------------
''' 
def compile():
    # Read the course config
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    # Compile all templates
    templateFilePaths = getTemplateFilePaths('')
    print("\nCompiling:\n----------")
    for templateFilePath in templateFilePaths:
        if VERBOSE:
            print("Compiling " + templateFilePath + "...")
        outputPath = getCompiledOutputPath(templateFilePath)

        # Recompile only if the template has changed
        templateLastModified = os.path.getmtime(os.path.join(TEMPLATE_DIR, templateFilePath))
        compiledLastModified = os.path.getmtime(outputPath) if os.path.exists(outputPath) else None
        if True: #templateLastModified > compiledLastModified: TODO: what if a file's dependency was changed?
            compileTemplate(templateFilePath, outputPath, config)
            if VERBOSE:
                print(templateFilePath + " -> " + outputPath)
        elif VERBOSE:
            print("Unmodified - skipping...")

    print("\nDONE.\n")

'''
FUNCTION: getCompiledOutputPath
-------------------------------
Parameters:
    relativePath - the path within TEMPLATE_DIR of the template file to find
                    the output path for

Returns: the path of where the saved, compiled template file would be put in
the OUTPUT_DIR directory.  Folder hierarchy is preserved.
'''
def getCompiledOutputPath(relativePath):
    suffix = relativePath.split('.')[-1]
    relativePath = relativePath[:len(relativePath) - len(suffix)] + "html"
    absolutePath = os.path.join(OUTPUT_DIR, relativePath)
    return absolutePath

'''
FUNCTION: getTemplateFilePaths
------------------------------
Parameters:
    templateRoot - the folder within TEMPLATE_DIR to get file paths for

Returns: a list of .html and .mdown template file paths from within the given 
directory within TEMPLATE_DIR.  Ignores .ptl files, which are partial templates.
------------------------------
'''
def getTemplateFilePaths(templateRoot):
    paths = []
    templateDirPath = os.path.join(TEMPLATE_DIR, templateRoot)
    for fileName in os.listdir(templateDirPath):
        filePath = os.path.join(templateRoot, fileName)
        templateFilePath = os.path.join(TEMPLATE_DIR, filePath)

        # Recurse if it's a directory, add if it's a template file
        if os.path.isdir(templateFilePath):
            childPaths = getTemplateFilePaths(filePath)
            for childPath in childPaths:
                paths.append(childPath)
        elif isTemplateFile(fileName):
            paths.append(filePath)

    return paths

'''
FUNCTION: isTemplateFile
------------------------
Parameters:
    fileName - the fileName to check is a template file

Returns: whether or not the given filename is a template file (ends with .html
or .mdown)
------------------------
'''
def isTemplateFile(fileName):
    extension = os.path.splitext(fileName)[1]
    return extension == '.html' or extension == '.mdown' or extension == '.md'

'''
FUNCTION: compileTemplate
-------------------------
Parameters:
    relativePath - the path within TEMPLATE_DIR of the template file to compile
    outputPath - the absolute path where the compiled template file should be saved.
    config - the site configuration info to pass into the template to compile it.
                Expected to be a ConfigParser with DEFAULT section.

Returns: N/A

Compiles the given template file and saves it to outputPath.
Can compile both HTML and Markdown template files.  If a Markdown file is
provided, it is converted to HTML and then rendered within
the template specified in the markdown's rebase field, if any, or otherwise
just rendered on its own.
-------------------------
'''
def compileTemplate(relativePath, outputPath, config):
    pathToRoot = getPathToRootFrom(relativePath)
    filePath = os.path.join(TEMPLATE_DIR, relativePath)
    fileContents = open(filePath, encoding='utf8').read()

    compiledHtml = ''

    if relativePath.endswith('html'):
        # HTML

        # Just render the HTML template
        compiledHtml = SimpleTemplate(fileContents).render(pathToRoot=pathToRoot, 
            config=config['DEFAULT'])
        compiledHtml = compiledHtml.encode('utf8')
    elif relativePath.endswith('mdown') or relativePath.endswith('md'):
        # Markdown

        # Convert Markdown -> HTML
        md = markdown.Markdown(extensions=['fenced_code', 'meta', 'attr_list', 'toc'])
        html = md.convert(fileContents)
        compiledHtml = html
        if html:
            compiledHtml = SimpleTemplate(html).render(pathToRoot=pathToRoot,
                config=config['DEFAULT'])

        # If the markdown file specifies a template to be rendered within,
        # use that.  Otherwise just use the compiled markdown file itself
        if 'template' in md.Meta:
            templateText = open(md.Meta['template'][0], encoding='utf8').read()
            attributes = {key:"\n".join(md.Meta[key]) for key in md.Meta}
            compiledHtml = SimpleTemplate(templateText).render(pathToRoot=pathToRoot,
            base=compiledHtml, filePath=filePath, config=config['DEFAULT'], **attributes)

        # Encode the HTML and make its rendered path .html instead of .mdown
        compiledHtml = compiledHtml.encode('utf8')
        if VERBOSE:
            print(outputPath)

    # Save HTML to file
    makePath(outputPath)
    open(outputPath, 'wb').write(compiledHtml)

'''
FUNCTION: getPathToRootFrom
---------------------------
Parameters:
    relativePath - the path to start at when calculating the path to the root

Returns: the relative path to the root directory from the given relativePath.
    Concatenates "../" for each level down from the root.
------------------------------
'''
def getPathToRootFrom(relativePath):
    depth = depthFromRoot(relativePath)
    pathToRoot = ''.join(['../' for i in range(depth)])
    return pathToRoot

'''
FUNCTION: depthFromRoot
-----------------------
Parameters:
    filePath - the path for which to calculate the depth

Returns: the number of levels filePath is from the root level.
    E.g. 'index.html' -> 0
         'stuff/index.html' -> 1
         'stuff/moreStuff/index.html' -> 2
-----------------------
'''
def depthFromRoot(filePath):
    rootPath = os.path.dirname(filePath)
    if len(rootPath) == 0: return 0
    return depthFromRoot(rootPath) + 1
    
'''
FUNCTION: makePath
------------------
Parameters:
    path - the path to make directories for

Returns: NA

Creates all needed directories in this path for the directory path to exist.
E.g. if path = 'stuff/moreStuff/index.html' then the stuff and moreStuff
directories would be created if they did not already exist.
------------------
'''
def makePath(path):
    dirPath = os.path.dirname(path)
    if dirPath != '' and not os.path.exists(dirPath):
        os.makedirs(dirPath)


if __name__ == '__main__':
    compile()
