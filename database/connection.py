# import mysql.connector as SQLC

# # 1. login to database
# database_config = SQLC.connect(
#                         host = 'localhost',
#                         user = 'root',
#                         password = 'root', # your myswl workbench password
#                         database = 'notes_management3234'
#                     )

import sqlite3

database_config = sqlite3.connect('notes.db', check_same_thread=False)
cursor = database_config.cursor()