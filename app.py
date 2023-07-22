from forms import RegisterForm, LoginForm, ForgetForm, Reset
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy as sq
import bcrypt
from flask_login import LoginManager, UserMixin
from flask_login import  login_user, current_user, logout_user

# from models import User, students
# from models import db



app = Flask(__name__)
app.secret_key = '1232@12hfseGGRDGS'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = sq(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    # Your code to load the user from the database based on the user_id goes here
    return User.query.get(int(user_id))  # Replace with your actual code



# #models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    gender = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def is_active(self):
        return True



# class students(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     FirstName = db.Column(db.String(100), nullable=False)
#     LasttName = db.Column(db.String(100), nullable=False)
#     midletName = db.Column(db.String(100), nullable=False)
#     motherName = db.Column(db.String(100), nullable=False)
#     dateOfBirth = db.Column(db.DateTime, nullable=False)
#     placeOfBirth = db.Column(db.String(100), nullable=False)


class students(db.Model):
    No = db.Column(db.Integer, primary_key=True)
    ID = db.Column(db.Text)
    Name = db.Column(db.Text)
    Username = db.Column(db.Text)
    Password = db.Column(db.Text)
    # field6 = db.Column(db.Text)
    # field7 = db.Column(db.Text)
    # field8 = db.Column(db.Text)
    # field9 = db.Column(db.Text)
    # field10 = db.Column(db.Text)
    # field11 = db.Column(db.Text)


class examsemister1(db.Model):
    No = db.Column(db.Integer, primary_key=True)
    # ID = db.Column(db.Text)
    Name = db.Column(db.Text)
    physics = db.Column(db.Integer)
    mathematics = db.Column(db.Integer)
    introduction = db.Column(db.Integer)
    English = db.Column(db.Integer)
    Arabic = db.Column(db.Integer)
    Total = db.Column(db.Integer)
    Average = db.Column(db.Text)
    Grade = db.Column(db.Text)
    status = db.Column(db.Text)



with app.app_context():
    db.create_all()




@app.route('/')
@app.route('/Home')
def Home():
    return render_template('home.html', title="Home")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    Form = RegisterForm()
    if Form.validate_on_submit():
        hashedPassword = bcrypt.hashpw(Form.password.data.encode('utf-8'), bcrypt.gensalt())
        email = User.query.filter_by(email=Form.email.data).first()
        username = User.query.filter_by(username=Form.username.data).first()
        if username:
          flash(f'already token this {Form.username.data}', category='danger')
        elif email:
          flash(f'already token this {Form.email.data}', category='danger')
        else:
            user  = User(username=Form.username.data, email=Form.email.data, gender=Form.gender.data, password=hashedPassword)
            db.session.add(user)
            db.session.commit()
            flash(f'You have successfully registered your account {Form.username.data}', category='success')
            return redirect('Home') 
    return render_template('register.html', form=Form, title='Register')





@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Home'))
    Form = LoginForm()
    if Form.validate_on_submit():
        # email = Form.email.data
        user = User.query.filter_by(email=Form.email.data).first()
        if user and bcrypt.checkpw(Form.password.data.encode('utf-8'), user.password):
            login_user(user)
            flash(f'You have successfully login your account', category='success')
            return redirect('studentsList')
        else:
            flash(f'Incorrect email or password', category='danger')

    return render_template('login.html', form=Form, title='Login')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('Home'))




@app.route('/studentsList', methods=['POST', 'GET'])
def studentsList():
    if not current_user.is_authenticated:
        flash(f'First sign in your account to view Students lists as possible!...', category='warning')
        return redirect('login')
    else:
        studentsNames = students.query.all()
        # print(studentsNames)
        return render_template('studentsList.html', title='Students List', students = studentsNames)
    

@app.route('/Exam', methods=['POST', 'GET'])
def Exam():
    if not current_user.is_authenticated:
        flash(f'First sign in your account to view Exam tab!...', category='warning')
        return redirect('login')
    else:
        Exam = examsemister1.query.all()
        return render_template('Exam.html', title='Students List', Exams = Exam)


@app.route('/ForgetPassword', methods=['POST', 'GET'])
def ForgetPassword():
    global Forgetform
    Forgetform = ForgetForm()
    if Forgetform.validate_on_submit():
        global user
        user = User.query.filter_by(email=Forgetform.email.data).first()
        print('the user is ' ,user)
        if not user:
            flash(f'The email was not valid please try again an valid email' , category="danger")
        else:
            return redirect(url_for('reset', user=user))

        
        
    return render_template('ForgetPassword.html', title='Forget Password',  form = Forgetform)
    


@app.route('/reset', methods=['POST', 'GET'])
def reset():
    # user = request.args.get('user')
    form = Reset()
    if form.validate_on_submit():
        # hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        user.password = form.password.data
        return redirect(url_for('login'))
    return render_template('resetPassword.html', form=form, user=user, title='Reset Password')






if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
