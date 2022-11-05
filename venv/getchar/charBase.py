from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("ind1.html")

__name__ = "__main__";
app.run(debug=True)