from flask import render_template
from .import main
from flask_login import login_required, current_user
from ..models import Pitch,User
 



# Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    return render_template('home.html')

@main.route('/pickuplines/<category>')
def pickuplines(category):
    '''
    view root page function that returns index and its data 
    '''
    pickuplines=Pickuplines.get_interviews(category)
    return render_template('pickuplines.html',pickuplines=pickuplines)

@main.route('/interview/<category>')
def interview(category):
    '''
    view root page function that returns index and its data 
    '''
    interview=Interview.get_interviews(category)
    return render_template('interview.html',interview=interview)

@main.route('/product/<category>')
def product(category):
    '''
    view root page function that returns index and its data 
    '''
    product=Product.get_product(product)
    return render_template('product.html',product=product)

@main.route('/promotion/<category>')
def promotion(category):
    '''
    view root page function that returns index and its data 
    '''
    promotion=Promotion.get_promotion(promotion)
    return render_template('promotion.html',promotion=promotion)












# @main.route('/pitches/new/', methods = ['GET','POST'])
# @login_required
# def new_pitch():
#     form = PitchForm()
#     if form.validate_on_submit():
#         description = form.description.data
#         title = form.title.data
#         owner_id = current_user
#         category = form.category.data
#         print(current_user._get_current_object().id)
#         new_pitch = Pitch(owner_id = current_user.get_current_object().id, title = title, description=description, category=category)
#         db.session.add(new_pitch)
#         db.session.commit() 
         
    