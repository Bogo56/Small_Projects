from models.base_model import db

##We're using falsk-marschmello for seriliazation json-model,model-json
# , so no need for __init__ and to json() method

class Stores(db.Model):

    __tablename__="stores"
    id=db.Column(db.Integer,primary_key=True)
    store_name=db.Column(db.String,unique=True,nullable=False)

    items=db.relationship("Items")

    def register_item(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_store(cls,store_name):
        result=cls.query.filter_by(store_name=store_name).first()
        return result

    @classmethod
    def get_all(cls):
        result=cls.query.all()
        return result

    @classmethod
    def delete_item(cls,store_name):
        store=cls.get_store(store_name)
        db.session.delete(store)
        db.session.commit()

    # @classmethod
    # def update_item(cls, store_name, price, quantity):
    #     store=cls.query.filter_by(item_name=store_name).first()
    #     store.price=price
    #     store.quantity=quantity
    #     db.session.commit()


