from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, BooleanField, SelectField  , RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=5, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Length(min=5, max=20), Email()])
    gender = SelectField('Gender', choices=[ ('Select', 'Select') , ('male', 'male') , ('female', 'female')],validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8), ])
    confirmPassword = PasswordField('confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sing Up')

    def validate_gender(self, field):
        if field.data == 'Select':
            raise ValidationError('Please select a valid gender option.')
        


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(min=5, max=20), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8), ])
    submit = SubmitField('Sing Up')


class ForgetForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(min=5, max=20), Email()])
    submit = SubmitField('Sing Up')



class Reset(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8), ])
    confirmPassword = PasswordField('confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sing Up')

