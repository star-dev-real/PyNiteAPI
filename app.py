from flask import Flask
import threading
import time

from routes.home import home_bp
from routes.athena import athena_bp
from routes.cosmetics import cosmetics_bp
from routes.image import image_bp
from routes.common_core import common_core_bp
from routes.content import content_bp
from routes.matchmake import matchmake_bp

from logic.athena import generate_athena
from logic.cosmetics import get_all_cosmetics

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(athena_bp)
app.register_blueprint(cosmetics_bp)
app.register_blueprint(image_bp)
app.register_blueprint(common_core_bp)
app.register_blueprint(content_bp)
app.register_blueprint(matchmake_bp)

def update_all():
    generate_athena()
    get_all_cosmetics()

def auto_update_profiles():
    while True:
        update_all()
        time.sleep(3600)

threading.Thread(target=auto_update_profiles, daemon=True).start()

if __name__ == '__main__':
    generate_athena()
    app.run()