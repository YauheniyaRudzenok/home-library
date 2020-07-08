from flask import jsonify, make_response


def ok(message=None):
    return make_response(_get_message(message), 200)


def created(message=None):
    return make_response(_get_message(message), 201)


def no_content():
    return make_response(_get_message(''), 204)


def bad_request(message=None):
    return make_response(_get_message(message), 400)


def not_found(message=None):
    return make_response(_get_message(message), 404)


def _get_message(message=None):
    return jsonify(message) if message else ""