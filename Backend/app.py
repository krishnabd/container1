from flask import Flask

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    return {'data': 'This is data from the backend microservice'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
