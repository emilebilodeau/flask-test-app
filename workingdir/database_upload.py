import pandas as pd
import sqlite3

# STEP 1: Use given data file on Lumber Futures to create a SQLite database to store it
df = pd.read_excel('OI - Copy of LumberFut.xlsx')

# connect & create database
connection = sqlite3.connect('demo.db')

# upload data to database
df.to_sql('LumberFut', connection, if_exists='replace')

# close
connection.close()