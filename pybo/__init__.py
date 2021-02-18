from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    from .views import main_views, question_views, answer_views


    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    app.register_blueprint(main_views.bp)   # app에 블루 프린트 객체 bp 등록
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    app.config.from_object(config)
    return app

