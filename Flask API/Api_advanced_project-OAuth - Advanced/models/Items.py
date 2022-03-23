from models.base_model import db


class Items(db.Model):

    __tablename__="items"
    id=db.Column(db.Integer,primary_key=True)
    item_name=db.Column(db.String,unique=True,nullable=False)
    price=db.Column(db.Float(2),nullable=False)
    quantity=db.Column(db.Integer,nullable=False)
    store_id=db.Column(db.Integer,db.ForeignKey("stores.id"))

    store=db.relationship("Stores")

    def register_item(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_item(cls,item_name):
        result=cls.query.filter_by(item_name=item_name).first()
        return result

    @classmethod
    def get_all(cls):
        result=cls.query.all()
        return result

    @classmethod
    def delete_item(cls,item_name):
        item=cls.get_item(item_name)
        db.session.delete(item)
        db.session.commit()

    @classmethod
    def update_item(cls,item_name,price,quantity):
        item=cls.query.filter_by(item_name=item_name).first()
        item.price=price
        item.quantity=quantity
        db.session.commit()


