#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:28:53 2019

@author: z1s1y8
"""

#import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
    SECRET_KEY='dev',
#    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
#if test_config is None:
    # load the instance config, if it exists, when not testing
#    app.config.from_pyfile('config.py', silent=True)
#else:
    # load the test config if passed in
#    app.config.from_mapping(test_config)
        
        # ensure the instance folder exists
#try:
#    os.makedirs(app.instance_path)
#except OSError:
#    pass
       
#from . import db
#db.init_app(app)
    
#from . import auth
#app.register_blueprint(auth.bp)
    
#from . import blog
#app.register_blueprint(blog.bp)
#app.add_url_rule('/', endpoint='index')
        
app.vars={}

def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
