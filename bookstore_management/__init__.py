from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import boto3



app = Flask(__name__)
ssm_client = boto3.client('ssm', region_name='us-east-1')

host = '/bookstore/host'
user = '/bookstore/user'
password = '/bookstore/password'
database = '/bookstore/database'

response = ssm_client.get_parameters(
    Names=[host, user, password, database],
    WithDecryption=True
)

rds_database = response['Parameters'][0]['Value']
rds_host = response['Parameters'][1]['Value']
rds_password = response['Parameters'][2]['Value']
rds_user = response['Parameters'][3]['Value']




app.config['SECRET_KEY'] = 'secret'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Test!2024@databasesbookstore.cz0i248ggya9.us-east-1.rds.amazonaws.com:3306/bookstore_db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqlconnector://{rds_user}:{rds_password}@{rds_host}:3306/{rds_database}'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from bookstore_management import routes
app.app_context().push()

