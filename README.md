# Application (login_manager)
Basic login management program. The idea of the program will be to implement a basic login service through the console to a python "backend" and database.

This is not the best or greatest, but a fair and honest attempt at a easy program in python with a visual GUI/interface.

## Goal (The learning man!)
*the goal of this excessive was to get a project down and improve use of python in an actual application*
1. Python 3 use.
2. Virtual Environment.
3. Classes, functions, methods, etc.
4. Helper functions and scripts.
5. Best Practice project structure. (License, .gitignore, Makefile, Setup.py, __init__.py, requirements.txt)
6. Database interaction. (sqlite3)
7. Safe database use.
8. Dictionaries, Lists, tuples, string editing (join)
9. Commenting, function description.
10. Unit testing.
11. GUI (Tkinter) use. (pack, grid, etc)
12. Proper importing.
13. Git interaction. (see all commits)
14. Refactoring possibilities. (cleaner code)

## Additionals
1. Password hashing.
2. Keep count of the number of login attempts (Successes/Failures).
3. Should not be able to create a duplicate username.
4. Must have a password, passwords must match
5. do a popup message to indicate what data we still need to have entered.
6. Password should be longer than 8 chars, include numeric values, and other characters.
7. Do another call to the db if login successful and welcome the user with their name ans surname.

## Setup
A Virtual Environment needs to be set up for the package to be tested in.
A blank Venv will suffice.
simply run the following: 
1. make init
2. make test

## Tests
*Tests are all located in the tests folder*

## Basic Project Description and overview

### Project improvements
Some basics
Login, Username: Password.
Create User,
User already exists
password check
encrypt password somehow.
username/password check.
email addon
email the user.
after completed in console do a GUI with python. Something dumb but at least it is something to the effect of actaual working code in the name.
Do a forget password, and offer to email the password to the registered email

#### Fields (Login)
1. Username
2. Password

#### Fields (Create new user)
1. First Name
2. Last Name
3. Username
4. Email
5. Phone Number
6. Password, verify password.
