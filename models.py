from core import app 

from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Image(db.Model):
    pass 


