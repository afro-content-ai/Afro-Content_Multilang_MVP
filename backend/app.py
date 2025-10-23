from flask import Flask, request, jsonify
from flask_cors import CORS
from main_multilang import generate_multilang_text
from main_multilang_reel import create_video_reel

app = Flask(__name__)
CORS(app)  # allow frontend access

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt')
    result = generate_multilang_text(prompt)
    return jsonify(result)

@app.route('/reel', methods=['POST'])
def reel():
    data = request.json
    lang = data.get('lang', 'en')
    text = data.get('text', '')
    path = create_video_reel(text, lang)
    return jsonify({'video_path': path})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
