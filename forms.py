from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (
    StringField, PasswordField, TextAreaField,
    SubmitField, BooleanField, SelectField
)
from wtforms.validators import (
    DataRequired, Email, Length,
    EqualTo, Regexp
)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(2, 20)])
    email = StringField('Email', validators=[DataRequired(), Email()])

    gender = SelectField(
        'Gender',
        choices=[('Male','Male'), ('Female','Female'), ('Other','Other')],
        validators=[DataRequired()]
    )

    college_id = StringField(
        'College ID',
        validators=[DataRequired(), Regexp(r'^\d{7}$')]
    )

    college = SelectField(
        'College',
        choices=[('VIT Bibewadi', 'VIT Bibewadi')],
        validators=[DataRequired()]
    )

    branch = SelectField(
        'Branch',
        choices=[
            ('CSE','CSE'), ('IT','IT'), ('AI','AI'),
            ('AIDS','AIDS'), ('AIML','AIML'),
            ('ENTC','ENTC'), ('Mechanical','Mechanical')
        ],
        validators=[DataRequired()]
    )

    city = StringField('City', validators=[DataRequired()])

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8),
            Regexp(
                r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%#?&]).{8,}$',
                message='Password must contain  at least ;1 letter, 1 number & 1 special character'
            )
        ]
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password')]
    )

    submit = SubmitField('Register')



class GlobalChatForm(FlaskForm):
    message = TextAreaField(
        'Message',
        validators=[DataRequired(), Length(min=1, max=500)]
    )
    submit = SubmitField('Send')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateProfileForm(FlaskForm):
    picture = FileField(
        'Update Profile Picture',
        validators=[FileAllowed(['jpg', 'jpeg', 'png'])]
    )

    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=2, max=20)]
    )

    college = SelectField(
        'College',
        choices=[('VIT Bibewadi', 'VIT Bibewadi')],
        validators=[DataRequired()]
    )

    branch = SelectField(
        'Branch',
        choices=[
            ('CSE','CSE'), ('AI','AI'),('IT','IT'),
            ('AIDS','AIDS'), ('AIML','AIML'),
            ('ENTC','ENTC'), ('Mechanical','Mechanical')
        ],
        validators=[DataRequired()]
    )

    city = StringField('City', validators=[DataRequired()])

    gender = SelectField(
        'Gender',
        choices=[('Male','Male'), ('Female','Female'), ('Other','Other')],
        validators=[DataRequired()]
    )

    submit = SubmitField('Update Profile')


class UpdateEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update Email')



class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField(
        'New Password',
        validators=[DataRequired(), Length(min=8)]
    )
    confirm_password = PasswordField(
        'Confirm New Password',
        validators=[DataRequired(), EqualTo('new_password')]
    )
    submit = SubmitField('Change Password')