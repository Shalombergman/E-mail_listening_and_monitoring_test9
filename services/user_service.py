from sqlalchemy.exc import SQLAlchemyError

from main_service import *
from main_service.database import session_maker
from main_service.models.device_info_model import DeviceInfoModel
from main_service.models.location_model import Location
from main_service.models.sentences_model import SentenceModel
from main_service.models.user import User
from services.sentences_service import hostage_and_explosive_words


def create_user(user_data):
    return User(
        username=user_data['username'],
        email = user_data['email']
    )


def create_location(location_data, user):
    return Location(
        latitude=location_data['latitude'],
        longitude=location_data['longitude'],
        city=location_data['city'],
        country=location_data['country'],
        user=user
    )

def create_device_info(device_data, user):
    return DeviceInfoModel(
        browser=device_data['browser'],
        os=device_data['os'],
        device_id=device_data['device_id'],
        user=user
    )

def create_sentence(sentence_data, user):
    return SentenceModel(
        sentence=sentence_data['sentence'],
        user=user
    )


def save_user_to_db(session, user):
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user.id
    except SQLAlchemyError as e:
        session.rollback()
        raise

def insert_user(user_data):
    try:
        with session_maker() as session:
            user = create_user(user_data)

            location = create_location(user_data['location'], user)
            user.location = location

            device_info = create_device_info(user_data['device_info'], user)
            user.device_info = device_info

            if sentences := user_data.get('sentences', []):
                hostage_and_explosive_words(sentences, user)

            return save_user_to_db(session, user)

    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
        return None
