from flask_restx import fields


class Base64String(fields.Raw):
    def format(self, value):
        return value.decode('utf-8')