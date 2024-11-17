from flask import Flask, render_template, request, jsonify
from dataPreprocessing import process_text
from matchMatrix import create_match_matrix
from pairGeneration import generate_pairs
import openai
import os

app = Flask(__name__)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("API Key is not set. Please set the OPENAI_API_KEY environment variable.")

openai.api_key = api_key

# Route for the dashboard (homepage)
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/index')
def index():
    return render_template('index.html')

# Route for processing the text and showing results (AJAX)
@app.route('/process', methods=['POST'])
def process_text_input():

    input_text = request.form.get('text_data', '')

    para1, para2 = process_text(input_text)

    match_matrix = create_match_matrix(para1, para2)

    pairs = generate_pairs(match_matrix, para1, para2)

    return jsonify(pairs=pairs)

if __name__ == '__main__':
    app.run(debug=True)
