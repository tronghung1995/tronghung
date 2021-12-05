import json
import sys
import configparser
import psycopg2
import uvicorn
from fastapi import FastAPI
from con_database import engineDB_BRVT, session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker


engine = engineDB_BRVT
#schema_name = "import_data"
#table_name = "ktts_tonghop_tinh"
table_name = "import_data.ktts_tonghop_tinh"
with engine.connect() as connection:
    sql_select = ("""SELECT * FROM import_data.ktts_tonghop_tinh;""")
    result = connection.execute(sql_select)
    for i in result:
        print(i)