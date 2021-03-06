import os

app_dir = os.path.abspath(os.path.dirname(__file__))
files_store_folder = os.path.join(app_dir, 'files_store_folder')

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'StapdpxtwVJJaEaOXJjGnGuwDIJElMDQXRrp#LviK%#Qk&Ck'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.googlemail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'gmail@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'password'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

    FILES_PER_PAGE = 10

    PERMISSION = ['admin', 'moderator', 'user']
    STATUS_TYPE = {'in_work': 'in_work', 'closed': 'closed', 'cancelled': 'cancelled'}
    STATUS_TYPE_CSS = {'in_work': 'style="background: #FAD7A0;"',
                       'closed': 'style="background: #ABEBC6;"',
                       'cancelled': 'style="background: #AED6F1;"'}

    UPLOADED_PATH = os.path.join(app_dir, 'files_store_folder')
    UPLOADED_MAX_FILES = 7 * 1024 * 1024
    # Flask-Dropzone config:
    # DROPZONE_ALLOWED_FILE_TYPE ='image'
    # DROPZONE_MAX_FILE_SIZE = 10
    DROPZONE_MAX_FILES = 7
    # DROPZONE_IN_FORM = True
    # DROPZONE_UPLOAD_ON_CLICK = True
    # DROPZONE_UPLOAD_ACTION = 'handle_upload'  # URL or endpoint
    # DROPZONE_UPLOAD_BTN_ID = 'submit'



POSTGRESQL = 'postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(
                os.environ.get('DB_USER'),
                os.environ.get('DB_PASSWORD'),
                os.environ.get('DB_HOST'),
                os.environ.get('DB_PORT'),
                os.environ.get('DB_NAME'),
            )


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or POSTGRESQL


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or POSTGRESQL


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or POSTGRESQL
