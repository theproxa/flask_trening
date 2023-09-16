from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

from models import *

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql//admin:admin@localhost/admin'
app.comfig['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app('app')


from core import routes
from core import models