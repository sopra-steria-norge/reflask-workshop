import os

MODE = os.getenv('FLASK_ENV')
DEV_SERVER_URL = "http://localhost:3000/"

print(MODE)
