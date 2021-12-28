from application import db


class Regions(db.Model):
    region_id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(30), nullable=False)
    region_property_address = db.Column(db.String(30), nullable=False)
    region_price = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(30), nullable=False)
