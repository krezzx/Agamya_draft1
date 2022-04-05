from email.headerregistry import Address
from flask_wtf import Form
from wtforms import PasswordField,IntegerField,SubmitField,StringField,BooleanField,TextAreaField,SelectField
from wtforms.validators import DataRequired,Length,EqualTo


class RegistrationForm(Form):
    RollNo=IntegerField("Mobile NUmber",validators=[DataRequired()])
    userName=StringField("UserName",validators=[DataRequired(),Length(min=2,max=20)])
    emailId=StringField("Webmail",validators=[DataRequired()])
    address=TextAreaField("Local Address",validators=[DataRequired()])
    course=SelectField("Course",choices=[('Btech','Btech'),('MCA','MCA'),('M.Sc','M.sc'),('Mtech','Mtech')],validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired(),Length(min=8)])
    confirm_password=PasswordField("Confirm_Password",validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

class LoginForm(Form):
    emailId=StringField("Email",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    remember=BooleanField("remember me")
    submit=SubmitField('Login')