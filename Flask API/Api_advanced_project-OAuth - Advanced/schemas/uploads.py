from marshmallow import fields, Schema
from werkzeug.datastructures import FileStorage
from marshmallow.exceptions import ValidationError


##This is just Marschmello, not flask-marschmello
class ImageField(fields.Field):
    default_error_messages = {
        "invalid": "Not a file of type FileStorage"
    }

    def _deserialize(self, value, attr, data, **kwargs):

        if value is None:
            return None
        elif not isinstance(value, FileStorage):
            self.fail("invalid")

        return value


class ImageSchema(Schema):
    image = ImageField(required=True)
