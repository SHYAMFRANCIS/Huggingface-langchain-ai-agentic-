# SummaQ - AI Text Summarizer

A Flask-based web application that leverages Hugging Face Transformers to provide AI-powered text summarization capabilities.

## Features

- **Text Summarization**: Condense lengthy text into concise summaries in short, medium, or long formats
- **CPU-Optimized**: Uses efficient models that run well on CPU without requiring GPU hardware
- **Flexible Length Control**: Customize summary length based on your needs
- **Modern UI**: Clean, responsive web interface with accessibility features
- **RESTful API**: Programmatic access to summarization functionality
- **Input Validation**: Prevents DoS attacks from overly large inputs
- **Security Features**: XSS protection, security headers, and input sanitization

## Architecture

This project uses the following key technologies:

- **Hugging Face Transformers**: Provides pre-trained models for summarization
- **DistilBART**: Fast and efficient summarization model
- **Flask**: Web framework for the API and UI
- **Python 3**: Core programming language

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/SHYAMFRANCIS/Huggingface-langchain-ai-agentic-.git
   cd Huggingface-langchain-ai-agentic-
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

The project requires the following packages:

```
torch
transformers
flask
```

## Usage

### Web Interface

To start the web application:

```bash
python app.py
```

Then navigate to `http://localhost:5000` in your browser.

### Command Line

To run tests with the default prompts:

```bash
python main.py
```

### Environment Variables

- `FLASK_DEBUG`: Set to `true` to enable debug mode (defaults to `False`)
- `PORT`: Port number to run the application on (defaults to `5000`)

### Custom Usage

The core functionality can be used programmatically:

```python
from main import summarize_text

# Generate a summary
summary = summarize_text("Your text here", "medium")
print(summary)
```

## API Endpoints

### GET /
Returns the main UI page

### POST /summarize
Accepts JSON payload with `text` and `length` fields and returns a summarized version of the text.

Example request:
```json
{
  "text": "Your text to summarize here...",
  "length": "medium"
}
```

Example response:
```json
{
  "summary": "Summarized text..."
}
```

## Project Structure

- `app.py`: Flask application entry point with security enhancements
- `main.py`: AI model logic and summarization functions
- `requirements.txt`: Python dependencies (optimized)
- `templates/modern_ui.html`: HTML template with security headers
- `static/css/modern_ui.css`: CSS styling
- `static/js/modern_ui.js`: Client-side JavaScript with security validations
- `README.md`: Project documentation

## Models Used

- **Summarization**: `sshleifer/distilbart-cnn-12-6` - A distilled, efficient version of BART optimized for summarization

## Security Enhancements

The application includes several security improvements made during recent refactoring:

- **Input Sanitization**: Both server and client-side input validation
- **Security Headers**: X-Content-Type-Options, X-Frame-Options, and X-XSS-Protection
- **CSP Headers**: Content Security Policy in HTML template to prevent XSS
- **URL Validation**: Client-side validation of API endpoints
- **Rate Limit Prevention**: Input length limits to prevent abuse (10,000 character max)
- **Output Sanitization**: Server-side sanitization of results before returning
- **Environment-based Debugging**: Uses environment variables to control debug mode in production

## Performance Optimization

The application implements several optimizations for CPU environments:

1. **Fast Models**: Uses distilled models that maintain quality while reducing computational overhead
2. **Single Pipeline Reuse**: Creates model pipelines once and reuses them
3. **Length Control**: Allows for summaries of different lengths to balance quality and speed
4. **Memory Management**: Efficient memory usage with proper caching
5. **Error Handling**: Robust error handling for production reliability
6. **Warning Suppression**: Filters unnecessary warnings for cleaner output

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Hugging Face for providing access to state-of-the-art transformer models
- The DistilBART model that makes this functionality possible
- The Flask community for the web framework
- The open-source community for the tools and libraries that power this project