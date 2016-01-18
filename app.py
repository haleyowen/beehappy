import json

from flask import Flask, render_template, request

from models import FeatureDetector, read_solutions

application = Flask(__name__, static_folder="static")
application.config['DEBUG'] = True


MESSAGES = ["test"]
GRADER = read_solutions()
FEATURE_DETECTOR = FeatureDetector()


@application.route("/")
def api_root():
    return render_template("index.html")


@application.route("/messages", methods=["GET", "POST"])
def api_messages():
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

    return json.dumps({"messages": list(valid)})


def is_insult(message):
    feature_vector = FEATURE_DETECTOR.vector(message)
    prediction = GRADER.predict(feature_vector)
    return bool(prediction[0])


if __name__ == "__main__":
    application.run(debug=True)
