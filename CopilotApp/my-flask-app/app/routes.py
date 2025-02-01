from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return jsonify({"message": "Welcome to my Flask app!"})

@bp.route('/api/data')
def get_data():
    return jsonify({"data": "This is some sample data."})

@bp.route('/api/about')
def about():
    return jsonify({"about": "This is a sample Flask application."})