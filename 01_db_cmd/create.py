import sqlite3

# connect to db
connection = sqlite3.connect("data/contacts.db")

#  create db cursor
cursor = connection.cursor()

firstname = input('Enter first name: ')
lastname  = input('Enter last name: ')
email     = input('Enter email: ')

# ---------------
#    YOUR CODE
# ---------------
