from flask import Flask
from os import getenv
app = Flask(__name__)

@app.route('/')
def hello_world():
    review_test = getenv("REVIEW_TEST", "env doesn't work")
    return {"message": f"I sent: {review_test}."}


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5003)