# server.py

from flask import Flask, request
import json
from aws_lambda import lambda_handler

app = Flask(__name__)

@app.route('/Keygen38', methods=['POST'])
def generate_keys():
    request_body = request.get_json()
    event = {"body": json.dumps(request_body)}

    handler_response = lambda_handler(event, context=None)

    response = app.response_class(
        response=handler_response['body'],
        status=handler_response['statusCode'],
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    # app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)