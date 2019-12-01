#first after creating your directory and your file is to run {pipenv install peewee then pipenv install psycopg2-binary} to install peewee in your file
#importing peewee
from peewee import *
from datetime import date 

#Using the PostgresqlDatabase class to create a database connection, 
#passing in the name of the database (in the case = notetaker), the user (postgres), the password (blank), the host (localhost), and the port.
db = PostgresqlDatabase('notetaker', user='postgres', password='',
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
    title = CharField()
    date = DateField()
    notes = CharField()
        # both CharField() and DateField() are from PeeWee's datatypes. others are BooleanField(), IntegerField() etc.
        # CharField() basically means that both the title and note fields are strings and 
        # the DateField() means that the date field will take a date

#db.create_tables([NoteTaker]) to add this table to the database
db.create_tables([NoteTaker])

# creating interactive input logic for creating the data
note = input("view note or create new note?")
if note == 'view note':
    searchtitle= input("Type in title: ") #ask for input to enable us to select() search in the next step
    result = NoteTaker.select().where(NoteTaker.title == searchtitle).get()     # Get/Select request to find a note by title
                    #above we select from the notetakerdb, but more specifically we select from where the title == searchtitle and then get.
                    #our first step to achieving crud.
    print(result.date)
    print(result.title)
    print(result.notes)
elif note == 'create new note':
    #first step to creating a new note is to collect inputs 
    # date input below is always year, date, month in that order, also because the date a num/integer, we wrap the input in int eg.
    # int(input())
    year = int(input('Enter the year like so (2012) '))
    month = int(input('Enter the month number like so (for March type 3): '))
    day = int(input('Enter the day number like so (21): '))
    # we can also ask for date input like so: date = int(input(enter date like so (1990, 11, 18)))
    title = input('Add a title for your new note: ')
    notes = input('Add some content to your note: ')
