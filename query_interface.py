# query_interface.py
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from flask_socketio import SocketIO
from datetime import datetime
import re

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://username:password@localhost:27017/database_name'    ##MongoDB Connection string
mongo = PyMongo(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query_logs():
    query_params = {}
    # Iterate over form fields
    for param in ['level', 'message', 'resourceId', 'timestamp', 'traceId', 'spanId', 'commit',
                  'metadata.parentResourceId']:
        value = request.form.get(param)
        if value:
            value = re.compile(value, re.IGNORECASE)
            query_params[param] = value

    # Process time range
    start_timestamp = request.form.get('startTimestamp')
    end_timestamp = request.form.get('endTimestamp')


    if start_timestamp and end_timestamp:
        try:
            start_datetime = datetime.strptime(start_timestamp, '%Y-%m-%dT%H:%M:%S.%f')
            end_datetime = datetime.strptime(end_timestamp, '%Y-%m-%dT%H:%M:%S.%f')
            query_params['timestamp'] = {'$gte': start_datetime, '$lte': end_datetime}
        except ValueError as e:
            print(f"Error parsing timestamps: {e}")

    logs = mongo.db.logs.find(query_params, {'_id': 0})

    formatted_logs = []
    for log in logs:
        log['timestamp'] = log['timestamp'].strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]  # Format timestamp
        formatted_logs.append(log)

    return render_template('index.html', logs=formatted_logs)

if __name__ == '__main__':
    socketio.run(app, port=3001, allow_unsafe_werkzeug=True)