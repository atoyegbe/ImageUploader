from core import app 

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Image(db.Model):
    name = db.Column(db.String())
    image_type = db.Column(db.String())
    size = db.Column(db.Integer)

    def __init__(self, name, image_type, size):
        self.name = name 
        self.image_type = image_type
        self.size = size 

    def save(self):
        db.session.add(self)
        db.session.commit()
