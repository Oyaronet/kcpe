from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, UserLoginForm, AdminLoginForm
# from database import users, engine, meta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, select, update, delete, and_, or_

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "718318cf14f5c2c3568b7bb620e6cc32"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://epmswlywsgfgec:a471edc1aa9d0338b9cb4de98802af9a10189f6a576b1311fa17300dbc26bf7a@ec2-44-194-92-192.compute-1.amazonaws.com:5432/deramp098sjfju"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.db"



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        """ string representation of the user table """
        return f'User({self.username}, {self.email})'

 
@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            """ send user data to the database """
            db.create_all()
            user = User(username=form.username.data, \
                  email=form.email.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Account created successfully for {form.username.data}!\
                    Please log in to continue!', 'success')
            return redirect(url_for('user_login'))
        except:
            flash(f'User by that email already exist in the system! Try Logging in instead', 'danger')
            return redirect(url_for('register'))
    return render_template('register.html', form=form)


@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    form = UserLoginForm()
    if form.validate_on_submit():
        """ Log in User with Correct Credentials """ 
        user = User.query.filter(and_(
            User.email == form.email.data,
            User.password == form.password.data
        )).first()
        if user:
            return render_template('userdashboard.html', user=user)
        else:
            flash('Failed to Log you in! Please check your email \
                  and password and try logging in again!', 'danger')
            return redirect(url_for('user_login'))
    return render_template('user_login.html', form=form)


@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@gmail.com' and \
        form.password.data == 'miami':
            data = select([users])
            data = engine.connect().execute(data).fetchall()
            return render_template('admindashboard.html', data= data)
        else:
            flash(f'Failed to Log in! Check your email or \
            password and then try again!', 'danger')
            return redirect(url_for('admin_login'))
    return render_template('admin_login.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)