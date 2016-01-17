from flask import Flask, render_template, request

import json

import random


application = Flask(__name__, static_folder="static")
application.config['DEBUG'] = True

MESSAGES = ["test halay"]


@application.route("/")
def api_root():
    return render_template("index.html")

@application.route("/messages", methods=["GET", "POST"])
def api_messages():
    print("/messages hit", request.method)
    if request.method == "GET":
        return json.dumps({i: {"text": MESSAGES[i]} for i in range(len(MESSAGES))})

    if "post_message" in request.values:
        messages = request.values["post_message"]
        msg = "".join(messages)
        MESSAGES.append(msg)

    return api_root()

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
