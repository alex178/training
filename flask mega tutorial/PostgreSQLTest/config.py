import os


WTF_CSRF_ENABLED = True
SECRET_KEY = 'rate_mal_178'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql:///mydb'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
