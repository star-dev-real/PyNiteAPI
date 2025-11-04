from flask import jsonify, Blueprint
from utils.helpers import load_json

common_core_bp = Blueprint('common_core', __name__)

@common_core_bp.route('/common_core')
def common_core():
    return jsonify(load_json("common_core.json"))