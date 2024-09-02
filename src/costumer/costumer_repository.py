from ..models.models import db, Costumer

class CostumerRepository:
    @staticmethod
    def find_all():
        return Costumer.query.all()

    @staticmethod
    def find_by_id(costumer_id):
        return Costumer.query.get(costumer_id)

    @staticmethod
    def find_by_email(email):
        return Costumer.query.filter_by(email=email).first()

    @staticmethod
    def add(name, email):
        new_costumer = Costumer(name=name, email=email)
        db.session.add(new_costumer)
        db.session.commit()

    @staticmethod
    def update(costumer):
        db.session.commit()

    @staticmethod
    def delete(costumer):
        db.session.delete(costumer)
        db.session.commit()
