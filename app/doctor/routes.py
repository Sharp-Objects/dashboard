# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, redirect, request
from flask_login import login_required
from jinja2 import TemplateNotFound

from app import db
from app.base.models import Patient, Recommendation
from app.doctor import blueprint


@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html', segment='index')


@blueprint.route('/doc_main')
@login_required
def doc_main():
    patient = db.session.query(Patient).order_by(Patient.id.asc()).all()
    return render_template('doc_main.html', segment='doc_main', patient=patient)


@blueprint.route('/add_recommendations')
@login_required
def add_recommendations():
    recommendations = db.session.query(Recommendation).join(Patient,
                                                            Recommendation.patient_snils == Patient.snils).all()
    patient_name = db.session.query(Patient).join(Recommendation, Recommendation.patient_snils == Patient.snils).all()
    return render_template('add_recommendations.html',
                           segment='add_recommendations',
                           recommendations=recommendations,
                           patient_name=patient_name)


@blueprint.route('/add_recommendations', methods=["POST"])
@login_required
def add_recommendations_post():
    text = request.form["text"]
    req = db.session.query(Recommendation).first()
    req.text = text
    db.session.commit()
    return redirect(request.url)


@blueprint.route('/<template>')
@login_required
def route_template(template):
    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/FILE.html
        return render_template(template, segment=segment)

    except TemplateNotFound:
        return render_template('page-404.html'), 404

    except:
        return render_template('page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
