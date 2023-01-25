from flask import Flask, render_template


app = Flask(__name__)


menu = ["Install", "First applicatoin", "Feed back"]


@app.route("/")
def index():
    return render_template('index.html', title = "About flask", menu = menu )


@app.route("/about")
def about():
    return render_template('about_site.html',title  = "About a site")

if __name__ == "__main__":
    app.run(debug=True)