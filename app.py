from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/paraphrase', methods=['POST'])
def paraphrase():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    # Dummy paraphrase function (to be replaced with actual implementation)
    paraphrased_text = text[::-1]  # Reversing text as a placeholder
    
    return jsonify({"original": text, "paraphrased": paraphrased_text})

if __name__ == '__main__':
    app.run(debug=True)
