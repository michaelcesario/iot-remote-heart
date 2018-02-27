from flask import Flask, jsonify
from flask import request
from db import DatabaseConnection

c = DatabaseConnection.getDBCursor()

app = Flask(__name__)

@app.route('/')
def pollNewMessage():
    dbConnection = DatabaseConnection.getDBCursor()
    cursor = dbConnection.cursor()

    query = "select * from messages order by date desc"
    cursor.execute(query,)
    result = cursor.fetchone()
    dbConnection.close()

    if result:
        message = result[0]
        duration = result[1]
        date = result[2]
        return jsonify({"message": message}), 200
    else:
        return jsonify({"error": "no message"}), 400


@app.route('/post-message', methods=['GET', 'POST'])
def postMessage():
    if request.method == 'POST':
        message = request.form['message']
        duration = request.form['duration']


if __name__ == "__main__":
    app.run()
