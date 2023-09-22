
from flask import jsonify
from flask import Flask,request
from flask_cors import CORS




app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
	return "Hello World!"

@app.route('/data', methods=['GET'])
def data():
 x ={
     "name ":"John",
     "age":5
    }
 return jsonify(x)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)