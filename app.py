from config import *

import flask
from flask import Flask, request
from werkzeug.exceptions import HTTPException, default_exceptions

import PIL.Image
from PIL import UnidentifiedImageError
import senya

SUPERSENYA = senya.load_faces(MODEL_PATH)
TOLERANCE = TOLERANCE or senya.DEFAULT_TOLERANCE

app = Flask(__name__)

def handle_error(error):
    code = 500
    description = 'Internal Server Error'

    if isinstance(error, HTTPException):
        code = error.code
        description = error.description
    return flask.jsonify(code=code, error="http_error", description=description), code

for exc in default_exceptions:
    app.register_error_handler(exc, handle_error)

@app.route('/health')
def healthcheck():
    return 'ok'

@app.route('/check', methods=['POST'])
def check():
    if request.mimetype not in ALLOWED_MIMETYPES:
        return flask.jsonify(
            error='invalid_mimetype',
            description=f'mime type {request.mimetype} is not allowed',
        ), 415

    try:
        img = PIL.Image.open(request.stream, mode='r', formats=ALLOWED_PIL_FORMATS)
    except UnidentifiedImageError:
        return flask.jsonify(
            error='invalid_image',
            description=f'cannot identify image file',
        ), 400

    faces = senya.extract_faces(img)

    if senya.any_same_face(SUPERSENYA, faces, tol=TOLERANCE):
        return flask.jsonify(
            result=True,
            description=f'senya found',
        ), 200

    return flask.jsonify(
        result=False,
        faces_found=len(faces),
    ), 200
