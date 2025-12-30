# Venice AI Interface

A comprehensive interface for interacting with the Venice AI API. Venice AI provides private, decentralized AI with support for chat, image generation, and text-to-speech.

## Features

- **Python Client Library**: Easy-to-use Python client for Venice AI API
- **Command-Line Interface**: Interactive and scriptable CLI tool
- **Web Interface**: Beautiful browser-based interface for all Venice AI features
- **Mobile-Friendly**: Fully responsive web interface works on smartphones and tablets
- **Multiple Capabilities**:
  - Chat with various LLM models
  - Generate images with text prompts
  - Text-to-speech conversion
  - Model browsing and selection

## Getting Started

### Prerequisites

- Python 3.7+
- Venice AI API key (get one at [venice.ai](https://venice.ai))

### Installation

1. Clone or download this repository
2. Install Python dependencies:

```bash
pip install requests
```

3. Set your API key as an environment variable:

```bash
export VENICE_API_KEY="your-api-key-here"
```

Or create a `.env` file:

```bash
echo "VENICE_API_KEY=your-api-key-here" > .env
```

## Usage

### Web Interface

Simply open `index.html` in your web browser:

```bash
# Using Python's built-in server
python3 -m http.server 8000
```

Then navigate to `http://localhost:8000` in your browser.

Features:
- Configure API settings
- Interactive chat with AI models
- Generate images from text prompts
- Browse available models

#### Using on Mobile

The web interface is fully mobile-responsive! See [MOBILE_GUIDE.md](MOBILE_GUIDE.md) for detailed setup instructions.

Quick options:
- **Same WiFi**: Access from your phone at `http://YOUR-COMPUTER-IP:8000`
- **GitHub Pages**: Deploy for access from anywhere
- **Home Screen**: Add as a shortcut for app-like experience

### Command-Line Interface

The CLI provides several commands for interacting with Venice AI:

#### Interactive Chat

```bash
python3 venice_cli.py chat --interactive
```

#### Single Message

```bash
python3 venice_cli.py chat --message "What is Venice AI?"
```

#### Generate Image

```bash
python3 venice_cli.py image "A beautiful sunset over mountains" --output sunset.png
```

#### List Available Models

```bash
python3 venice_cli.py models
```

#### Text to Speech

```bash
python3 venice_cli.py tts "Hello, this is Venice AI" --output hello.mp3
```

### Python Library

Use the Venice client in your own Python scripts:

```python
from venice_client import VeniceClient

# Initialize client
client = VeniceClient()  # Uses VENICE_API_KEY env var

# Chat completion
messages = [
    {"role": "user", "content": "Hello!"}
]
response = client.chat_completion(messages)
print(response['choices'][0]['message']['content'])

# Generate image
result = client.generate_image("A futuristic city at night")
print(result['data'][0]['url'])

# List models
models = client.list_models()
for model in models['data']:
    print(model['id'])
```

## API Configuration

### Environment Variables

- `VENICE_API_KEY`: Your Venice AI API key (required)
- `VENICE_API_BASE_URL`: Base URL for the API (default: `https://api.venice.ai/api/v1`)

### Available Models

**Chat Models:**
- `llama-3.3-70b` - Llama 3.3 70B (default)
- `llama-3.1-405b` - Llama 3.1 405B
- `nous-hermes-3` - Nous Hermes 3

**Image Models:**
- `fluently-xl` - Fluently XL (default)
- `flux-pro` - Flux Pro
- `stable-diffusion` - Stable Diffusion

**Audio Models:**
- `kokoro` - Kokoro TTS (default)

## Project Structure

```
.
├── venice_client.py    # Python client library
├── venice_cli.py       # Command-line interface
├── index.html          # Web interface
├── example.py          # Usage examples
├── README.md           # This file
├── MOBILE_GUIDE.md     # Mobile setup instructions
├── requirements.txt    # Python dependencies
└── .env.example        # Example environment file
```

## Examples

### Example 1: Quick Chat

```bash
python3 venice_cli.py chat -m "Explain quantum computing in simple terms"
```

### Example 2: Generate Multiple Images

```bash
python3 venice_cli.py image "Cyberpunk character portrait" -o portrait1.png
python3 venice_cli.py image "Steampunk robot" -o portrait2.png
```

### Example 3: Custom Script

```python
from venice_client import VeniceClient

client = VeniceClient()

# Multi-turn conversation
messages = []
questions = [
    "What is machine learning?",
    "How does it differ from traditional programming?",
    "What are some real-world applications?"
]

for question in questions:
    messages.append({"role": "user", "content": question})
    response = client.chat_completion(messages)
    answer = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": answer})
    print(f"Q: {question}")
    print(f"A: {answer}\n")
```

## Troubleshooting

### API Key Issues

If you see "API key is required" errors:
1. Verify your API key is set: `echo $VENICE_API_KEY`
2. Ensure the key is valid at [venice.ai](https://venice.ai)
3. Check for typos or extra whitespace

### Connection Errors

If you experience connection issues:
1. Check your internet connection
2. Verify the API base URL is correct
3. Check Venice AI status page for outages

### CORS Issues (Web Interface)

If the web interface shows CORS errors:
1. Serve the HTML file through a local server (not file://)
2. Use `python3 -m http.server 8000`
3. Note: Direct API calls from browser may have CORS restrictions

## Resources

- [Venice AI Official Site](https://venice.ai)
- [Venice API Documentation](https://docs.venice.ai)
- [Venice API Blog Post](https://venice.ai/blog/how-to-use-venice-api)
- [Postman Documentation](https://postman.venice.ai)

## License

This project is provided as-is for educational and development purposes.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.
