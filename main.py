from flask import Flask, render_template, request, jsonify
from dataPreprocessing import process_text
from matchMatrix import create_match_matrix
from pairGeneration import generate_pairs

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
    # Collect text data from the form input
    input_text = request.form.get('text_data', '')

    # Step 1: Process the input text to generate two paragraphs (para1, para2)
    para1, para2 = process_text(input_text)

    # Step 2: Create the match matrix based on noun overlap between sentences
    match_matrix = create_match_matrix(para1, para2)

    # Step 3: Generate the sentence pairs
    pairs = generate_pairs(match_matrix, para1, para2)

    # Step 4: Return the pairs as a JSON response for AJAX to handle
    return jsonify(pairs=pairs)

if __name__ == '__main__':
    app.run(debug=True)
