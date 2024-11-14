from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from main_service.models.Base import Base
from models import *
import os
from pymongo import MongoClient



#postgres
#todo: can be converted to env variable via os.environ.get('DB_URL')
connection_url = 'postgresql://shalom:1234@db-sql:5432/email_monitoring_db'
engine = create_engine(connection_url, convert_unicode=True)
session_maker = sessionmaker(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    import models
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    with session_maker() as session:
        session.commit()


#nongodb
client = MongoClient(os.getenv("mongodb://localhost:27017/"))
mongo_db = client['email_monitoring_db']
mongo_collection = mongo_db["all_messages"]
all_messages = client['all_messages']
emails = all_messages['emails']


def save_to_mongo(data):
    mongo_collection.insert_one(data)

