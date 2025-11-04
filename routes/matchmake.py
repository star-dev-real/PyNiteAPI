from flask import jsonify, Blueprint
from config import BASE_DIR
import os

matchmake_bp = Blueprint('matchmake', __name__)


@matchmake_bp.route('/')
def matchmake():
    return jsonify({
        "Matchmaking isn't supported with PyNite"
    }, 204)