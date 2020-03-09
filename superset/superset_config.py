#---------------------------------------------------------
# Superset specific config (defaults)
#---------------------------------------------------------
ROW_LIMIT = 5000
SUPERSET_WEBSERVER_PORT = 8088
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'
SQLALCHEMY_DATABASE_URI = 'sqlite:////home/superset/db/superset.db'
WTF_CSRF_ENABLED = True
WTF_CSRF_EXEMPT_LIST = []
MAPBOX_API_KEY = ''