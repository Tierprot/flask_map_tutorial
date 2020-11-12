from flask import render_template, jsonify, request
from app import app

from . import db
from .models import GeoData

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/ask')
def ask():
    param = request.args.get('param')
    result = GeoData.query.filter_by(territory_name=param).first_or_404()
    return jsonify(result=result.features)

