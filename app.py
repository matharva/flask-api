from time import sleep
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from flask import Flask
# import requests


# Patch the requests module to enable automatic instrumentation
# patcher.patch(('requests',))

app = Flask(__name__)
# app.config['DEBUG'] = True


# Configure the X-Ray recorder to generate segments with our service name
xray_recorder.configure(service='Local Server')

# Instrument the Flask application
XRayMiddleware(app, xray_recorder)
xray_recorder.configure(context_missing='LOG_ERROR')


@ app.route('/')
def hello_world():
    return {"data": "Server is running"}


@app.route("/test")
def call_ec2():

    # EC2_URL = "http://13.234.29.198:5000/"

    # Start a segment
    # segment = xray_recorder.begin_segment('ec2 segment')

    # Start a subsegment
    xray_recorder.begin_subsegment('Sleep subsegment')

    # Add metadata and annotations
    # segment.put_metadata('key', dict, 'namespace')
    # subsegment.put_annotation('key', 'value')
    sleep(1)
    xray_recorder.end_subsegment()

    # xray_recorder.begin_subsegment('GET REQ subsegment')
    # # response = requests.get(EC2_URL)
    # xray_recorder.end_subsegment()

    # Close the subsegment and segment
    # xray_recorder.end_segment()
    return {"data": "Test end point"}


if __name__ == "__main__":
    app.run(debug=True, port=8443)
