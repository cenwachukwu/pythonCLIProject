#first after creating your directory and your file is to run {pipenv install psycopg2 then pipenv install} to install peewee in your file
#importing peewee
from peewee import *
from datetime import date 

#Using the PostgresqlDatabase class to create a database connection, 
#passing in the name of the database (in the case = notetaker), the user, the password, the host, and the port.
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