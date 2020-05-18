from flask import Flask, redirect, url_for
import routes
from helpers.reverse_proxied import ReverseProxied


app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(routes.oauth, url_prefix="/oauth")
app.register_blueprint(routes.init, url_prefix="/init")
app.register_blueprint(routes.webhooks, url_prefix="/webhooks")
app.register_blueprint(routes.events, url_prefix="/events")


@app.route("/")
def init():
    return redirect(url_for("init.readme"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)