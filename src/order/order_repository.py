from ..models.models import db, Order

class OrderRepository:
    @staticmethod
    def find_all():
        return Order.query.all()

    @staticmethod
    def find_by_id(order_id):
        return Order.query.get(order_id)

    @staticmethod
    def add(item_name, costumer_id, image_filename=None):
        new_order = Order(item_name=item_name, costumer_id=costumer_id, image=image_filename)
        db.session.add(new_order)
        db.session.commit()

    @staticmethod
    def update(order):
        db.session.commit()

    @staticmethod
    def delete(order):
        db.session.delete(order)
        db.session.commit()
