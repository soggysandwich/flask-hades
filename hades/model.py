from hades import db


class Advert(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    seller = db.Column(db.String(length=200), nullable=False)
    product = db.Column(db.String(length=500), nullable=False)
    price = db.Column(db.Integer())
    currency = db.Column(db.String(length=3))

    def __repr__(self):
        return f'Advert {self.seller}'