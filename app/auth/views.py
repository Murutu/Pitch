from ..email import mail_message

@auth.route('/register',methods = ["GET","POST"])
def register():
    from = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.user.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        
        mail_message("Welcome to pitch","email/welcome",user.email,user=user)
        
 return render_template('auth/register.html',registration_form = form)        