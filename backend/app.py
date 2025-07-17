# backend/app.py
from flask import Flask, request, jsonify, render_template_string
import json
from datetime import datetime
import uuid
import os

app = Flask(__name__)
DB_FILE = "db.json"

def load_reports():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_reports(reports):
    with open(DB_FILE, "w") as f:
        json.dump(reports, f, indent=4)
        f.flush()
        os.fsync(f.fileno())

@app.route("/report", methods=["POST"])
def report():
    data = request.json
    data["id"] = str(uuid.uuid4())
    data["timestamp"] = datetime.now().isoformat()

    reports = load_reports()
    data["report_id"] = max((r.get("report_id", 0) for r in reports), default=0) + 1

    reports.append(data)
    save_reports(reports)

    return jsonify({
        "status": "success",
        "report_id": data["report_id"],
        "uuid": data["id"]
    }), 201

@app.route("/reports")
def get_reports_json():
    reports = load_reports()
    response = jsonify(reports)
    response.headers["Cache-Control"] = "no-store"
    return response

@app.route("/reports/browser")
def get_reports_html():
    reports = load_reports()
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <meta http-equiv="refresh" content="10">
        <title>Live Reports</title>
        <style>
            body {
                background: #121212;
                color: #e0e0e0;
                font-family: Arial, sans-serif;
                padding: 20px;
            }
            pre {
                background: #1e1e1e;
                color: #bb86fc;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
            }
            .header {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .last-updated {
                color: #888;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Current Reports</h1>
            <div class="last-updated" id="lastUpdated"></div>
        </div>
        <pre>{{ reports|tojson(indent=4) }}</pre>
        <script>
            document.getElementById('lastUpdated').textContent = 'Last updated: ' + new Date().toLocaleTimeString();
            document.title = 'Reports @ ' + new Date().toLocaleTimeString();
        </script>
    </body>
    </html>
    """, reports=reports)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
