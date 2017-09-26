import os
import sys
import json
from requests.auth import HTTPBasicAuth
import hashlib
import json
import hmac
import requests
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        #if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
        if not request.args.get("hub.verify_token") == "hello123":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print data
    return "ok", 200


if __name__ == '__main__':
    app.run(debug=True)