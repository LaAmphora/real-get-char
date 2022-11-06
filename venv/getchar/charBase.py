from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(days=3)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    pawprint = db.Column(db.String(100))
    gender = db.Column(db.String(3))
    time = db.Column(db.Integer)

    def __init__(self, name, age, pawprint, gender, time):
        self.name = name
        self.age = age
        self.pawprint = pawprint
        self.gender = gender
        self.time = time


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        name = request.form["nm"]
        """
        age = request.form["yr"]
        pawprint = request.form["pp"]
        gender = request.form["gn"]
        time = request.form["tm"]
        """
        session["user"] = user
        
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["age"] = found_user.age
            session["pawprint"] = found_user.pawprint
            session["gender"] = found_user.gender
            session["time"] = found_user.time
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()
            
        flash("Login successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        
        return render_template("login.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    pawprint = None
    if "user" in session:
        user = session["user"]
        
        if request.method == "POST":
            pawprint = request.form["pawprint"]
            session["pawprint"] = pawprint
            found_user = users.query.filter_by(name=user).first()
            found_user.pawprint = pawprint
            db.session.commit()
            flash("Pawprint was saved!")
        else:
            if "pawprint" in session:
                pawprint = session["pawprint"]
            
        return render_template("user.html", pawprint=pawprint)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("Log out successful!", "info")
    session.pop("user", None)
    session.pop("pawprint", None)
    return redirect(url_for("login"))

with app.app_context():
    if __name__ == '__main__':
        db.create_all()
        app.run(debug=True)