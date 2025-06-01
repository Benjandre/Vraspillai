from flask import Flask, render_template, redirect

# Remember to specify where both the template and the static folder is.
app = Flask(__name__, template_folder="Frontend/templates", static_folder="Frontend/static")

@app.route("/")
def Home_Redirect():
    return redirect("/home")


# This shows the landing page.
@app.route("/home")
def Home():
    return render_template("Home.html")

# This shows the work page.
@app.route("/work")
def Work():
    return render_template("Work.html")

# This shows the about page.
@app.route("/about")
def About():
    return render_template("About.html")

# This shows the contact page.
@app.route("/contact")
def Contact():
    return render_template("Contact.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
