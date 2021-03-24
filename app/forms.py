from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields import TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired


class Form(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField("description", validators = [DataRequired()])   
    number_of_bedrooms = StringField("number_of_bedrooms", validators=[DataRequired()])
    number_of_bathrooms = StringField("number_of_bathrooms", validators=[DataRequired()])
    price= StringField("price", validators=[DataRequired()])

    ptype= SelectField("Type", choices=[("None", "Select Property Type"), ("House", "House"), ("Apartment", "Apartment")], validators=[DataRequired()])

    location = StringField("Location", validators = [DataRequired()])
    photo = FileField("photo", validators=[FileRequired()])
    
