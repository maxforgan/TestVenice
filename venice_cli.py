#!/usr/bin/env python3
"""
Venice AI CLI
Interactive command-line interface for Venice AI API.
"""

import argparse
import sys
import json
from venice_client import VeniceClient


def chat_interactive(client: VeniceClient, model: str = "llama-3.3-70b"):
    """Run an interactive chat session."""
    print("Venice AI Chat (type 'exit' or 'quit' to end, 'clear' to reset conversation)")
    print("=" * 70)

    messages = []

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break

            if user_input.lower() == 'clear':
                messages = []
                print("Conversation cleared.")
                continue

            messages.append({"role": "user", "content": user_input})

            response = client.chat_completion(messages, model=model)

            assistant_message = response['choices'][0]['message']['content']
            messages.append({"role": "assistant", "content": assistant_message})

            print(f"\nAssistant: {assistant_message}")

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")


def chat_single(client: VeniceClient, message: str, model: str = "llama-3.3-70b"):
    """Send a single chat message."""
    messages = [{"role": "user", "content": message}]
    response = client.chat_completion(messages, model=model)
    print(response['choices'][0]['message']['content'])


def generate_image_cmd(client: VeniceClient, prompt: str, output: str = "image.png", model: str = "fluently-xl"):
    """Generate an image from a prompt."""
    print(f"Generating image: {prompt}")
    response = client.generate_image(prompt, model=model)

    if 'data' in response and len(response['data']) > 0:
        image_url = response['data'][0].get('url')
        if image_url:
            print(f"Image generated successfully!")
            print(f"URL: {image_url}")

            # Download image if output path specified
            if output:
                import requests
                img_data = requests.get(image_url).content
                with open(output, 'wb') as f:
                    f.write(img_data)
                print(f"Image saved to: {output}")
        else:
            print("Image generated but no URL returned")
            print(json.dumps(response, indent=2))
    else:
        print("Error: No image data in response")
        print(json.dumps(response, indent=2))


def list_models_cmd(client: VeniceClient):
    """List available models."""
    response = client.list_models()
    print(json.dumps(response, indent=2))


def text_to_speech_cmd(client: VeniceClient, text: str, output: str = "speech.mp3", model: str = "kokoro"):
    """Convert text to speech."""
    print(f"Converting text to speech...")
    audio_data = client.text_to_speech(text, model=model)

    with open(output, 'wb') as f:
        f.write(audio_data)

    print(f"Audio saved to: {output}")


def main():
    parser = argparse.ArgumentParser(description='Venice AI CLI - Interact with Venice AI API')
    parser.add_argument('--api-key', help='Venice API key (or set VENICE_API_KEY env var)')

    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # Chat command
    chat_parser = subparsers.add_parser('chat', help='Chat with Venice AI')
    chat_parser.add_argument('--message', '-m', help='Single message (non-interactive)')
    chat_parser.add_argument('--model', default='llama-3.3-70b', help='Model to use')
    chat_parser.add_argument('--interactive', '-i', action='store_true', help='Interactive chat mode')

    # Image generation command
    image_parser = subparsers.add_parser('image', help='Generate an image')
    image_parser.add_argument('prompt', help='Image generation prompt')
    image_parser.add_argument('--output', '-o', default='image.png', help='Output file path')
    image_parser.add_argument('--model', default='fluently-xl', help='Image model to use')

    # List models command
    subparsers.add_parser('models', help='List available models')

    # Text-to-speech command
    tts_parser = subparsers.add_parser('tts', help='Convert text to speech')
    tts_parser.add_argument('text', help='Text to convert to speech')
    tts_parser.add_argument('--output', '-o', default='speech.mp3', help='Output file path')
    tts_parser.add_argument('--model', default='kokoro', help='TTS model to use')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        client = VeniceClient(api_key=args.api_key)

        if args.command == 'chat':
            if args.interactive or not args.message:
                chat_interactive(client, model=args.model)
            else:
                chat_single(client, args.message, model=args.model)

        elif args.command == 'image':
            generate_image_cmd(client, args.prompt, output=args.output, model=args.model)

        elif args.command == 'models':
            list_models_cmd(client)

        elif args.command == 'tts':
            text_to_speech_cmd(client, args.text, output=args.output, model=args.model)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
