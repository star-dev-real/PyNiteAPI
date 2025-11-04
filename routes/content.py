from flask import jsonify, Blueprint
from utils.helpers import load_json

content_bp = Blueprint('content', __name__)

@content_bp.route('/athena')
def content():
    return jsonify(load_json("content.json"))