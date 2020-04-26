# models.py

from flask_login import UserMixin
from . import db
#from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

#class MyModelView(ModelView):
#    pass

#admin = Admin()
#admin.add.view(MyModelView(User, db.session))