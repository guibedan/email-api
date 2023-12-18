from marshmallow import Schema, fields, validate


class EmailSchema(Schema):
    recipient_name = fields.String(required=True, validate=validate.Length(max=255))
    recipient_email = fields.Email(required=True, validate=validate.Length(max=255))
    subject = fields.String(required=True, validate=validate.Length(max=255))
    body = fields.String(required=True, validate=validate.Length(max=255))
