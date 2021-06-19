# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present SharpObjects
"""
from datetime import datetime
from random import choice

from flask import render_template, request, jsonify
from flask_login import login_required
from jinja2 import TemplateNotFound

from app import db
from app.base.models import Common, Recommendation
from app.patient import blueprint


@blueprint.route('/write_data', methods=['POST', 'GET'])
def write_data():
    response = request.json
    common = Common(
        date=datetime.fromtimestamp(response["date"]),
        model_name=response["modelName"],
        high_value=response["highValue"],
        low_value=response["lowValue"],
        pulse=response["pulse"],
        activity=response["activity"]
    )
    db.session.add(common)
    db.session.commit()
    return jsonify(response)


@blueprint.route('/recommendation', methods=['GET'])
def recommendation():
    rec = db.session.query(Recommendation).order_by(Recommendation.id.asc()).all()
    return str(rec)


@blueprint.route('/dashboard')
@login_required
def dashboard():
    common = db.session.query(Common).order_by(Common.id.asc()).limit(5)
    return render_template('dashboard.html', segment='dashboard', common=common)


@blueprint.route('/transactions')
@login_required
def transactions():
    common = db.session.query(Common).order_by(Common.id.asc()).all()
    return render_template('transactions.html', segment='transactions', common=common)


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
    except Exception as e:
        print(f"Exception: {e}")
        return None
