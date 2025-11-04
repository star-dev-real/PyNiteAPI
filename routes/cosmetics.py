from flask import jsonify, Blueprint
from utils.helpers import load_json

cosmetics_bp = Blueprint('cosmetics', __name__)

@cosmetics_bp.route('/all-cosmetics')
def all_cosmetics():
    return jsonify(load_json("all_cosmetics.json"))