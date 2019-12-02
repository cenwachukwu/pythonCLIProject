# theNotes!

## Description:
The purpose of this project was to use python to build a note taking command line application with uses a SQL database with peewee models.
In this application, the users are able to create notes with title, contents and dates. They are also able to view a list of their notes or select and view a specific note.
The users are also able to update and delete previous notes. Future plans for this project would include buiding out its own user interface and incorporating web scraping.


## Technologies: 
* Peewee 
* SQL and Postgres
* Python
* pyscopg2
* VS code

## Required Installations:
* Fork and clone (or just clone) the repository
  * git clone https://github.com/cenwachukwu/pythonCLIProject.git
  * cd into the directory ie. cd pythonCLIProject
* Inside the directory install the dependencies:
  * pipenv install peewee
  * pipenv install psycopg2-binary
* brew install python3 -if you do not have python installed
* Run python3 notes.py
* To open the code in vs code, run code .
* To run theNotes: pipenv run python notes.py


## Instructions:
Here's an explanation on how to navigate through the application:
* To begin run: pipenv run python notes.py

* Create a username:
  * Once in the application, you will be propmted to enter a username. Enter a username unique and memorable to you.

* Create notes:
  * Because you have no notes at this point, you will be directed to created a note. After your first note, you will be asked if you want to create another note or view your previous note.
  * if you choose to create another note, you will go through the same cycle. However if you choose to view your previous notes, you will be directed to view your previous creations. 
    
* View note:
  * When you are directed to view notes, you can either view all your notes or select by title what note you would like to see.
  * Viewing all notes is pretty self explanatory, all the notes you've created will be shown to you. 
  * When you view notes by title, you will be shown the note with the matching title you searched for
  * You would be redirected to either "view note or create new note?"
  * You will only be shown notes that match your user name for the sake of other users privacy

* Editing notes:
  * When you view all notes, you wont be directly redirected to edit your notes, rather you will be asked once more if you would like to "Type in note title or say view all". This time type in the note title you would like to edit.
  * When you view notes by title, you would be asked if you would like to edit your notes after viewing:
    * inputing Y would lead you to an Update or Delete question:
      * to delete, simply type delete and the post will be deleted
      * to update, type in update and you will be directed to a set of instructions asking you whether you would like to update the title or the content. Make sure to copy your previous to notes and add them to the update.
    * inputing N would direct you to the "Would you like to view another note? Y/N:" question. Answering N for no would lead to the view or create question.
 
* Leaving the app:
   * To leave the app at any point just type in: \q to quit

