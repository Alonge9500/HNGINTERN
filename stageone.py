from flask import Flask,request,jsonify
from datetime import datetime
import pytz

app = Flask(__name__)


@app.route("/api", methods=['GET'])
def home():
    
    slack_name = request.args.get('slack_name')
    track_name = request.args.get('track_name')
    day = datetime.now(pytz.utc).strftime('%A')
    time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    git_file = 'sscvncvs'
    git_repo = 'ksscvncvs'
    
    response = {
        "slack_name":slack_name,
        "Current_day":day,
        "utc_time":time,
        "track":track_name,
        "github_file_url":git_file,
        "github_repo_url":git_repo,
        "status_code":200
        
    }
    
    return jsonify(response)
    
    
    
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
    
    