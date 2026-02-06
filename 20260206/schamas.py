# 책 스키마 정의
from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.String(required=True)
    author = fields.String(required=True)