# Define database connection using SQLAlchemy 
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get config db file
script_dir = os.path.dirname(__file__)
rel_path = "../config/config.json"
abs_file_path = os.path.join(script_dir, rel_path)
configFile = open(abs_file_path, "r")
configFile = json.load(configFile)

# Get database connection
def get_db_connect(q_projectName):
    host = configFile['project'][q_projectName]['pg_database']['host']
    user = configFile['project'][q_projectName]['pg_database']['user']
    password = configFile['project'][q_projectName]['pg_database']['password']
    port =configFile['project'][q_projectName]['pg_database']['port']
    database = configFile['project'][q_projectName]['pg_database']['database']

    SQLALCHEMY_DATABASE_URL = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(SQLALCHEMY_DATABASE_URL, echo = False)
    print(f'DB connected: {host}, {user}, {port} , {database}')
    return engine

engineDB_BRVT = get_db_connect('BRVT')
Session = sessionmaker(bind=engineDB_BRVT)
session = Session()