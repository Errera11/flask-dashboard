from flask import url_for, redirect, render_template, flash, g, session
from flask_login import login_user, logout_user, current_user, login_required
from app import app, lm, db
from app.forms import ExampleForm, LoginForm, SaleForm
from app.models import User, Sales


@app.route('/')
def index():
    sales = Sales.query.all()

    # Define Plot Data
    labels = [sale.date for sale in sales]
    data = [sale.total_amount for sale in sales]

    # Return the components to the HTML template
    return render_template(
        template_name_or_list='index.html',
        data=data,
        labels=labels,
    )


@app.route('/new/')
def new():
	form = SaleForm()
	return render_template('new.html', form=form)


@app.route('/save/', methods = ['GET','POST'])
def save():
    form = SaleForm()

    if form.validate_on_submit():
        sales = form.total_amount.data
        date = form.date.data
        new_sale = Sales(date=date, total_amount=sales)

        db.session.add(new_sale)
        db.session.commit()

        form.total_amount.data = ""
        form.date.data = ""
        flash('Sale created successfully!', 'success')
    return render_template('new.html', form=form)

@app.route('/view/<id>/')
def view(id):
	return render_template('view.html')

# === User login methods ===

@app.before_request
def before_request():
    g.user = current_user

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login/', methods = ['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        login_user(g.user)

    return render_template('login.html', 
        title = 'Sign In',
        form = form)

@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))

# ====================
