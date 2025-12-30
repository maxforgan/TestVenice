#!/usr/bin/env python3
"""
Venice AI CLI
Interactive command-line interface for Venice AI API.
"""

import argparse
import sys
import json
from venice_client import VeniceClient


def chat_interactive(client: VeniceClient, model: str = None):
    """Run an interactive chat session."""
    # Get available models if no model specified
    if not model:
        try:
            models_response = client.list_models()
            if 'data' in models_response and len(models_response['data']) > 0:
                model = models_response['data'][0]['id']
                print(f"Using model: {model}")
            else:
                print("Warning: Could not fetch models, using default")
                model = "llama-3.3-70b"
        except:
            print("Warning: Could not fetch models, using default")
            model = "llama-3.3-70b"

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


def chat_single(client: VeniceClient, message: str, model: str = None):
    """Send a single chat message."""
    # Get available models if no model specified
    if not model:
        try:
            models_response = client.list_models()
            if 'data' in models_response and len(models_response['data']) > 0:
                model = models_response['data'][0]['id']
        except:
            model = "llama-3.3-70b"

    messages = [{"role": "user", "content": message}]
    response = client.chat_completion(messages, model=model)
    print(response['choices'][0]['message']['content'])


def generate_image_cmd(client: VeniceClient, prompt: str, output: str = "image.png", model: str = None):
    """Generate an image from a prompt."""
    # Get available image models if no model specified
    if not model:
        try:
            models_response = client.list_models()
            if 'data' in models_response:
                # Try to find an image model
                for m in models_response['data']:
                    model_id = m['id'].lower()
                    if 'flux' in model_id or 'stable' in model_id or 'fluently' in model_id:
                        model = m['id']
                        break
                if not model:
                    model = models_response['data'][0]['id']  # Use first available
        except:
            model = "fluently-xl"  # Fallback

    print(f"Generating image: {prompt}")
    print(f"Using model: {model}")
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


def generate_video_from_text_cmd(
    client: VeniceClient,
    prompt: str,
    model: str,
    output: str = "video.mp4",
    duration: int = 5,
    fps: int = 30,
    resolution: str = "1024x576"
):
    """Generate a video from text prompt."""
    print(f"Generating video from prompt: {prompt}")
    print(f"Using model: {model}")
    print(f"Duration: {duration}s | FPS: {fps} | Resolution: {resolution}")
    print("This may take a few minutes...")

    response = client.generate_video_from_text(prompt, model, duration, fps, resolution)

    if 'data' in response and len(response['data']) > 0:
        video_url = response['data'][0].get('url')
        if video_url:
            print(f"Video generated successfully!")
            print(f"URL: {video_url}")

            # Download video if output path specified
            if output:
                import requests
                video_data = requests.get(video_url).content
                with open(output, 'wb') as f:
                    f.write(video_data)
                print(f"Video saved to: {output}")
        else:
            print("Video generated but no URL returned")
            print(json.dumps(response, indent=2))
    else:
        print("Error: No video data in response")
        print(json.dumps(response, indent=2))


def generate_video_from_image_cmd(
    client: VeniceClient,
    image_path: str,
    model: str,
    output: str = "video.mp4",
    motion_prompt: str = None,
    duration: int = 5,
    fps: int = 30
):
    """Generate a video from an image."""
    import base64

    print(f"Loading image: {image_path}")

    # Read and encode image
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')

    print(f"Generating video from image...")
    print(f"Using model: {model}")
    if motion_prompt:
        print(f"Motion prompt: {motion_prompt}")
    print(f"Duration: {duration}s | FPS: {fps}")
    print("This may take a few minutes...")

    response = client.generate_video_from_image(
        f"data:image/png;base64,{image_data}",
        model,
        motion_prompt,
        duration,
        fps
    )

    if 'data' in response and len(response['data']) > 0:
        video_url = response['data'][0].get('url')
        if video_url:
            print(f"Video generated successfully!")
            print(f"URL: {video_url}")

            # Download video if output path specified
            if output:
                import requests
                video_data = requests.get(video_url).content
                with open(output, 'wb') as f:
                    f.write(video_data)
                print(f"Video saved to: {output}")
        else:
            print("Video generated but no URL returned")
            print(json.dumps(response, indent=2))
    else:
        print("Error: No video data in response")
        print(json.dumps(response, indent=2))


def main():
    parser = argparse.ArgumentParser(description='Venice AI CLI - Interact with Venice AI API')
    parser.add_argument('--api-key', help='Venice API key (or set VENICE_API_KEY env var)')

    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # Chat command
    chat_parser = subparsers.add_parser('chat', help='Chat with Venice AI')
    chat_parser.add_argument('--message', '-m', help='Single message (non-interactive)')
    chat_parser.add_argument('--model', help='Model to use (auto-detects if not specified)')
    chat_parser.add_argument('--interactive', '-i', action='store_true', help='Interactive chat mode')

    # Image generation command
    image_parser = subparsers.add_parser('image', help='Generate an image')
    image_parser.add_argument('prompt', help='Image generation prompt')
    image_parser.add_argument('--output', '-o', default='image.png', help='Output file path')
    image_parser.add_argument('--model', help='Image model to use (auto-detects if not specified)')

    # List models command
    subparsers.add_parser('models', help='List available models')

    # Text-to-speech command
    tts_parser = subparsers.add_parser('tts', help='Convert text to speech')
    tts_parser.add_argument('text', help='Text to convert to speech')
    tts_parser.add_argument('--output', '-o', default='speech.mp3', help='Output file path')
    tts_parser.add_argument('--model', default='kokoro', help='TTS model to use')

    # Video generation (text-to-video) command
    video_text_parser = subparsers.add_parser('video-text', help='Generate video from text')
    video_text_parser.add_argument('prompt', help='Video generation prompt')
    video_text_parser.add_argument('--model', required=True, help='Video model to use')
    video_text_parser.add_argument('--output', '-o', default='video.mp4', help='Output file path')
    video_text_parser.add_argument('--duration', type=int, default=5, help='Duration in seconds (default: 5)')
    video_text_parser.add_argument('--fps', type=int, default=30, help='Frames per second (default: 30)')
    video_text_parser.add_argument('--resolution', default='1024x576', help='Resolution (default: 1024x576)')

    # Video generation (image-to-video) command
    video_image_parser = subparsers.add_parser('video-image', help='Generate video from image')
    video_image_parser.add_argument('image', help='Path to input image')
    video_image_parser.add_argument('--model', required=True, help='Video model to use')
    video_image_parser.add_argument('--output', '-o', default='video.mp4', help='Output file path')
    video_image_parser.add_argument('--motion-prompt', help='Optional motion description')
    video_image_parser.add_argument('--duration', type=int, default=5, help='Duration in seconds (default: 5)')
    video_image_parser.add_argument('--fps', type=int, default=30, help='Frames per second (default: 30)')

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

        elif args.command == 'video-text':
            generate_video_from_text_cmd(
                client,
                args.prompt,
                args.model,
                output=args.output,
                duration=args.duration,
                fps=args.fps,
                resolution=args.resolution
            )

        elif args.command == 'video-image':
            generate_video_from_image_cmd(
                client,
                args.image,
                args.model,
                output=args.output,
                motion_prompt=args.motion_prompt,
                duration=args.duration,
                fps=args.fps
            )

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
