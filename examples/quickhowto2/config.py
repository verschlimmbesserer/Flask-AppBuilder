import os
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/quickhowto'
#SQLALCHEMY_DATABASE_URI = 'postgresql://fab:password@localhost:5432/quickhowto2'
#SQLALCHEMY_ECHO = True


BABEL_DEFAULT_LOCALE = 'en'
BABEL_DEFAULT_FOLDER = 'translations'
LANGUAGES = {
    'en': {'flag': 'gb', 'name': 'English'},
    'pt': {'flag': 'pt', 'name': 'Portuguese'},
    'es': {'flag': 'es', 'name': 'Spanish'},
    'de': {'flag': 'de', 'name': 'German'},
    'zh': {'flag': 'cn', 'name': 'Chinese'},
    'ru': {'flag': 'ru', 'name': 'Russian'}
}


#------------------------------
# GLOBALS FOR GENERAL APP's
#------------------------------
UPLOAD_FOLDER = basedir + '/app/static/uploads/'
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'
IMG_UPLOAD_URL = '/static/uploads/'
AUTH_TYPE = AUTH_DB
AUTH_LDAP_SERVER = "ldap://testdc.test.local"
AUTH_LDAP_SEARCH = "dc=test,dc=local"
AUTH_LDAP_UID_FIELD = 'userPrincipalName'
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Admin'
AUTH_ROLE_ADMIN = 'Admin'
AUTH_ROLE_PUBLIC = 'Public'

OAUTH_PROVIDERS = [
    {'name':'twitter', 'icon':'fa-twitter',
        'remote_app': {
            'consumer_key':'xBeXxg9lyElUgwZT6AZ0A',
            'consumer_secret':'aawnSpNTOVuDCjx7HMh6uSXetjNN8zWLpZwCEU4LBrk',
            'base_url':'https://api.twitter.com/1.1/',
            'request_token_url':'https://api.twitter.com/oauth/request_token',
            'access_token_url':'https://api.twitter.com/oauth/access_token',
            'authorize_url':'https://api.twitter.com/oauth/authenticate'}
    }
    ]


APP_NAME = "F.A.B. Example"
APP_ICON = "/static/img/brand.jpg"
#APP_THEME = "bootstrap-theme.css"  # default
#APP_THEME = "cerulean.css"      # COOL
#APP_THEME = "amelia.css"
#APP_THEME = "cosmo.css"
#APP_THEME = "cyborg.css"       # COOL
#APP_THEME = "flatly.css"
#APP_THEME = "journal.css"
#APP_THEME = "readable.css"
#APP_THEME = "simplex.css"
#APP_THEME = "slate.css"          # COOL
#APP_THEME = "spacelab.css"      # NICE
#APP_THEME = "united.css"
#APP_THEME = "yeti.css"
