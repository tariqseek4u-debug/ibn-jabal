from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """Home page"""
    return jsonify({
        'message': 'Welcome to Ibn Jabal HTTP Library Web App',
        'status': 'running'
    })

@app.route('/api/test', methods=['GET', 'POST'])
def test_api():
    """Test API endpoint"""
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({
            'received': data,
            'status': 'success'
        })
    return jsonify({
        'message': 'Send POST request with JSON data'
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True)
