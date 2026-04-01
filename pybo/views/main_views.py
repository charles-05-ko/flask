from flask import Blueprint, redirect, url_for

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

@bp.route('/hello')
def hello_world():
    return 'Hello Pybo!'

@bp.route('/bye')
def bye_world():
    return 'Bye Pybo!'