#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/userSimilarity/<string:user_id>', methods=['GET'])
def get_similar(user_id):
    if len(user_id) == 0:
        abort(404)
    return user_id

if __name__ == '__main__':
    app.run(debug=True)
