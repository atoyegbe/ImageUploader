from core import app 

from flask import request, jsonify
from werkzeug.utils import secure_filename


from models import Image 
from schema import imageSchema

app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024
app.config["UPLOAD_EXTENSIONS"] = ['.jpg', '.png']


def checkImageProperties():
    pass 

@app.route('/image', methods=['POST'])
def imageUpload():
    pass

