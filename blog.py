# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:20:09 2019

@author: Siyu
"""
import os

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app as app
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
import pickle
from sklearn.linear_model import LogisticRegression


bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    
    return render_template('blog/index.html')
'''
@bp.route('/show', methods=('GET', 'POST'))
@login_required
def show():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, score, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/show.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    filename = os.path.join(app.static_folder, 'finalized_model.sav')
    loaded_model = pickle.load(open(filename, 'rb'))
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
            Xnew=[[float(gender),float(education),float(diet),float(exercise),float(income),float(marriage),float(build),float(smoke),float(alcohol),float(blopre),float(chol)]]
            ynew=loaded_model.predict_proba(Xnew)
            db = get_db()
            db.execute(
                'INSERT INTO post (score, author_id)'
                ' VALUES (?, ?)',
                (round(float(ynew[0][1]),4), g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.show'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, score, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post
'''