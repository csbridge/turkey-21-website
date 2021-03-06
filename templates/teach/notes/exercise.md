template: templates/teach/notes/template.ptl
problemtitle: Office Hours Exercise
nosolution: True

## Exercise 1: Mountain Karel Getting Started
Each of you should choose a role.  Then, click the button (and only that button!) corresponding to your role below.

<div class="panel-group" id="accordion1">
  <div class="panel panel-primary">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion1" href="#collapse3">I am the SL</a>
      </h4>
    </div>
    <div id="collapse3" class="panel-collapse collapse">
      <div class="panel-body">
    You're an SL helping a student get started on <a href="{{pathToRoot}}en/projects/mountain.html">Mountain Karel</a>.  Starter code is <a href="{{pathToRoot}}starter/Day2AM.zip">here</a>.
    <br />
    <br />
    It looks like they are working on getting Karel to ascend the mountain, but are having trouble repeating steps.  They can share their screen with you if you want to take a look at code they are talking about.  Remember that loops and conditions are tricky at this point - the <a href="{{pathToRoot}}teach/notes/mountain.html">TA Notes</a> for this problem may help you!  The student will also fill you in on where they're at.
      </div>
    </div>
  </div>
  <div class="panel panel-primary">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion1" href="#collapse4">I am the Student</a>
      </h4>
    </div>
    <div id="collapse4" class="panel-collapse collapse">
      <div class="panel-body">
    You're a student signing up for Office Hours for help with approaching <a href="{{pathToRoot}}en/projects/mountain.html">Mountain Karel</a>.  Download <a href="{{pathToRoot}}starter/office_hours_staff_training.zip">this PyCharm project</a> and open it in PyCharm - the file <code>mountain_karel_1.py</code> is "your code". From there you can play around with it first if you want to.
    <br />
    <br />
    You are currently working on getting Karel to ascend the mountain, but are struggling - you can get Karel to ascend one step of the mountain, but you aren't sure how to use conditions (which you just learned about) to make Karel repeat the task.  Tell this to the SL when you start to describe where you are, and what you are stuck with.  You can share your screen to show the SL your code.
    <br />
    <br />
    Note: the ultimate issue is you should first figure out <i>what you want to repeat</i>, and then <i>how long you want to repeat it for</i>.  You want to repeat the code to go up a single step, and you want to continue doing this until you reach the top of the mountain.  One possible solution is to use a <code>while</code> loop with the condition being <code>right_is_blocked()</code>.  Then inside the loop you include the instructions to go up one step.
      </div>
    </div>
  </div>
</div>

## Exercise 2: Mountain Karel Debugging
Now, switch roles!  Then, click the button (and only that button!) corresponding to your new role below.

<div class="panel-group" id="accordion2">
  <div class="panel panel-primary">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion2" href="#collapse1">I am the SL</a>
      </h4>
    </div>
    <div id="collapse1" class="panel-collapse collapse">
      <div class="panel-body">
    You're an SL helping a student with a bug they have while working on <a href="{{pathToRoot}}en/projects/mountain.html">Mountain Karel</a>.  Starter code is <a href="{{pathToRoot}}starter/Day2AM.zip">here</a>.
    <br />
    <br />
    It looks like they are working on getting Karel to ascend the mountain.  They can share their screen with you if you want to take a look at code they are talking about.  Remember that loops and conditions are tricky at this point - the <a href="{{pathToRoot}}teach/notes/mountain.html">TA Notes</a> for this problem may help you!  The student will also fill you in on where they're at.
      </div>
    </div>
  </div>
  <div class="panel panel-primary">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion2" href="#collapse2">I am the Student</a>
      </h4>
    </div>
    <div id="collapse2" class="panel-collapse collapse">
      <div class="panel-body">
    You're a student signing up for Office Hours for help with a bug you have while working on <a href="{{pathToRoot}}en/projects/mountain.html">Mountain Karel</a>.  Download <a href="{{pathToRoot}}starter/office_hours_staff_training.zip">this PyCharm project</a> and open it in PyCharm - the file <code>mountain_karel_2.py</code> is "your code". From there you can play around with it first if you want to.
    <br />
    <br />
    You are currently working on getting Karel to ascend the mountain, but are struggling - it looks like Karel climbs in a reasonable manner, but doesn't stop at the top, and keeps going to the top edge of the screen!  In other words, you have roughly figured out what you want to repeat, but are stuck figuring out the condition.  Tell this to the SL when you start to describe where you are, and what you are stuck with.  You can share your screen to show the SL your code.  You're having a hard time knowing what condition to use to get Karel to climb and then stop!
    <br />
    <br />
    Note: the ultimate issue is the condition for the while loop, which is still true even when you reach the top of the mountain.  One possible solution is to use <code>right_is_blocked()</code> instead.  Another is to not have Karel turn left, and instead immediately check for <code>front_is_blocked()</code>, and use that as a condition to stop.
      </div>
    </div>
  </div>
</div>

<!-- Currently unused
## Exercise 2: Khansole Academy Debugging
Now, switch roles!  Then, click the button (and only that button!) corresponding to your new role below.

<div class="panel-group" id="accordion2">
  <div class="panel panel-primary">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion2" href="#collapse1">I am the SL</a>
      </h4>
    </div>
    <div id="collapse1" class="panel-collapse collapse">
      <div class="panel-body">
    You're an SL helping a student with a partially-complete implementation of <a href="{{pathToRoot}}en/projects/khansole.html">Khansole Academy</a>.  Starter code is <a href="{{pathToRoot}}starter/Day3PM.zip">here</a>.
    <br />
    <br />
    It looks like they are working on keeping track of the number of correct answers in a row, but they can't figure out how to do this.   They can share their screen with you if you want to take a look at code they are talking about.  Remember that variables and control flow in Python are tricky at this point - the <a href="{{pathToRoot}}teach/notes/khansole.html">TA Notes</a> for this problem may help you!  The student will also fill you in on where they're at.
      </div>
    </div>
  </div>
  <div class="panel panel-primary">
    <div class="panel-heading">
      <h4 class="panel-title">
        <a data-toggle="collapse" data-parent="#accordion2" href="#collapse2">I am the Student</a>
      </h4>
    </div>
    <div id="collapse2" class="panel-collapse collapse">
      <div class="panel-body">
    You're a student signing up for Office Hours for help with getting unstuck while working on <a href="{{pathToRoot}}en/projects/khansole.html">Khansole Academy</a>.  Download <a href="{{pathToRoot}}starter/khansole_submission.zip">this PyCharm project</a> and open it in PyCharm - this is "your code". From there you can play around with it first if you want to.
    <br />
    <br />
    You are currently working on keeping track of the number of correct answers in a row, and stopping once you hit 3, but are struggling - you can prompt the user with addition problems and tell them if they are right or wrong, but can't keep track of overall streaks.  In other words, you have roughly figured out what you want to do, but are stuck figuring out the condition and how to track the correct guesses in a row.  Tell this to the SL when you start to describe where you are, and what you are stuck with.  You can share your screen to show the SL your code.  You're having a hard time knowing how to use variables, and how to use a while loop to stop once you hit 3 correct answers in a row!
    <br />
    <br />
    Note: the ultimate solution is to add a variable outside the loop to keep track of the number of correct answers, and check whether or not this is 3 in the while loop.  Inside the loop, you need to increment the number of correct answers when the user answers a question correctly, and reset it to 0 if they answer incorrectly.
      </div>
    </div>
  </div>
</div>
-->