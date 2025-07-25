##'/api/v1/details'
##'/api/v1/health'

from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        "message": 'Hello World',
        'time': datetime.datetime.now(),
        'hostname': socket.gethostname()
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        "status": 'Healthy'
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")