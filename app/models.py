from .import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch', backref='user', lazy='dynamic')
    # comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)
    def __repr__(self):
        return f'User {self.username}'
    
    
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    # category =db.Column(db.ForeignKey('categories.id'))   
    # comment = db.Column(db.Integer,db.ForeignKey('comments.id'))
    
    
    @classmethod
    def get_pitches(cls,category):
        pitches=Pitch.query.filter_by(title=category).all()
        return pitches
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()        
    
    # @classmethod
    # def get_pitches(cls, id):
    #     pitches = Pitch.query.filter_by(id=id).first()
    #     return pitches
    
    def __repr__(self):
        return f'Pitch {self.description}'
    
# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String())
#     pitch = db.relationship('Pitch',backref = 'role',lazy="dynamic")
    

        
    
    
    
    
