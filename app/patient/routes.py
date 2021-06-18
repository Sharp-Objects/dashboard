# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound

from app import db
from app.base.models import Indications
from app.patient import blueprint


@blueprint.route('/dashboard')
@login_required
def dashboard():
    indications = db.session.query(Indications).order_by(Indications.id.asc()).all()
    return render_template('dashboard.html', segment='dashboard', indications=indications)


@blueprint.route('/transactions')
@login_required
def transactions():
    indications = db.session.query(Indications).order_by(Indications.id.asc()).all()
    return render_template('transactions.html', segment='transactions', indications=indications)


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:
        if not template.endswith('.html'):
            template += '.html'
        segment = get_segment(request)
        return render_template(template, segment=segment)
    except TemplateNotFound:
        return render_template('page-404.html'), 404
    except:
        return render_template('page-500.html'), 500


def get_segment(request):
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment
    except:
        return None
