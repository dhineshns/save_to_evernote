import sys
sys.path.insert(0, 'lib')
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
