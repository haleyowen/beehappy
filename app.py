from flask import Flask, render_template, request

import json

import random


application = Flask(__name__, static_folder="static")
application.config['DEBUG'] = True

messages = ["test halay"]


@application.route("/")
def api_root():
    return render_template("index.html")

@application.route("/messages", methods=["GET"])
def api_get_messages():
    global messages
    return json.dumps(messages)
  

@application.route("/bh-validate", methods=["POST"])
def api_behappy():
    messages = list()
    valid = list()

    if "messageList" in request.get_json():
        messages = request.get_json()["messageList"]
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
