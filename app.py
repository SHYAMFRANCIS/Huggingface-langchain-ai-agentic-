from flask import Flask, render_template, request, jsonify, send_from_directory
from main import summarize_text
import os
import logging
import html

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Security: Configure security headers
@app.after_request
def after_request(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response

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
        
        # Validate and sanitize inputs
        if not text or not isinstance(text, str):
            return jsonify({'error': 'Text is required and must be a string'}), 400
            
        if not length or length not in ['short', 'medium', 'long']:
            return jsonify({'error': 'Invalid summary length. Must be short, medium, or long'}), 400
        
        # Sanitize input text
        text = html.escape(text).strip()
        
        if not text:
            return jsonify({'error': 'Text is required'}), 400
        
        # Limit input text size to prevent abuse
        if len(text) > 10000:  # 10k characters max
            return jsonify({'error': 'Text is too long. Maximum allowed length is 10,000 characters.'}), 400
        
        logging.info(f"Received summarization request. Length: {len(text)} chars, Desired summary: {length}.")
        # Generate summary using the existing function
        summary = summarize_text(text, length)
        
        # Check if summary is empty or too short
        if not summary or not summary.strip():
            logging.warning("Failed to generate summary for the provided text.")
            return jsonify({'error': 'Could not generate a summary for the provided text. The text may be too short or not suitable for summarization.'}), 400
        
        # Sanitize output before returning
        summary = html.escape(summary)
        
        return jsonify({'summary': summary})
    
    except Exception as e:
        logging.error(f"An error occurred during summarization: {e}", exc_info=True)
        return jsonify({'error': 'An internal server error occurred.'}), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    os.makedirs(templates_dir, exist_ok=True)
    
    # WARNING: Only use debug=True in development. For production, use a production WSGI server like Gunicorn or uWSGI.
    # Security: Run with debug=False in production
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))