from flask import Flask, jsonify, make_response

app = Flask(__name__)

from application.rmflib.handler.direct import *

@app.errorhandler(400)
def not_found(error):
    """
    Handles the 400 error if some occures. Because we are an API server return json
    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    """
    Handles the 404 error if some occures. Because we are an API server return json
    :param error:
    :return:
    """
    return make_response(jsonify({'error': 'Not found'}), 404)
