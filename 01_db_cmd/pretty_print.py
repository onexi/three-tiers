# Printing Lists as Tabular Data
# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

# Console colors - rick pythong package
# https://github.com/willmcgugan/rich

# Markdown tables - Github syntax
# https://docs.github.com/en/github/writing-on-github/organizing-information-with-tables

import sqlite3
from tabulate import tabulate

# connect to db
connection = sqlite3.connect("data/contacts.db")

#  create db cursor
cursor = connection.cursor()

# ---------------
#    YOUR CODE
# ---------------
