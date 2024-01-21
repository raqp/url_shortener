import os
from dotenv import load_dotenv

from sqlalchemy import create_engine, MetaData, Column, String
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

Base = declarative_base()


class URLS(Base):
    __tablename__ = 'urls'

    original_url = Column(String, primary_key=True, autoincrement=False)
    short_url = Column(String)


Base.metadata.create_all(bind=engine)
