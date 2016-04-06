# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 11:37:13 2016

@author: pravinth
"""

from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('flaskserver.cfg')

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
