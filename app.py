from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("timeline_dots.html")


@app.route("/choropleth")
def choro():
    return render_template("choropleth.html")


if __name__ == "__main__":
    app.run(debug=True)
