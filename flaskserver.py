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
    return 'Hello World! If this is present then travis is able to successfully deploy to OpenShift!!'

@app.route('/pravinth/')
def hello_pravinth():
    return 'Hello <H2>Pravinth</H2>!'
    
@app.route('/kerastest/')
def keras_test():
    import theano, keras
    import keras.backend
    s = 'Theano Version is ' + theano.version.version
    s = s + '\nKeras is using backend - ' + str(keras.backend._BACKEND)
    return s

if __name__ == '__main__':
    app.run()
