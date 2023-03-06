import sqlite3

# connect to db
connection = sqlite3.connect("data/contacts.db")

#  create db cursor
cursor = connection.cursor()

# enter row id to update
firstname = input('Enter first name: ')
lastname  = input('Enter last name: ')
email     = input('Enter email: ')

# ---------------
#    YOUR CODE
# ---------------
