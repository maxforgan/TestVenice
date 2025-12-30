"""
Venice AI API Client
A Python client for interacting with the Venice AI API (OpenAI-compatible).
"""

import os
import json
import requests
from typing import Optional, Dict, List, Any


class VeniceClient:
    """Client for interacting with Venice AI API."""

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the Venice AI client.

        Args:
            api_key: Venice API key (defaults to VENICE_API_KEY env var)
            base_url: Base URL for Venice API (defaults to official endpoint)
        """
        self.api_key = api_key or os.getenv('VENICE_API_KEY')
        self.base_url = base_url or os.getenv('VENICE_API_BASE_URL', 'https://api.venice.ai/api/v1')

        if not self.api_key:
            raise ValueError("API key is required. Set VENICE_API_KEY environment variable or pass api_key parameter.")

        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def chat_completion(
        self,
        messages: List[Dict[str, str]],
        model: str = "llama-3.3-70b",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        stream: bool = False
    ) -> Dict[str, Any]:
        """
        Create a chat completion.

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use for completion
            temperature: Sampling temperature (0-2)
            max_tokens: Maximum tokens to generate
            stream: Whether to stream the response

        Returns:
            API response as dictionary
        """
        endpoint = f"{self.base_url}/chat/completions"

        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "stream": stream
        }

        if max_tokens:
            payload["max_tokens"] = max_tokens

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()

        return response.json()

    def generate_image(
        self,
        prompt: str,
        model: str = "fluently-xl",
        width: int = 1024,
        height: int = 1024,
        num_images: int = 1
    ) -> Dict[str, Any]:
        """
        Generate an image from a text prompt.

        Args:
            prompt: Text description of the image to generate
            model: Image generation model to use
            width: Image width in pixels
            height: Image height in pixels
            num_images: Number of images to generate

        Returns:
            API response with image URLs
        """
        endpoint = f"{self.base_url}/images/generations"

        payload = {
            "prompt": prompt,
            "model": model,
            "width": width,
            "height": height,
            "n": num_images
        }

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()

        return response.json()

    def list_models(self) -> Dict[str, Any]:
        """
        List available models.

        Returns:
            API response with available models
        """
        endpoint = f"{self.base_url}/models"

        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()

        return response.json()

    def text_to_speech(
        self,
        text: str,
        model: str = "kokoro",
        voice: str = "default"
    ) -> bytes:
        """
        Convert text to speech.

        Args:
            text: Text to convert to speech
            model: TTS model to use
            voice: Voice to use

        Returns:
            Audio data as bytes
        """
        endpoint = f"{self.base_url}/audio/speech"

        payload = {
            "model": model,
            "input": text,
            "voice": voice
        }

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()

        return response.content

    def generate_video_from_text(
        self,
        prompt: str,
        model: str,
        duration: int = 5,
        fps: int = 30,
        resolution: str = "1024x576"
    ) -> Dict[str, Any]:
        """
        Generate a video from a text prompt.

        Args:
            prompt: Text description of the video to generate
            model: Video generation model to use
            duration: Video duration in seconds
            fps: Frames per second
            resolution: Video resolution (e.g., "1024x576", "1280x720")

        Returns:
            API response with video URL
        """
        endpoint = f"{self.base_url}/videos/generations"

        payload = {
            "prompt": prompt,
            "model": model,
            "duration": duration,
            "fps": fps,
            "resolution": resolution,
            "type": "text-to-video"
        }

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()

        return response.json()

    def generate_video_from_image(
        self,
        image_data: str,
        model: str,
        motion_prompt: Optional[str] = None,
        duration: int = 5,
        fps: int = 30
    ) -> Dict[str, Any]:
        """
        Generate a video from an image.

        Args:
            image_data: Base64 encoded image data or image URL
            model: Video generation model to use
            motion_prompt: Optional description of desired motion
            duration: Video duration in seconds
            fps: Frames per second

        Returns:
            API response with video URL
        """
        endpoint = f"{self.base_url}/videos/generations"

        payload = {
            "image": image_data,
            "model": model,
            "duration": duration,
            "fps": fps,
            "type": "image-to-video"
        }

        if motion_prompt:
            payload["prompt"] = motion_prompt

        response = requests.post(endpoint, headers=self.headers, json=payload)
        response.raise_for_status()

        return response.json()


if __name__ == "__main__":
    # Example usage
    client = VeniceClient()

    # Test chat completion
    messages = [
        {"role": "user", "content": "Hello! What is Venice AI?"}
    ]

    response = client.chat_completion(messages)
    print(json.dumps(response, indent=2))
