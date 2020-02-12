from flask import render_template
from .import main
from flask_login import login_required, current_user
 



# Views
@main.route('/', methods = ['GET','POST'])
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    pickuplines = Pitch.query.filter_by(category="pickuplines")
    interviewpitch = Pitch.query.filter_by(category = "interviewpitch")
    promotionpitch = Pitch.query.filter_by(category = "promotionpitch")
    productpitch = Pitch.query.filter_by(category = "productpitch")
    
    return render_template('home.html', title = 'title', pickuplines=pickuplines, interviewpitch=interviewpitch, promotionpitch=promotionpitch, productpitch=productpitch)


@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id = current_user.get_current_object().id, title = title, description=description, category=category)
        db.session.add(new_pitch)
        db.session.commit() 
         
    