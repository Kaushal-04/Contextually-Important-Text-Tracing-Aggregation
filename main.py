from flask import Flask, render_template, request, jsonify
from dataCollection import dataCollect

from dataPreprocessing import cleanText
from ner import extract_entities
from vectorize import vectorize_text
from aggregate import aggregate_entities
from plot import plot_aggregated_entities

app = Flask(__name__)

# Route for the dashboard (homepage)
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Route for the index page
@app.route('/index')
def index():
    return render_template('index.html')  # Render the index HTML

# Route for processing the text and returning results
@app.route('/process', methods=['POST'])
def process_text():
    # Collect text data (you might want to replace this with form input)
    text_data = dataCollect()  # This could also come from form input

    # Process the text using your existing functions
    tokens = cleanText(text_data)
    entities = extract_entities(text_data)
    df = vectorize_text(text_data)
    aggregated_entities = aggregate_entities(entities)

    # Call plotting function (this could save an image or return data for charting)
    plot_aggregated_entities(aggregated_entities)

    # Return the results as JSON for the frontend to use
    return jsonify({
        'tokens': tokens,
        'entities': entities,
        'aggregated_entities': aggregated_entities,
        'vectorized_data': df.to_dict()
    })

if __name__ == '__main__':
    app.run(debug=True)
