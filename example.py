#!/usr/bin/env python3
"""
Example script demonstrating Venice AI API usage.
"""

import os
from venice_client import VeniceClient


def main():
    print("Venice AI API Example")
    print("=" * 50)

    # Check if API key is set
    api_key = os.getenv('VENICE_API_KEY')
    if not api_key:
        print("\nError: VENICE_API_KEY environment variable not set!")
        print("Please set it with: export VENICE_API_KEY='your-key-here'")
        return

    try:
        # Initialize client
        print("\n1. Initializing Venice AI client...")
        client = VeniceClient()
        print("   ✓ Client initialized successfully")

        # Example 1: Simple chat
        print("\n2. Testing chat completion...")
        messages = [
            {"role": "user", "content": "In one sentence, what is Venice AI?"}
        ]
        response = client.chat_completion(messages, model="llama-3.3-70b")
        answer = response['choices'][0]['message']['content']
        print(f"   Question: {messages[0]['content']}")
        print(f"   Answer: {answer}")

        # Example 2: Multi-turn conversation
        print("\n3. Testing multi-turn conversation...")
        conversation = [
            {"role": "user", "content": "What's the capital of France?"}
        ]
        response = client.chat_completion(conversation)
        assistant_msg = response['choices'][0]['message']['content']
        conversation.append({"role": "assistant", "content": assistant_msg})
        print(f"   User: {conversation[0]['content']}")
        print(f"   AI: {assistant_msg}")

        conversation.append({"role": "user", "content": "What's its population?"})
        response = client.chat_completion(conversation)
        assistant_msg = response['choices'][0]['message']['content']
        print(f"   User: {conversation[2]['content']}")
        print(f"   AI: {assistant_msg}")

        # Example 3: List models
        print("\n4. Listing available models...")
        models_response = client.list_models()
        if 'data' in models_response:
            print(f"   Found {len(models_response['data'])} models:")
            for model in models_response['data'][:5]:  # Show first 5
                print(f"   - {model.get('id', 'Unknown')}")
            if len(models_response['data']) > 5:
                print(f"   ... and {len(models_response['data']) - 5} more")

        print("\n" + "=" * 50)
        print("All examples completed successfully!")
        print("\nNext steps:")
        print("- Try the CLI: python3 venice_cli.py chat --interactive")
        print("- Open the web interface: index.html")
        print("- Generate an image: python3 venice_cli.py image 'a sunset'")

    except ValueError as e:
        print(f"\n✗ Configuration Error: {e}")
    except Exception as e:
        print(f"\n✗ Error: {e}")
        print("\nMake sure:")
        print("1. Your API key is valid")
        print("2. You have internet connection")
        print("3. Venice AI API is accessible")


if __name__ == "__main__":
    main()
