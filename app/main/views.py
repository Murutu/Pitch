from flask import render_template


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


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'Hello World'
    return render_template('index.html',message = message)
    