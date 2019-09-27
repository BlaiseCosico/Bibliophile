from flask_wtf import FlaskForm, Form
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, IntegerField, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User


class PhoneForm(FlaskForm):
    country_code = IntegerField('Country Code', validators=[DataRequired()])
    number = StringField('Phone Number', validators=[DataRequired(), Length(min=9, max=9)])
    #We could deal with the phone number issue in 2 ways.
    # 1) Create custom validation
    # 2) create custom form
    #http://wtforms.simplecodes.com/docs/0.6.1/fields.html#wtforms.fields.FormField
    #http://wtforms.simplecodes.com/docs/0.6.1/validators.html#custom-validators

class RegistrationForm(FlaskForm):
    # phone_number = StringField('Phone Number', validators=[DataRequired()])
    phone_number = FormField(PhoneForm, 'Phone Number')
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')




    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user:
    #         raise ValidationError('That username is already taken. Please choose another one.')

    # def validate_email(self, email):
    #     user = User.query.filter_by(username=email.data).first()
    #     if user:
    #         raise ValidationError('That email is already taken. Please choose a different email.')

   