# GYST-task-coach-flask-api
# GYST - React/Flask App 

# User Stories: 

User is greeted by splash page with login window / register link
User enters username (email) & password with input fields
User submits form and database entry for user login time is created
Database is queried with user email & compares hashed password
Returns GYST show page. Shows index with input / tasks listed /clock component
User can enter task in ‘tasks’ input component with submit task (create Task - POST) 
When several tasks are created - user can press start button to initialize clock component
Each Task will run will run for 25 minute with a 5 minute break.
After each task is completed is rotated to the bottom of the list 
After clicking on a task a modal will populate offering the user options to change priority, delete task, or update notes/name of task, save tasks. 
After logging out the uncompleted tasks (that are not saved) are deleted from DB
Session logout time is updated for user 

# MODELS

## USER
+ Name (varChar)
+ Email (Username) (varChar)
+ PW (varChar) 
+ Login Time (Date) 
+ LogOut Time (Date)
+ UserID   (Integer)

## TASK
+ Name (varChar)
+ Priority  (varChar)
+ Saved (Boolean)
+ Body (varChar)
+ Completed (Boolean)
+ Date Created / Timestamp (Date) 
+ User ID (Integer)







