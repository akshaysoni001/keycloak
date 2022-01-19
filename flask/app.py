from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/login')
def login():
    return jsonify({'Message':'Logged In'})



@app.route('/django')
def django():
    return jsonify({'Message': 'Welcome to Django'})



if __name__ == '__main__':
    app.run(debug=True)