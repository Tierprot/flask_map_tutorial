from app import db

class GeoData(db.Model):
    __tablename__='geodata'
    id = db.Column(db.Integer, primary_key=True)
    territory_name = db.Column(db.String(60), index=True, unique=True)
    features = db.Column(db.String(200))

    def __repr__(self):
        return 'territory: {}'.format(self.territory_name)
