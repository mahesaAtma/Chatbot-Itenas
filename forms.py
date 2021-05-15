# ==========================================================
# CREATOR : Mahesa Atmawidya Negara Ekha Salawangi
# DATE CREATED : 20 JUNE 2020
# ABOUT : Simple Chatbot Itenas
# ==========================================================

from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

class chatForm(FlaskForm):
    user_input = StringField('User Input',validators=[DataRequired()])
    submit = SubmitField('Chat')
