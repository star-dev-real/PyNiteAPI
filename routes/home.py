from flask import jsonify, Blueprint
from config import BASE_DIR
import os

home_bp = Blueprint('home', __name__)

routes = []

routes_dir = os.path.join(BASE_DIR, "routes")
files = os.listdir(routes_dir)

for file in files:
    if file.endswith('.py') and file != '__init__.py' and file != 'home.py':
        file_name = file.replace(".py", "")
        routes.append(f"/{file_name}")

@home_bp.route('/')
def home():
    return jsonify({
        "available_endpoints": routes
    })