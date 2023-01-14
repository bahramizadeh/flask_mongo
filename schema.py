from marshmallow import Schema, fields
from pydantic import BaseModel, Field


class UserSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Str(required=True)

class UserEmailSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Str(required=True)


class UserEmailSchemaP(BaseModel):
    username : str
    password : str
    email : str

