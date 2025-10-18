# Huggingface-langchain-ai-agentic - SummaQ

SummaQ is an efficient Python application that leverages Hugging Face's state-of-the-art transformer models to perform text summarization and question answering. The project focuses on providing fast, accurate text processing while optimizing performance for CPU environments.

## Features

- **Text Summarization**: Condense lengthy text into concise summaries in short, medium, or long formats
- **Question Answering**: Extract answers to specific questions from the generated summaries
- **CPU-Optimized**: Uses efficient models that run well on CPU without requiring GPU hardware
- **Flexible Length Control**: Customize summary length based on your needs
- **Performance Monitoring**: Built-in timing metrics to monitor execution speed
- **Input Validation**: Prevents DoS attacks from overly large inputs
- **Error Handling**: Robust error handling for production reliability

## Architecture

This project uses the following key technologies:

- **Hugging Face Transformers**: Provides pre-trained models for summarization and question answering
- **DistilBART**: Fast and efficient summarization model
- **RoBERTa**: SQuAD-optimized model for question answering
- **Python 3**: Core programming language
- **LangChain** (HuggingFacePipeline): For integrating Hugging Face models into a pipeline

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/SHYAMFRANCIS/Huggingface-langchain-ai-agentic-.git
   cd Huggingface-langchain-ai-agentic-
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

Make sure you have the following packages installed:

```
transformers
torch
langchain-huggingface
```

You can install them using:

```bash
pip install transformers torch langchain-huggingface
```

## Usage

To run the application with the default test prompts:

```bash
python main.py
```

### Custom Usage

The core functionality can be used programmatically:

```python
from main import summarize_text

# Generate a summary
summary = summarize_text("Your text here", "medium")
print(summary)
```

### Configuration

You can customize the model cache directory by setting the `TRANSFORMERS_CACHE` environment variable:

```bash
export TRANSFORMERS_CACHE="/path/to/your/cache/directory"
```

## Project Structure

- `main.py`: The main application logic
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation
- `.gitignore`: Files and directories to be ignored by Git
- `QWEN_MEMORY.md`: Development notes (not included in Git)

## Models Used

- **Summarization Model**: `sshleifer/distilbart-cnn-12-6` - A distilled, efficient version of BART optimized for summarization
- **Question Answering Model**: `deepset/roberta-base-squad2` - A RoBERTa model fine-tuned on the SQuAD2.0 dataset

## Performance Optimization

The application implements several optimizations for CPU environments:

1. **Fast Models**: Uses distilled models that maintain quality while reducing computational overhead
2. **Single Pipeline Reuse**: Creates model pipelines once and reuses them
3. **Length Control**: Allows for summaries of different lengths to balance quality and speed
4. **Memory Management**: Properly handles GPU usage when available with `device_map="auto"`
5. **Time Limits**: Sets maximum generation time to prevent long-running operations

## Security Considerations

- Input validation prevents denial-of-service from large inputs
- Model versions should be pinned in production for consistency
- API tokens should be stored securely using environment variables if authentication is required
- For web deployment, ensure the Flask app runs with `debug=False` in production
- Use a production WSGI server like Gunicorn with proper security headers
- Input sanitization is implemented to prevent XSS attacks
- The application includes Content Security Policy (CSP) headers in the HTML template

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
- The DistilBART and RoBERTa models that make this functionality possible
- The open-source community for the tools and libraries that power this project
