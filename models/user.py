from db import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        data = cls.query.filter_by(username=name).first()
        return data
        # return {
        #     "username": data["username"],
        #     "password": data["password"],
        #     "email": data["email"]
        # }

    @classmethod
    def all_users(cls):
        # data = cls.query.order_by(cls.username).all()
        data = cls.query.all()
        return data