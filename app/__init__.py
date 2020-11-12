from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db=SQLAlchemy()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
db.init_app(app)
migrate=Migrate(app, db)


from app import models
from app import views




