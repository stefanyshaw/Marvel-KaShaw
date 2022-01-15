from flask import Flask, render_template
from flask_fontawesome import FontAwesome
#from flask_bootstrap import Bootstrap
#from service.marvel import get_hero
from model.marvel import busca_herois

app = Flask(__name__)
fa = FontAwesome(app)
#bootstrap = Bootstrap(app)

@app.route("/")
def index():
    lista_herois = busca_herois()
    return render_template('index.html', lista_herois)

if __name__ == '__main__':
    app.run()