from flask import jsonify


def created(message=None):
    return _get_message(message), 201


def deleted(message=None):
    return _get_message(message), 204


def bad_request(message=None):
    return _get_message(message), 400


def not_found(message=None):
    return _get_message(message), 404


def _get_message(message=None):
    return jsonify(message) if message else ""