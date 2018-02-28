from flask import Flask, jsonify
from flask import request
from db import DatabaseConnection

#c = DatabaseConnection.getDBCursor()

app = Flask(__name__)

@app.route('/')
def pollNewMessage():
    dbConnection = DatabaseConnection.getDBCursor()
    cursor = dbConnection.cursor()

    query = "select * from alerts order by id desc"
    cursor.execute(query,)
    result = cursor.fetchone()

    dbConnection.close()

    if result:
        message = result[0]
        duration = result[1]
        valid = result[2]
        _id = result[3]

        if valid == 1:
            return jsonify({"message": message, "duration": duration, "id": _id}), 200
        else:
            return jsonify({}), 202

    else:
        return jsonify({}), 202


@app.route('/new-alert', methods=['POST'])
def addNewAlert():
    if request.method == 'POST':
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        message = request.form['message']
        duration = request.form['duration']

        query = "insert into alerts values (%s, %s, 1)"
        cursor.execute(query, (message, duration))

        dbConnection.commit()
        dbConnection.close()
        return jsonify({}), 201


@app.route('/invalidate-alert', methods=['POST'])
def invalidateAlert():
    if request.method == 'POST':
        dbConnection = DatabaseConnection.getDBCursor()
        cursor = dbConnection.cursor()

        _id = request.form['id']

        print("invalidating alert with id")
        print(_id)

        query = "update alerts set valid = 0 where id = %s"
        cursor.execute(query, (_id,))

        dbConnection.commit()
        dbConnection.close()
        return jsonify({}), 201

if __name__ == "__main__":
    app.run()
