from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))
Base = declarative_base()
Metadata =MetaData()

conn = engine.connect()
Meta = MetaData()

Session = sessionmaker(bind=engine)
session = Session()
