from .import db
from flask_login import UserMixin
from . import login_manager



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
    comment = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    
    def __repr__(self):
        return f'User {self.username}'
    
    
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    comment = db.relationship('Comment', backref = 'comment', lazy = 'dynamic')
    
    @classmethod
    def get_pitches(cls, id):
        pitches = Pitch.query.order_by(pitch_id).desc().all()
        return pitches
    
    def __repr__(self):
        return f'Pitch {self.description}'
    

# class Comment(db.Model):
#     __tablename__='comments'
    
#     id = db.Column(db.Integer,primary_key=True)
#     pitch_id = db.Column(db.Integer, db.Foreign('pitches.id'))
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     description = db.Column(db.Text)
    
#     def __repr__(self):
#         return f"Comment : id: {self.id} comment: {self.description}"
              