from flask import Flask, render_template, request

import json

import random


application = Flask(__name__, static_folder="static")
application.config['DEBUG'] = True


@application.route("/")
def api_root():
    return render_template("box.html")


@application.route("/bh-validate", methods=["POST"])
def api_behappy():
    data = request.get_json()
    messages = data["messages"]
    valid = list()
    for msg in messages:
        valid.append(is_insult(msg))
    return json.dumps({"messages": valid})


@application.route("/behappy-form", methods=["POST"])
def next_page():
    return render_template("success.html")


def is_insult(message):
    return random.random() > 0.5


if __name__ == "__main__":
    application.run(debug=True)
