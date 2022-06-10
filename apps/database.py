from sqlalchemy import create_engine, databases
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sqlalchemy

import databases

DATABASE_URL="postgresql://postgres:password@10.211.55.5:5432/keycloak?sslmode=prefer"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL, pool_size=3, max_overflow=0
)

metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()