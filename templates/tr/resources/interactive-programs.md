template: templates/en/template.ptl
title: Interactive Programs Reference

# Interactive Programs Reference
---

<div class="row">
	<div class="col-xs-12">
		<a class="btn btn-primary" role="button" data-toggle="collapse" href="#quickreference" aria-expanded="false" aria-controls="collapseExample">
		  	Show/Hide Quick Reference
		</a>
		<a class="btn btn-primary" role="button" href="api-docs/graphics.html">
		  	View Complete Reference Docs
		</a>
	</div>
</div>

<br />
<div class="collapse" id="quickreference">
	<h4>Get Recent Events</h4>
	<table class="table table-bordered table-striped">
		<thead>
			<tr>
				<td>Method</td>
				<td>Description</td>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td><code>get_new_mouse_presses</code></td>
				<td>Returns a list of mouse presses that have occurred since the last time this function was called.  Each element in the list has an "x" and "y" property for its x and y coordinates.  This function should be called inside a loop to continually check for mouse presses.</td>
			</tr>
			<tr>
				<td><code>get_new_mouse_drag_events</code></td>
				<td>Returns a list of mouse drag events (when the mouse is moved while being held down) that have occurred since the last time this function was called.  Each element in the list has an "x" and "y" property for its x and y coordinates.  This function should be called inside a loop to continually check for mouse drag events.</td>
			</tr>
			<tr>
				<td><code>get_new_key_presses</code></td>
				<td>Returns a list of key presses that have occurred since the last time this function was called.  Each element in the list is a string description of the key that was pressed (e.g. "a", "space", "B").  This function should be called inside a loop to continually check for key presses.</td>
			</tr>
			<tr>
				<td><code>get_new_button_clicks</code></td>
				<td>Returns a list of button clicks that have occurred since the last time this function was called.  Each element in the list is a string which is the text for the button that was clicked.  This function should be called inside a loop to continually check for button clicks.</td>
			</tr>
		</tbody>
	</table>
	<h4>Create/Delete Interactors</h4>
	<table class="table table-bordered table-striped">
		<thead>
			<tr>
				<td>Method</td>
				<td>Description</td>
			</tr>
		</thead>
		<tbody>
			<tr>
				<td><code>create_button(text, location)</code></td>
				<td>Creates a new button displaying the specified text, on the given side of the canvas (TOP, BOTTOM, LEFT, RIGHT).</td>
			</tr>
			<tr>
				<td><code>create_text_field(description, location)</code></td>
				<td>Creates a new text field and label next to it displaying the given description, on the given side of the canvas (TOP, BOTTOM, LEFT, RIGHT).</td>
			</tr>
			<tr>
				<td><code>button.destroy()</code></td>
				<td>Delete a button from the canvas.  This should be called on the value you get from the <code>create_button</code>, e.g. <code>button = create_button(...) ... button.destroy()</code></td>
			</tr>
			<tr>
				<td><code>delete_text_field(description)</code></td>
				<td>Delete a text field from the canvas.  This should be called with the same description text you specified when you created the text field.</td>
			</tr>
		</tbody>
	</table>  	
	<hr />
</div>

One of the most common libraries to create interactive graphics in Python is called Tk (short for "tkinter"). Tk is a powerful graphics library that should be automatically installed for Windows and Mac along with Python when you installed it.  But some of the functions are hard to use.  For this reason, we provide our own small graphics library that is built on top of Tk and makes it easier to use.  However, it's not a replacement for Tk - it just adds new functions to make certain things like drawing text easier.  You can always explore the full Tk library if you're interested in seeing what else you can do!

## The Mouse
You can get the location of the mouse at any time using `get_mouse_x()` and `get_mouse_y()` on the canvas:

```
rect = canvas.create_rectangle(0, 0, 100, 100)
...
canvas.moveto(rect, canvas.get_mouse_x(), canvas.get_mouse_y())
```

Most times, we will get the mouse location inside a loop so that we can update something many times as the mouse moves (such as the position of a shape).

To check for mouse clicks, use `get_new_mouse_clicks` in a loop:

```
while ...:
	clicks = canvas.get_new_mouse_clicks()
	for click in clicks:
		canvas.create_rectangle(click.x, click.y, click.x + 10, click.y + 10)
```

Each element of the list given to you by the canvas has an `x` and `y` coordinate that you can use to know where that click occurred.

To check for mouse drag events (when the user moves the mouse while it is being held down), use `get_new_mouse_drag_events` in a loop:

```
while ...:
	mouse_drag_events = canvas.get_new_mouse_drag_events()
	for event in mouse_drag_events:
		canvas.create_rectangle(event.x, event.y, event.x + 10, event.y + 10)
```

Each element of the list given to you by the canvas has an `x` and `y` coordinate that you can use to know where that mouse drag event occurred.

Finally, you can wait for the user to click using `wait_for_click`:

```
canvas.wait_for_click() # This line will wait for the user to click
print("You clicked!") # This code will not run until the user clicks
```

Unlike the previous examples, `wait_for_click` doesn't need to be called in a loop - the function itself will not finish until the user clicks.

## The Keyboard
To check for keyboard key presses, use `get_new_key_presses` in a loop:

```
while ...:
	presses = canvas.get_new_key_presses()
	for press in presses:
		if press == "Up":
			character.move(0, -5)
```

Each element of the list given to you by the canvas is the text name of the key that was pressed.  E.g. "a" will be for the lowercase "a" key, "A" will be if Shift+a is pressed, etc.  If you are unsure what the key name is, try writing a program that prints out the key name, like this:

```
while True:
	presses = canvas.get_new_key_presses()
	for press in presses:
		print(press)
```

## Interactors (Buttons / Text Fields)
You can add interactors (buttons and text fields) around the edges of the canvas to allow users to interact with them.  These aren't put on the canvas, these are put around the edges of the canvas, so you don't specify coordinates like you usually do for graphical objects, you specify which area (top, bottom, left, right) you want the interactor.

### Buttons
Create a button using the `create_button` function:

```
my_button = canvas.create_button("Click me", Canvas.TOP)
```

To delete the button you have created, use `destroy()` on the button variable:

```
my_button.destroy()
```

To check for button clicks, use `get_new_button_clicks` in a loop:

```
while ...:
	clicks = canvas.get_new_button_clicks()
	for click in clicks:
		if click == "Click me":
			...
```

Each element of the list given to you by the canvas is the text name of the button that was clicked.

### Text Fields
Create a text field using the `create_text field` function:

```
canvas.create_text_field("Enter name", Canvas.TOP)
```

To delete the text field you have created, use `delete_text_field()` and specify the description you used when you created it:

```
canvas.delete_text_field("Enter name")
```

To get the text currently entered into the text field, use `canvas.get_text_field_text` and specify the description you used when you created it:

```
entered_text = canvas.get_text_field_text("Enter name")
```

You will usually use this in combination with a button to know when the user is ready to do something - e.g. have them enter their name and click "Ok" to begin:

```
while ...:
	clicks = canvas.get_new_button_clicks()
	for click in clicks:
		if click == "Click me":
			entered_text = canvas.get_text_field_text("Enter name")
```