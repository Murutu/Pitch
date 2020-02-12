from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email,EqualTo

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description = TextAreaField("What would you like to pitch?",validators=[Required()])
	category = RadioField('Label', choices=[ ('promotionpitch','promotionpitch'), ('interviewpitch','interviewpitch'),('pickuplines','pickuplines'),('productpitch','productpitch')],validators=[Required()])
    submit = SubmitField('Submit')