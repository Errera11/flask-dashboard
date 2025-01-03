from flask_wtf import FlaskForm
from wtforms  import TextField, TextAreaField, DateTimeField, PasswordField
from wtforms.validators import Required

class ExampleForm(FlaskForm):
	title = TextField(u'Título', validators = [Required()])
	content = TextAreaField(u'Conteúdo')
	date = DateTimeField(u'Data', format='%d/%m/%Y %H:%M')
	#recaptcha = RecaptchaField(u'Recaptcha')

class LoginForm(FlaskForm):
	user = TextField(u'Usuário', validators = [Required()])
	password = PasswordField(u'Senha', validators = [Required()])


class SaleForm(FlaskForm):
	title = TextField(u'Create sale')
	total_amount = TextField(u'Sales amount')
	date = DateTimeField(u'Date', format='%d/%m/%Y', validators = [Required()])