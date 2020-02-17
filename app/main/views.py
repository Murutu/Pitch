from flask import render_template,redirect, url_for
from .import main
from flask_login import login_required, current_user
from ..models import Pitch,User 
from .forms import PitchForm

# Pitch = pitch.Pitch
 



# Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch'
    pickuplines_pitches = Pitch.get_pitches('pickuplines')
    interview_pitches = Pitch.get_pitches('interview')
    product_pitches = Pitch.get_pitches('product')
    promotion_pitches = Pitch.get_pitches('promotion')
    return render_template('home.html', title=title,pickuplines=pickuplines_pitches,interview=interview_pitches,product=product_pitches,promotion_pitches=promotion_pitches)

@main.route('/pitch/new', methods = ['GET','POST'])
# @login_required
def create_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.description.data
        # category = pitch_form.category.data
        
        create_pitch = Pitch(title=title, description=pitch)
        
        create_pitch.save_pitch()
        return redirect(url_for('.index'))
    return render_template('create_pitch.html',pitch_form=pitch_form)
    

@main.route('/pickuplines')
def pickuplines():
    '''
    view root page function that returns index and its data 
    '''
    pitches=Pitch.query.filter_by(title='pickuplines').all()
    return render_template('promotion.html',pitches=pitches)

@main.route('/interview')
def interview():
    '''
    view root page function that returns index and its data 
    '''
    pitches=Pitch.query.filter_by(title='interview').all()
    return render_template('promotion.html',pitches=pitches)

@main.route('/product')
def product():
    '''
    view root page function that returns index and its data 
    '''
    pitches=Pitch.query.filter_by(title='product').all()
    return render_template('promotion.html',pitches=pitches)

@main.route('/promotion')
def promotion():
    '''
    view root page function that returns index and its data 
    '''
    pitches=Pitch.query.filter_by(title='promotion').all()
    return render_template('promotion.html',pitches=pitches)













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
         
    