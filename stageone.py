from flask import Flask,request,jsonify
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/api", methods=['GET'])
def home():

    slack_name = request.args.get('slack_name')
    track_name = request.args.get('track')
    day = datetime.now(pytz.utc).strftime('%A')
    time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    git_file = 'https://github.com/Alonge9500/HNGINTERN/blob/main/stageone.py'
    git_repo = 'https://github.com/Alonge9500/HNGINTERN'

    response = {
        "slack_name":slack_name,
        "current_day":day,
        "utc_time":time,
        "track":track_name,
        "github_file_url":git_file,
        "github_repo_url":git_repo,
        "status_code":200

    }

    return jsonify(response)





