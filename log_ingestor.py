# log_ingestor.py
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://username:password@localhost:27017/database_name'    ##MongoDB Connection string
mongo = PyMongo(app)

@app.route('/ingest', methods=['POST'])
def ingest_log():
    log_data = request.get_json()
    # Convert timestamp to datetime object
    log_data['timestamp'] = datetime.fromisoformat(log_data['timestamp'])
    mongo.db.logs.insert_one(log_data)
    return 'Log ingested successfully.', 200

if __name__ == '__main__':
    app.run(port=3000)
