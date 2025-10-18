from flask import Flask, render_template, request, jsonify, send_from_directory
from main import summarize_text
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('modern_ui.html')

@app.route('/favicon.ico')
def favicon():
    # Return an empty 204 No Content response to prevent 404 errors for the favicon
    return '', 204

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON payload'}), 400

        text = data.get('text', '')
        length = data.get('length', 'medium')
        
        if not text.strip():
            return jsonify({'error': 'Text is required'}), 400
        
        logging.info(f"Received summarization request. Length: {len(text)} chars, Desired summary: {length}.")
        # Generate summary using the existing function
        summary = summarize_text(text, length)
        
        # Check if summary is empty or too short
        if not summary.strip():
            logging.warning("Failed to generate summary for the provided text.")
            return jsonify({'error': 'Could not generate a summary for the provided text. The text may be too short or not suitable for summarization.'}), 400
        
        return jsonify({'summary': summary})
    
    except Exception as e:
        logging.error(f"An error occurred during summarization: {e}", exc_info=True)
        return jsonify({'error': 'An internal server error occurred.'}), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    os.makedirs(templates_dir, exist_ok=True)
    
    # WARNING: debug=True is not for production use. Use a production WSGI server like Gunicorn or uWSGI.
    app.run(debug=True, host='0.0.0.0', port=5000)