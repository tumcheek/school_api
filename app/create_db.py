import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from config import db_config

# Establishing the connection
connection = psycopg2.connect(user=db_config['postgresql']['user'], password=db_config['postgresql']['pass'])
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Creating a cursor object
cursor = connection.cursor()

# Creating a database
cursor.execute('create database test_2')

# Close connection
cursor.close()
connection.close()
