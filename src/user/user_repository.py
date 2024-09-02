from src.models.models import db, User

class UserRepository:
    @staticmethod
    def find_all():
        return User.query.all()

    @staticmethod
    def find_by_id(user_id):
        return User.query.get(user_id)

    # @staticmethod
    # def find_by_email(email):
    #     return User.query.filter_by(email=email).first()

    # @staticmethod
    # def add(name, email):
    #     new_user = User(name=name, email=email)
    #     db.session.add(new_user)
    #     db.session.commit()

    # @staticmethod
    # def update(user):
    #     db.session.commit()

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()
