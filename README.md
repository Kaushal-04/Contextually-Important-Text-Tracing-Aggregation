# Contextually Important Text Tracing and Aggregation

## EssenceExtract

EssenceExtract is a web application that provides an advanced solution for efficiently analyzing and summarizing large volumes of text. Using Natural Language Processing (NLP) techniques, it identifies key themes, sentiment, and context within text data to generate concise summaries.

## Features

-   **Text Summarization**: Condenses large texts into key sentence pairs.
-   **Contextual Analysis**: Traces important text based on context.
-   **Web Interface**: Easy-to-use dashboard for inputting text and viewing results.

## Project Structure

-   `core/`: Contains the backend logic for text processing, matrix creation, and pair generation.
-   `data/`: Stores data files.
-   `static/`: Contains static assets like CSS, JavaScript, and images.
-   `templates/`: Contains HTML templates for the web interface.
-   `main.py`: The entry point for the Flask application.

## Installation

1.  Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd Contextually-Important-Text-Tracing-Aggregation
    ```
3.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You may need to create a requirements.txt file if one doesn't exist, containing packages like flask, nltk, etc.)*

## Usage

1.  Run the application:
    ```bash
    python main.py
    ```
2.  Open your browser and navigate to `http://127.0.0.1:5000/`.
3.  Enter your text in the input area and click "Summarize".