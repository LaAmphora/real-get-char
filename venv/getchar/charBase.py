from flask import Flask, request, render_template
 
app = Flask(__name__)

@app.route('/paw', methods =["GET", "POST"])
def pawprint():
    if request.method == "POST":
       pawprint = request.form.get("pp")
       return pawprint + " successfully logged in."
    return render_template("login.html")
 

@app.route('/')      
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)