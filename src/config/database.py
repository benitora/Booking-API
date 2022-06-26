from venv import create
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from urllib import urlquote
import logging

from config.settings import Settings
setting = Settings()

engine = create_engine("mysql+pymysql://"+setting.DB_USERNAME+":"+setting.DB_PASSWORD+"@"+setting.DB_HOST+":"+setting.DB_PORT+"/"+setting.DB_NAME)
# db = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# import os
# from dotenv import load_dotenv
# load_dotenv()

# try:
#     connection = mysql.connector.connect(host='localhost',
#                                          database='Electronics',
#                                          user='pynative',
#                                          password='pynative@#29')
#     if connection.is_connected():
#         db_Info = connection.get_server_info()
#         print("Connected to MySQL Server version ", db_Info)
#         cursor = connection.cursor()
#         cursor.execute("select database();")
#         record = cursor.fetchone()
#         print("You're connected to database: ", record)

# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")