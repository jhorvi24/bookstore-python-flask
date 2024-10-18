from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import boto3



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookStore.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from bookstore_management import routes
app.app_context().push()

#Cognito configuration
USER_POOL_ID = 'us-east-1_93g070eZC'
APP_CLIENT_ID = '187sh2q1h8m30g3uv4p28cis2p'
REGION = 'us-east-1'

cognito = boto3.client('cognito-idp', region_name=REGION)