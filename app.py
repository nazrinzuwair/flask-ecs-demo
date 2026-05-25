from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'region':  os.getenv('AWS_DEFAULT_REGION', 'unknown')
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


