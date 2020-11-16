import os
import logging
from flask import Flask, request, render_template
from classifier import classifyImage
from reverseProxy import proxyRequest

MODE = os.getenv('FLASK_ENV')
DEV_SERVER_URL = 'http://localhost:3000/'

logging.getLogger('werkzeug').disabled = True
app = Flask(__name__, template_folder='')

@app.route('/')
@app.route('/<path:path>')
def index(path=''):
    # Route through webpack-dev-server if development mode.
    if MODE == 'development':
        return proxyRequest(DEV_SERVER_URL, path)
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    if (request.files['image']): 
        file = request.files['image']

        result = classifyImage(file)

        print('Model classification: ' + result)
        
        return result
