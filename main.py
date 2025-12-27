from flask import Flask, render_template, request, jsonify
from core.dataPreprocessing import process_text
from core.matchMatrix import create_match_matrix
from core.pairGeneration import generate_pairs
from core.sample import summarize_paragraphs

app = Flask(__name__)

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
    
    summarized_pairs = summarize_paragraphs(pairs)

    return jsonify(pairs=summarized_pairs)

if __name__ == '__main__':
    app.run(debug=True)
