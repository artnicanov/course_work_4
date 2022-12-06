from marshmallow import Schema, fields
from setup_db import db


class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(255), unique=True, nullable=False)  # устанавливаем уникальность и обязательность поля и
	password = db.Column(db.String(255), nullable=False)
	name = db.Column(db.String(255))
	surname = db.Column(db.String(255))
	favorite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"), nullable=False)  # любимый жанр подтягивается пользователю из модели жанров по id

class UserSchema(Schema):
	id = fields.Int()
	email = fields.Str()
	# password = fields.Str(load_only=True)  # позволит только загрузить поле и не взаимодействовать с ним для безопасности
	password = fields.Str()
	name = fields.Str()
	surname = fields.Str()
	favorite_genre = fields.Str()
