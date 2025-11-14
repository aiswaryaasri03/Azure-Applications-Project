import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'images11'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'xoL4kg/avO/IRcJv3hgsS3+iAwWNiC49vGQB6iRpEZkmOn9J4d+Zd21usd1hsR7QPj5IJIP7Nv1L+AStxDcGow=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Azure SQL Database
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-west.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'cmsadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'CMS4dmin'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = (
        'mssql+pyodbc://'
        + SQL_USER_NAME + '@' + SQL_SERVER + ':'
        + SQL_PASSWORD + '@' + SQL_SERVER
        + ':1433/' + SQL_DATABASE
        + '?driver=ODBC+Driver+17+for+SQL+Server'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or 'VEc8Q~ZpEPXdEY6N5j2A0bL.FjDwGZrG6scckcpT'
    CLIENT_ID = os.environ.get('CLIENT_ID') or '30c213e4-d53f-4d89-8fe2-4297a9405b41'

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app

    REDIRECT_PATH = "/getAToken"  # Must match redirect_uri set in AAD

    # Permissions requested from Microsoft Graph
    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"  # Token cache stored in server-side session
