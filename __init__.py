from flask import Flask,render_template,flash,request,url_for,redirect,session,g
from content_management import Content

from connector import connection
import gc
from wtforms import Form, BooleanField, TextField, PasswordField, validators

from passlib.hash import sha256_crypt
#from sqlite3 import escape_string as thwart

TOPIC_DICT = Content()

app = Flask(__name__)

app.config['SECRET_KEY'] = "it'ssecret"

class RegistrationForm(Form):
    username = TextField("Username",[validators.Length(min=4,max=20)])
    email = TextField("Email Address",[validators.Length(min=6,max=50)])
    password = PasswordField('Password',[validators.Required(),validators.EqualTo('confirm',message='the password must be equal')])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the Terms of services and the privacy notice')

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
    flash('flash test')
    return render_template("dashboard.html",topics=TOPIC_DICT)

    
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def page_not_found(e):
    return "Oops ,knocked out",500

@app.route('/register/',methods=['GET','POST'])
def register_page():
    try:
        #c,conn = connection()
        form = RegistrationForm(request.form)
        
        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt(str(form.password.data))
            
            c,conn = connection()
            
            x = c.execute("SELECT * FROM users WHERE username = ?",(username,))
            
            r = c.fetchall()
            
            if len(r) > 0:
                flash("That username is already taken,")
                return render_template('register.html',form=form)
            else:
                c.execute("INSERT INTO users (username,password,email,tracking) VALUES (?,?,?,?)",(username,password,email,"/introduction_to_pythonprograming/"))
                conn.commit()
                
                flash("Thankks for registering")
                c.close()
                conn.close()
                
                gc.collect()
                
                session['logged_in'] = True
                session['username'] = username
                
                return redirect(url_for('dashboard'))
                
        return render_template('register.html',form=form)
            
    except Exception as e:
        return str(e)
    
    
@app.route('/login/',methods=['GET','POST'])
def login_page():
    error = None
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            
            flash(attempted_username)
            flash(attempted_password)
            
            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))
            else:
                error = "invalid credentials,Try Again."
                
        return render_template("login.html",error=error)
    
    except Exception as e:
        flash(e)
        return render_template("login.html",error=error)
    
if __name__ == "__main__":
    app.run()
