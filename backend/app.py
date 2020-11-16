import os
import logging
from flask import Flask, request, render_template, send_from_directory
from classifier import classifyImage
from reverseProxy import proxyRequest

MODE = os.getenv('FLASK_ENV')
DEV_SERVER_URL = 'http://localhost:3000/'

logging.getLogger('werkzeug').disabled = True
app = Flask(__name__, template_folder='static')

@app.route('/')
@app.route('/<path:path>')
def index(path=''):
    # Route through webpack-dev-server if development mode.
    if MODE == 'development':
        return proxyRequest(DEV_SERVER_URL, path)
    if path and os.path.exists(app.static_folder + '/' + path):
       return send_from_directory(app.static_folder, path)
    else:
        return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if (request.files['image']): 
        file = request.files['image']

        result = classifyImage(file)

        print('Model classification: ' + result)
        
        return result
