from flask import Flask
from app.configs import configs, database, migration
from app.routes import vacine_route

def create_app():
    app = Flask(__name__)

    configs.init_app(app)
    database.init_app(app)
    migration.init_app(app)

    app.register_blueprint(vacine_route.bp)

    return app