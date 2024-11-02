from flask import Flask, render_template, request
from pairGeneration import pairs

app = Flask(__name__)

# Route for the dashboard (homepage)
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/index')
def index():
    return render_template('index.html')

# Route for processing the text and showing results
@app.route('/process', methods=['POST'])
def process_text():
    # Collect text data from form input
    text_data = request.form.get('text_data', '')
    sentence_pairs = pairs

    # Render a new template to display the pairs
    return render_template('pairs.html', pairs=sentence_pairs)

if __name__ == '__main__':
    app.run(debug=True)
