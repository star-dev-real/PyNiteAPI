from flask import jsonify, Blueprint
from utils.helpers import load_json

athena_bp = Blueprint('athena', __name__)

@athena_bp.route('/athena')
def athena():
    return jsonify(load_json("athena.json"))