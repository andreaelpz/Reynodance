from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/events")
def events():
  return render_template("events.html")

@app.route("/logIn")
def login():
  return render_template("logIn.html")

@app.route("/register")
def register():
  return render_template("register.html")

if __name__ == "__main__":
  app.run()