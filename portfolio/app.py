import argparse
import datetime
from flask import (
    Flask,
    render_template,
    request
)

import utils


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/_cowsay")
def make_cowsay_request():
    showerthought = utils.get_random_showerthought_from_file()
    cowsay = utils.get_cowsay_message(showerthought)
    return cowsay

@app.route("/_update_showerthoughts", methods=["POST"])
def update_showerthoughts():
    # Only fetch new thoughts if request came from Cron:
    if "X-Appengine-Cron" in request.headers:
        utils.fetch_showerthoughts()

    return ("", 204)  # No Content


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    app.run(debug=args.debug)