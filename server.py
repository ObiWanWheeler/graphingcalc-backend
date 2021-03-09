from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(response={'status': 'success 200', 'data':'lovely'})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)