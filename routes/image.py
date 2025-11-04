from flask import send_file, Blueprint
import os
from config import BASE_DIR

image_bp = Blueprint('images', __name__)

@image_bp.route('/image')
def image():
    image_path = os.path.join(BASE_DIR, "images/image.ico")
    
    if not os.path.exists(image_path):
        return {"error": "PyNite image not found"}, 404
    
    return send_file(image_path, mimetype='image/ico')