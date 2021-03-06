from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[validators.Email()])
    password = PasswordField(label='Password', validators=[validators.Length(min=8)])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = "H3t@1512"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        entered_email = login_form.email.data
        entered_pass = login_form.password.data
        if entered_email == "admin@email.com" and entered_pass == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
