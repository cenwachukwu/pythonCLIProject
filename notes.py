#first after creating your directory and your file is to run {pipenv install peewee then pipenv install psycopg2-binary} to install peewee in your file
#importing peewee
from peewee import *
from datetime import date 

#Using the PostgresqlDatabase class to create a database connection, 
#passing in the name of the database (in the case = notetaker), the user (postgres), the password (blank), the host (localhost), and the port.
db = PostgresqlDatabase('notetaker2', user='postgres', password='',
                        host='localhost', port=5432)

#Use db.connect() to actually connect to the database
db.connect()

#PeeWee gives us a base Model class that we can inherit from. 
#Our model needs to define the fields for that SQL table as well as the database the table should be in 
#(because there can be more than one).

class BaseModel(Model):     #this class defines a BaseModel class that sets the database connection
    class Meta:             
        database = db       #A Meta class is a class that describes and configures another class, 
                            #so basically to explain where exactly where our Note model 
                            #should be pulling its information from

#Now that we have our BaseModel, we can define our model and have it inherit from this BaseModel class:
# Define what a 'Note' (our model) is
class NoteTaker(BaseModel):   
#These are all the fields NoteTaker has, but You need to explain to peewee what the datatype in each column in the table is:
    user = CharField()
    title = CharField()
    date = DateField()
    notes = CharField()
        # both CharField() and DateField() are from PeeWee's datatypes. others are BooleanField(), IntegerField() etc.
        # CharField() basically means that both the title and note fields are strings and 
        # the DateField() means that the date field will take a date

class User(BaseModel): #the requirement asked for users to be able to view all their notes or a particular note
    name = CharField() #in the functions below we would use their name as a filter in our select()

#db.create_tables([NoteTaker]) to add this table to the database
db.create_tables([NoteTaker, User])

# creating interactive input logic for creating the data: 
#initially, i didnt have this as a function but it makes more sense to have it as a function.
#so we can have functions that serve as menu to view or create, creates new notes, and views notes or view particular notes
#we also had to add the user, so we have to have a function that creates a user with the user table and adds it to the notetaker's user column


def find_user():
    name = str(input("Enter your username: ")).title()  #adding a title() or upper() to variables you want to query is extremly important b/c lack of it can lead to dumb bugs
    print(f'Hello {name}')
    returning = User.select().where(User.name == name)
    if not returning : 
        new_user = User(name=name)
        new_user.save()
    elif returning :
        your_notes = NoteTaker.select().where(NoteTaker.user == name).count()#i want to count the number of books each user has
        if your_notes >= 1:
            print(f'Youve got {your_notes} notes.') #and tell them oh you've xyz amout of notes
        else :
            print("Youve got 0 notes!")   
    return name #return name

#we pass the user's username to the rest of the function to be able to access it to create a user with that user name
def view_or_create(name): 
    note = input("view note or create new note?: ")
    if note == 'view note':
        your_notes = NoteTaker.select().where(NoteTaker.user == name).count()
        if your_notes >= 1:
            view_note(name)
        else:
            print("Youve got 0 notes!")
            create_note(name)
    elif note == 'create new note':
        create_note(name)

def view_note(name): 
    searchEngine = str(input("Type in note title or say view all: ")).title()    #ask for input to enable us to select() search in the next step
    if searchEngine == 'View all':
        all_user_notes = NoteTaker.select().where(NoteTaker.user == name) #how we get all the notes belonging to the user using select
        print(f'{NoteTaker.user}s notes: ')
        for notes in all_user_notes: #we use a for loop to loop/map through the notes belonging to the user and print it
            print(f'{notes.date}\n{notes.title}\n{notes.notes}') #\n makes the entry go down to the next line
        view_or_create(name)
    else :
        result = NoteTaker.get(NoteTaker.title == searchEngine, NoteTaker.user == name)     
                    #{Get} search finds a single data while {select} finds multiple
                    #above we search by note title and by the user name for a strict single result search.
                    #our first step to achieving crud.
        print(result.date)
        print(result.title)
        print(result.notes)
        
        #working on update and delete:
        user_edit = str(input("Would you like to edit the post? y/n: ")).title()
            if user_edit == 'Y':
                user_edit2 = str(input("Would you like to Update or Delete this note? update / delete: ")).title()
                if user_edit2 == 'Delete':
                    result.delete_instance()
                    print(f'{result} has been deleted')
                elif user_edit2 == 'Update':
                    user_update = str(input("What would you like to update? title / notes / date")).title()
                    if user_update == 'Title':
                        update = str(input('Update your title: ')).title()
                        result.title = update
                        result.save
                    elif user_update == 'Date':
                        update = int(input(enter date like so (1990, 11, 18)): )
                        result.date = update
                        result.save
                    elif user_update == 'Notes':
                        update = input('Add some content to your note: ')
                        result.notes = update
                        result.save

        view_another = input('Would you like to view another note? Y/N: ')
        if view_another == "y":
            view_note(name)
        else :
           theNotes()

        

def create_note(name):
    #first step to creating a new note is to collect inputs 
    # date input below is always year, date, month in that order, also because the date a num/integer, we wrap the input in int eg.
    # int(input())
    print(f'{name}')
    year = int(input('Enter the year like so (2012) '))
    month = int(input('Enter the month number like so (for March type 3): '))
    day = int(input('Enter the day number like so (21): '))
    # we can also ask for date input like so: date = int(input(enter date like so (1990, 11, 18))) and to get date of present time(date = datetime.datetime.now())
    title = str(input('Add a title for your new note: ')).title()
    notes = input('Add some content to your note: ')

    # next step to bind all the entries together to make a new note in the NoteTaker db, we also call the name agruement as the name of the user
    new_note = NoteTaker(
        title=title, 
        notes=notes, 
        date=date(year, month, day), 
        user=name)

    #next we save the new note like so:
    new_note.save() 

    #next we display our new note:
    print("") #for space asthetics lol
    print(new_note.date)
    print(new_note.title)
    # print(f"{new_note.title}") 
    print(f"{new_note.notes}")
    print("") #for space asthetics

    #next we create a cycle, so we ask the user if they want to create a another note or view a note
    create_another = input('Would you like to create another note or would you like to view notes? Enter create / view: ')
    if create_another == 'create' :
        create_note(name)
    elif create_another == 'view' :
        view_note(name)
    else :
        theNotes()

#since we broke our code up into functions, we have to make a function to start our application
def theNotes():
    print("Welcome to the theNotesCli application!")
    print("To begin, enter your username")
    name = find_user()
    view_or_create(name)

theNotes() #we call theNotes function here