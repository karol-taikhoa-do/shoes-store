from shoe_api.config import db, ma

class Shoe(db.Model):
    __tablename__ = "shoes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    desc = db.Column(db.String(200))
    shoe_size = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    shoe_type = db.Column(db.String(20))
    colour = db.Column(db.String(20))

class ShoeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Shoe
        load_instance = True
        sqla_session = db.session

shoe_schema = ShoeSchema()
shoes_schema = ShoeSchema(many=True)