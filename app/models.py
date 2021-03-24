from . import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(800))
    number_of_bedrooms = db.Column(db.String(30))
    number_of_bathrooms = db.Column(db.String(30))
    price = db.Column(db.String(200))
    location = db.Column(db.String(300))
    ptype = db.Column(db.String(60))
    photo = db.Column(db.String(80))
    
    __tablename__ = "property"
    
    def __init__(self,title,description,number_of_bedrooms,number_of_bathrooms,price,location,ptype,photo):
        self.title = title
        self.description = description
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price = price
        self.location = location
        self.ptype= ptype
        self.photo = photo
                         
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support


                         
    
    def __repr__(self):
        return "User: {0} {1}".format(self.firstname, self.lastname)
