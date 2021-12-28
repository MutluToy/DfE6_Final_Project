from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class RegionForm(FlaskForm):
    region_name = StringField(label="Region Name", validators=[DataRequired()])
    region_property_address = StringField(label="Region Type", validators=[DataRequired()])
    region_price = StringField(
        label="Region Price", validators=[DataRequired()])
    description = StringField(label="Description", validators=[DataRequired()])
    submit = SubmitField("Create Region")
