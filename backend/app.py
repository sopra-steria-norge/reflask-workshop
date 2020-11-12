import os
import logger

MODE = os.getenv('FLASK_ENV')
DEV_SERVER_URL = "http://localhost:3000"
# logging.getLogger('werkzeug').disabled = True

print(MODE)
