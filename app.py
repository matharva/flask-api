# Import the X-Ray modules
# from aws_xray_sdk.ext.flask.middle
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from flask import Flask, request, jsonify


# Patch the requests module to enable automatic instrumentation
patcher.patch(('requests',))

app = Flask(__name__)

# Configure the X-Ray recorder to generate segments with our service name
xray_recorder.configure(service='My First Serverless App')

# Instrument the Flask application
XRayMiddleware(app, xray_recorder)


@ app.route('/')
def hello_world():
    return {"data": "Server is running"}


@ app.route('/post', methods=["POST"])
def testpost():
    input_json = request.get_json(force=True)
    dictToReturn = {'text': input_json['text']}
    return jsonify(dictToReturn)
