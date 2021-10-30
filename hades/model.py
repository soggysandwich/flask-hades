from hades import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=100), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)


class Seller(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    seller_name = db.Column(db.String(length=100), nullable=False)
    adverts = db.relationship('Advert', backref='advert_seller', lazy=True)


class Advert(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    product = db.Column(db.String(length=500), nullable=False)
    price = db.Column(db.Integer())
    currency = db.Column(db.String(length=3))
    advertiser = db.Column(db.Integer(), db.ForeignKey('seller.id'))

    def __repr__(self):
        return f'Advert {self.product}'
