from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route("/")
def survey():
    return render_template("index.html")

@app.route("/survey",methods=["POST"])
def results():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect("/results")

@app.route("/results")
def results1():
    return render_template("results.html")

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True) 