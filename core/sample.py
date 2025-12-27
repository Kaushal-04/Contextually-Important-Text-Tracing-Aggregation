import os
import logging
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv(dotenv_path=".env")  

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is missing from the .env file")

genai.configure(api_key=google_api_key)

def summarize_paragraphs(pairs):
    try:
        # Prepare the messages for batch processing of pairs
        gemini_messages = [
            {
                "role": "user",
                "parts": [
                    {
                        "text": f"Summarize the following pair of sentences: Sentence 1: {pair[0]} Sentence 2: {pair[1]}"
                    }
                ]
            }
            for pair in pairs
        ]

        # Set up the model for text generation (non-streaming approach)
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",  # You can adjust this to use any other model if needed
            generation_config={"temperature": 0.5}  # Adjust temperature for summarization
        )

        # Generate the response in batch
        responses = model.generate_content(contents=gemini_messages)

        # Extract summarized texts from responses
        summaries = [response.text.strip() if response.text else "Summary unavailable" for response in responses]

        return summaries

    except Exception as e:
        logging.error(f"Error generating summaries: {e}")
        return ["Summary unavailable"] * len(pairs)  # Return default summaries if error occurs
