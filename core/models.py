from core import db
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique = True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

class Catigorie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    categorie_name = db.Column(db.String(80), unique = True)
    categorie_image = db.Column(db.String(256))
    
    def __repr__(self):
        return '<categorie_name %r>' % self.categorie_name

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    product_name = db.Column(db.String(80))
    product_description = db.Column(db.String(1024))
    price = db.Column(db.Integer)
    product_image = db.Column(db.String(256))
    
    def __repr__(self):
        return '<product_id %r>' % self.product_id

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(128))
    
    product_id = db.Column(db.Integer, db.ForeignKey('id'))
    post = db.relationship('Product',backref = db.backref('comments', lazy='dynamic' ))
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref = db.backref('comments', lazy='dynamic') )
    
        
    
    def __repr__(self):
        return '<comment_id %r>' % self.comment_id
    
