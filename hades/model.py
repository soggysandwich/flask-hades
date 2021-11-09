from hades import db, bcrypt, login_manager
from flask_login import UserMixin
from datastore_entity import DatastoreEntity,EntityValue

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=100), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_pw):
        self.password_hash = bcrypt.generate_password_hash(plain_text_pw).decode('utf-8')

    def check_password(self, password_to_check):
        return bcrypt.check_password_hash(self.password_hash, password_to_check)


class Seller(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    seller_name = db.Column(db.String(length=100), nullable=False)
    #adverts = db.relationship('Advert', backref='advert_seller', lazy=True)


class Advert(DatastoreEntity):
    """
    id = db.Column(db.Integer(), primary_key=True)
    product = db.Column(db.String(length=500), nullable=False)
    price = db.Column(db.Integer())
    currency = db.Column(db.String(length=3))
    advertiser = db.Column(db.Integer(), db.ForeignKey('seller.id'))

    """

    title=EntityValue(None)
    price=EntityValue(None)
    currency=EntityValue(None)
    country=EntityValue(None)
    found_date=EntityValue(None)
    location=EntityValue(None)

    # name of entity's kind
    __kind__ = "ebay-adverts"

    def __repr__(self):
        return f'Advert {self.title}'


