from flask import Blueprint, request, jsonify

from emails_producer.emails_producer import all_email
from main_service.database import save_to_mongo

email_bp = Blueprint("email_bp", __name__)
@email_bp.route('api/email', methods=['POST'])
def email():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'no data'}), 400
    all_email(data)
    save_to_mongo(data)

    return jsonify(data), 201

