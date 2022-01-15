from flask import Flask, render_template
from flask_fontawesome import FontAwesome
from flask_bootstrap import Bootstrap

app = Flask(__name__)
fa = FontAwesome(app)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ = '__main__':
    app.run()