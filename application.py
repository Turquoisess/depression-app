#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:28:53 2019

@author: z1s1y8
"""

import pickle
from flask import Flask, render_template, request, redirect, flash, url_for, session



# Initialise the Flask app
app = Flask(__name__)
        
app.vars={}

@app.route('/')
def main():
    return redirect('/index')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/show', methods=('GET', 'POST'))
def show():
    result = 0.0025
    result = request.args['result']
    return render_template('show.html', result = result)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        gender = request.form.get('gender')
        education = request.form.get('education')
        diet = request.form.get('diet')
        exercise = request.form.get('exercise')
        income = request.form.get('income')
        marriage = request.form.get('marriage')
        build = request.form.get('build')
        smoke = request.form.get('smoke')
        alcohol = request.form.get('alcohol')
        blopre = request.form.get('blopre')
        chol = request.form.get('chol')
        error = None
        
        if error is not None:
            flash(error)
        else:
            '''
            # Use pickle to lead in the pre-trained model
            with open(f'static/finalized_model.pkl', 'rb') as f:
                loaded_model = pickle.load(f)                
            Xnew=[[float(gender),float(education),float(diet),float(exercise),float(income),float(marriage),float(build),float(smoke),float(alcohol),float(blopre),float(chol)]]
            ynew=loaded_model.predict_proba(Xnew)
            session['result'] = round(float(ynew[0][1]),4)
            '''
            result = 0.2548
            return redirect(url_for('show', result = result))
    return render_template('create.html')



if __name__=="__main__":
    app.run(debug=True)
