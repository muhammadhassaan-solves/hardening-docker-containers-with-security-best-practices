# Python Flask app with read-only file system
from flask import Flask, request, jsonify
import os, tempfile

app = Flask(__name__)

@app.route('/')
def hello():
    return f"Hello from read-only container! Running as user: {os.getuid()}"

@app.route('/write-test', methods=['POST'])
def write_test():
    try:
        with tempfile.NamedTemporaryFile(mode='w', delete=False, dir='/tmp') as f:
            f.write("Temporary data")
            temp_file = f.name
        return jsonify({"status": "success", "message": f"Successfully wrote to {temp_file}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/illegal-write', methods=['POST'])
def illegal_write():
    try:
        with open('/app/illegal_file.txt', 'w') as f:
            f.write("This should not work")
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
