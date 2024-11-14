from flask import Flask
from emails_bp import email_bp
from database import connection_url, init_db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = connection_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG"] = True

app.register_blueprint(email_bp)


with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(host='localhost',
            debug=True, #todo: maybe remove because we declared before.
            port=5000)