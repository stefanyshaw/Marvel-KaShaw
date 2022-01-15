try:
    import requests
    import pendulum
    import hashlib
    from model.key import public_key, private_key
    from model.api import get_character
    from flask import Flask, render_template, request
except ImportError as err:
    print(f"Failed to import required packages: {err}")




app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["search"]
        data = get_character(public_key, private_key, name)
        return render_template("index.html", data=data)

    return render_template("index.html")


if __name__ == '__main__':
    app.run()
