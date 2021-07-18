from core import app
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

class ImageSchema(ma.Schema):
    class Meta:
        fields: ('name', 'image_type', 'size')


imageSchema = ImageSchema()
