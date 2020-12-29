from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length

class MovementForm(FlaskForm): #hereda de FlaskForm
    fecha = DateField('Fecha', validators=[DataRequired()])
    concepto = StringField('Concepto', validators=[DataRequired(), Length(min=10, message="Debe de tener al menos 10 caracteres")])
    cantidad = FloatField('Cantidad', validators=[DataRequired()])
    submit = SubmitField('Aceptar')