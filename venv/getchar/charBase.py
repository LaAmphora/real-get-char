from flask import Flask, request, render_template, flash, redirect
 
app = Flask(__name__)
app.secret_key = "topsecretkey"

class Driver():
    def __init__(self, paw, name, age, gender, start, end, loc, phone, cmodel, cmake, clicense):
        self.paw = paw
        self.name = name
        self.age = age
        self.gender = gender
        self.start = start
        self.end = end
        self.loc = loc
        self.phone = phone
        self.cmake = cmake
        self.cmodel = cmodel
        self.clicense = clicense
        
john = Driver('jcw24', 'John', 20, 'M', 20, 0, '101 Main St', 314-449-3602, 'Nissan', 'Sentra', 'ABC123')
sarah = Driver('ssh33', 'Sarah', 19, 'F', 21, 1, 'Sigma Nu', 404-425-4583, 'Honda', 'Civic', '123ABC')
alex = Driver('ajp96', 'Alex', 22, 'NB', 22, 0, 'Gillett', 314-797-9085, 'Porsche', 'Cayenne', '1A2B3C')
cameron = Driver('cap39', 'Cameron', 20, 'M', 19, 0, 'downtown Columbia', 423-255-2728, 'Subaru', 'Outback', '321CBA')
abby = Driver('als72', 'Abby', 18, 'F', 23, 3, 'Lafferre Hall', 573-701-5455, 'GMC', 'Sierra', 'A1B2C3')

drivers = [john, sarah, alex, cameron, abby]

@app.route('/confirm')
def confirm():
    return render_template("confirm.html")


@app.route('/check/<user>', methods=["GET","POST"])
def check(user):
    for drive in drivers:
        if user == (drive.name):
            usr = drive
            return render_template("check.html", name = usr.name, age = usr.age, gender = usr.gender, start = usr.start, end = usr.end, loc = usr.loc)
    return render_template("view.html", drivers = drivers)


@app.route('/view', methods=["GET", "POST"])
def view():
    return render_template("view.html", drivers = drivers)


@app.route('/login', methods =["GET", "POST"])
def login():
    if request.method == "POST":
       pawprint = request.form.get("pp")
       flash(pawprint + " is successfully logged in")
       return redirect('/view')
    return render_template("login.html")
 

@app.route('/')      
def base():
    return render_template("NEWbase.html")


if __name__ == "__main__":
    app.run(debug=True)