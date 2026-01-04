import os
import secrets
from datetime import datetime

from PIL import Image
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager, UserMixin,
    login_user, logout_user,
    login_required, current_user
)
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

from forms import (
    RegistrationForm, LoginForm,
    UpdateProfileForm,
    UpdateEmailForm,
    ChangePasswordForm,
    GlobalChatForm
)

# ================= APP CONFIG =================
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# ================= MODELS =================
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    college_id = db.Column(db.String(7), unique=True, nullable=False)
    college = db.Column(db.String(50), nullable=False)
    branch = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default_other.png')


class GlobalMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='global_messages')


class Mess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    images = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    google_map_link = db.Column(db.String(300), nullable=False)
    contact = db.Column(db.String(50), nullable=False)


class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    category = db.Column(db.String(10), nullable=False)  # boys / girls
    description = db.Column(db.Text, nullable=False)
    images = db.Column(db.String(300), nullable=True)
    address = db.Column(db.String(200), nullable=False)
    google_map_link = db.Column(db.String(300), nullable=False)
    contact = db.Column(db.String(50), nullable=True)


# ⭐ NEW: Seed status (IMPORTANT)
class SeedStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seeded = db.Column(db.Boolean, default=False)


# ================= LOGIN =================
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ================= UTILITIES =================
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    img = Image.open(form_picture)
    img.thumbnail((150, 150))
    img.save(picture_path)

    return picture_fn


# ================= ROUTES =================
@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


# ================= PROFILE =================
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    profile_form = UpdateProfileForm()
    email_form = UpdateEmailForm()
    password_form = ChangePasswordForm()

    if profile_form.validate_on_submit():
        if profile_form.picture.data:
            picture_file = save_picture(profile_form.picture.data)
            current_user.image_file = picture_file

        current_user.username = profile_form.username.data
        current_user.city = profile_form.city.data

        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('profile'))

    elif request.method == 'GET':
        profile_form.username.data = current_user.username
        profile_form.city.data = current_user.city

    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)

    return render_template(
        'profile.html',
        profile_form=profile_form,
        email_form=email_form,
        password_form=password_form,
        image_file=image_file
    )


# ---------- GLOBAL CHAT ----------
@app.route('/global-chat', methods=['GET', 'POST'])
@login_required
def global_chat():
    form = GlobalChatForm()

    if form.validate_on_submit():
        msg = GlobalMessage(
            content=form.message.data,
            user_id=current_user.id
        )
        db.session.add(msg)
        db.session.commit()
        return redirect(url_for('global_chat'))

    messages = GlobalMessage.query.order_by(GlobalMessage.timestamp.asc()).all()
    return render_template('global_chat.html', form=form, messages=messages)


@app.route('/delete-message/<int:message_id>', methods=['POST'])
@login_required
def delete_message(message_id):
    message = GlobalMessage.query.get_or_404(message_id)

    if message.user_id != current_user.id:
        flash('You are not allowed to delete this message.', 'danger')
        return redirect(url_for('global_chat'))

    db.session.delete(message)
    db.session.commit()
    flash('Message deleted.', 'success')
    return redirect(url_for('global_chat'))


# ---------- HOSTEL / MESS ----------
@app.route("/Hostel_PG")
def hostel_pg():
    return render_template('hostel_pg.html')


@app.route("/Mess_Near_College")
def mess_near_college():
    messes = Mess.query.all()
    return render_template('mess_near_college.html', messes=messes)


@app.route("/hostel-pg/boys")
def boys_hostel_pg():
    hostels = Hostel.query.filter_by(category="boys").all()
    return render_template("boys_hostel_pg.html", hostels=hostels)


@app.route("/hostel-pg/girls")
def girls_hostel_pg():
    hostels = Hostel.query.filter_by(category="girls").all()
    return render_template("girls_hostel_pg.html", hostels=hostels)


# ---------- AUTH ----------
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode('utf-8')

        image_file = (
            'default_male.png' if form.gender.data == 'Male'
            else 'default_female.png' if form.gender.data == 'Female'
            else 'default_other.png'
        )

        user = User(
            username=form.username.data,
            email=form.email.data,
            college_id=form.college_id.data,
            college=form.college.data,
            branch=form.branch.data,
            city=form.city.data,
            password=hashed_password,
            gender=form.gender.data,
            image_file=image_file
        )

        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            flash('User already exists.', 'danger')
            return redirect(url_for('register'))

        flash('Account created successfully!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))

        flash('Login unsuccessful.', 'danger')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
def seed_if_empty():
    from seed import seed_mess, seed_girls_hostels, seed_boys_hostels

    if Mess.query.first() is None:
        seed_mess()
        print("✅ Mess seeded")

    if Hostel.query.first() is None:
        seed_girls_hostels()
        seed_boys_hostels()
        print("✅ Hostels seeded")


with app.app_context():
    db.create_all()
    seed_if_empty()

if __name__ == '__main__':
    app.run()




