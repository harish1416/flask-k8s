from flask import Flask, request, jsonify
import psycopg2
import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins

conn = psycopg2.connect(
    host=os.environ.get("DB_HOST", "localhost"),
    dbname="postgres",
    user="postgres",
    password="password"
)

@app.route('/texts')
def get_texts():
    cur = conn.cursor()
    cur.execute("SELECT * FROM text")
    rows = cur.fetchall()
    cur.close()
    return jsonify([{'id': r[0], 'text': r[1]} for r in rows])

@app.route('/add', methods=['POST'])
def add_text():
    data = request.json
    cur = conn.cursor()
    cur.execute("INSERT INTO text (text) VALUES (%s) ON CONFLICT DO NOTHING", (data['text'],))
    conn.commit()
    cur.close()
    return '', 204

@app.route('/delete', methods=['DELETE'])
def delete_texts():
    cur = conn.cursor()
    cur.execute("DELETE FROM text")
    conn.commit()
    cur.close()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0')
