from sqlalchemy.ext.declarative import declarative_base

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("project.config.Config")

db = SQLAlchemy(app)
Base = declarative_base()
