# Model Auto-Detection and Dynamic Loading

## Changes Made

The Venice AI interface now **dynamically loads models** from the API instead of using hardcoded model names. This ensures the interface always works with Venice AI's current model lineup.

## Why This Change?

Venice AI regularly updates their available models. Hardcoded model names can become outdated and cause errors like:
```
Error: API Error: 404 - {"error":"Specified model not found: nous-hermes-3"}
```

## How It Works

### Web Interface

1. When you save your API key in Settings, the interface automatically fetches available models
2. Chat models and image models are filtered and populated in their respective dropdowns
3. Click the "↻ Refresh" button next to model selectors to reload the model list
4. Your previously selected model is preserved when refreshing

### Command-Line Interface

Models are auto-detected when you don't specify the `--model` flag:

```bash
# Auto-detects best chat model
python3 venice_cli.py chat -m "Hello"

# Auto-detects best image model
python3 venice_cli.py image "a sunset"

# Or specify a specific model
python3 venice_cli.py chat --model "llama-3.3-70b" -m "Hello"
```

### Python Client

The client library works with any valid model name:

```python
from venice_client import VeniceClient

client = VeniceClient()

# List all available models
models = client.list_models()
for model in models['data']:
    print(model['id'])

# Use any model
response = client.chat_completion(
    messages=[{"role": "user", "content": "Hello"}],
    model="llama-3.3-70b"  # Or any available model
)
```

## Venice AI's Model Paradigm (2025)

As of 2025, Venice uses a simplified model categorization:

- **Venice Uncensored**: For unrestricted conversations
- **Venice Reasoning**: For complex problem-solving
- **Venice Small**: Faster, lightweight model
- **Venice Medium**: Balanced performance
- **Venice Large**: Most capable model

They also provide access to specific models like:
- Llama models (e.g., Llama 3.3, Llama 4 Maverick)
- Qwen models (replacing some Llama variants)
- Flux and other image generation models

## Checking Available Models

### Method 1: Web Interface
1. Open the web interface
2. Go to the "Models" tab
3. Click "Refresh Models List"
4. Browse all available models with their IDs

### Method 2: CLI
```bash
python3 venice_cli.py models
```

### Method 3: Python Script
```python
from venice_client import VeniceClient

client = VeniceClient()
models = client.list_models()

print("Available Models:")
for model in models['data']:
    print(f"  - {model['id']}")
```

## Troubleshooting

### "Error loading models" in web interface
- Make sure you've entered a valid API key in Settings
- Check your internet connection
- Verify your API key at https://venice.ai

### Models not appearing in dropdowns
- Click the "↻ Refresh" button next to the model selector
- Make sure you've saved your API key in Settings
- Check browser console for errors (F12)

### CLI shows "Warning: Could not fetch models"
- Verify VENICE_API_KEY environment variable is set
- Check internet connection
- The CLI will fall back to a default model if auto-detection fails

## Benefits

✅ Always compatible with Venice AI's latest models
✅ No need to update code when Venice adds new models
✅ Automatic fallback to working defaults
✅ Smart filtering between chat and image models
✅ User-friendly model selection in web interface

## References

For the latest information on Venice AI models:
- [Venice AI Blog - New Model Paradigm](https://venice.ai/blog/venice-new-model-paradigm)
- [Venice API Docs - Models Endpoint](https://docs.venice.ai/api-reference/endpoint/models/list)
- [Venice Changelog](https://featurebase.venice.ai/changelog)
