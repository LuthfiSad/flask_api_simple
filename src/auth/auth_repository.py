from ..models.models import db, User

class UserRepository:
    @staticmethod
    def add(name, email, password):
        new_costumer = User(name=name, email=email, password=password)
        db.session.add(new_costumer)
        db.session.commit()

    @staticmethod
    def find_by_email(email):
        return User.query.filter_by(email=email).first()
