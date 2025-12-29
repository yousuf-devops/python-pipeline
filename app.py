from flask import Flask, jsonify, render_template_string
import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask CI/CD Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 { margin-top: 0; }
        .info { 
            background: rgba(255, 255, 255, 0.2);
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
        }
        .version {
            font-size: 24px;
            font-weight: bold;
            color: #ffd700;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Flask CI/CD Pipeline Demo</h1>
        <div class="info">
            <p><strong>Status:</strong> Application is running successfully!</p>
            <p><strong>Version:</strong> <span class="version">2.0</span></p>
            <p><strong>Server Time:</strong> {{ current_time }}</p>
            <p><strong>Deployment:</strong> Automated via GitHub Actions</p>
        </div>
        <h2>✅ Pipeline Features:</h2>
        <ul>
            <li>Automatic deployment on git push</li>
            <li>Zero-downtime updates</li>
            <li>Runs on AWS EC2</li>
            <li>Production-ready setup</li>
        </ul>
        <p><em>Make a change to this file and push to see the magic!Build by Shahzaib.!! ✨</em></p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML_TEMPLATE, current_time=current_time)

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "2.0"
    })

@app.route('/api/info')
def info():
    return jsonify({
        "app": "Flask CI/CD Demo",
        "version": "2.0",
        "description": "Automated deployment pipeline demo"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
