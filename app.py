#!/usr/bin/env python

from flask import Flask, jsonify
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
        'SERVICE_NAME': 'test-flask',
        'DEBUG': True
}

apm = ElasticAPM(app)

@app.route("/")
def index():
    return jsonify({"test" : "ok"})

@app.route("/error")
def error():
    try:
        1 / 0
    except ZeroDivisionError:
        app.logger.error("error", exc_info=True)
        return jsonify({"status" : "error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
