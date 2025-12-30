# Video Generation Guide

The Venice AI interface now supports comprehensive video generation with both text-to-video and image-to-video capabilities!

## Features

### 🎬 Two Generation Modes

**Text to Video (📝)**
- Generate videos from text descriptions
- Control duration, FPS, and resolution
- Perfect for creating original video content

**Image to Video (🖼️)**
- Animate static images
- Add motion with optional prompts
- Transform photos into dynamic videos

## Web Interface Usage

### Getting Started

1. **Configure API Key**
   - Go to Settings tab
   - Enter your Venice API key
   - Click "Save Settings"
   - Video models will load automatically

2. **Access Video Generation**
   - Click the "Video Generation" tab
   - Choose your generation mode (Text or Image)

### Text to Video

1. **Select Mode**
   - Click "📝 Text to Video" button (selected by default)

2. **Choose Model**
   - Select a video model from the dropdown
   - Click ↻ Refresh if no models appear

3. **Enter Prompt**
   - Describe the video you want to generate
   - Example: "A serene sunset over the ocean with waves gently crashing"
   - Be specific about motion, camera movement, and visual details

4. **Configure Parameters**
   - **Duration**: 1-30 seconds (default: 5)
   - **FPS**: 24, 30, or 60 (default: 30)
   - **Resolution**: Choose from presets
     - 512x512 (square)
     - 768x768 (square HD)
     - 1024x576 (16:9 widescreen) ⭐ recommended
     - 1280x720 (HD 720p)

5. **Generate**
   - Click "Generate Video from Text"
   - Wait for processing (may take several minutes)
   - Video will appear with playback controls
   - Click download button to save

### Image to Video

1. **Select Mode**
   - Click "🖼️ Image to Video" button

2. **Upload Image**
   - Click the upload area or drag & drop
   - Supported formats: JPG, PNG, WebP
   - Preview will appear after upload

3. **Choose Model**
   - Select a video model from the dropdown

4. **Add Motion Prompt (Optional)**
   - Describe the motion/animation you want
   - Examples:
     - "Camera slowly zooms out"
     - "Clouds moving across the sky"
     - "Character turns head to look at camera"
   - Leave blank for automatic motion

5. **Configure Parameters**
   - **Duration**: 1-30 seconds (default: 5)
   - **FPS**: 24, 30, or 60 (default: 30)

6. **Generate**
   - Click "Generate Video from Image"
   - Wait for processing
   - Video player will show the result

## Command-Line Interface

### Text to Video

```bash
# Basic usage
python3 venice_cli.py video-text "A butterfly flying through a forest" --model <model-name>

# With custom parameters
python3 venice_cli.py video-text "Ocean waves at sunset" \
  --model <model-name> \
  --duration 10 \
  --fps 30 \
  --resolution 1280x720 \
  --output my-ocean-video.mp4
```

### Image to Video

```bash
# Basic usage
python3 venice_cli.py video-image photo.jpg --model <model-name>

# With motion prompt
python3 venice_cli.py video-image portrait.jpg \
  --model <model-name> \
  --motion-prompt "Camera slowly zooms in on face" \
  --duration 8 \
  --fps 30 \
  --output animated-portrait.mp4
```

## Python Client Library

```python
from venice_client import VeniceClient

client = VeniceClient()

# Text to Video
response = client.generate_video_from_text(
    prompt="A cat playing with a ball of yarn",
    model="your-video-model",
    duration=5,
    fps=30,
    resolution="1024x576"
)

video_url = response['data'][0]['url']
print(f"Video URL: {video_url}")

# Image to Video
import base64

with open('image.jpg', 'rb') as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')

response = client.generate_video_from_image(
    image_data=f"data:image/jpeg;base64,{image_data}",
    model="your-video-model",
    motion_prompt="Camera pans left to right",
    duration=5,
    fps=30
)

video_url = response['data'][0]['url']
```

## Tips for Best Results

### Prompt Writing

**Text to Video Prompts:**
- Be specific about motion and action
- Include camera movement if desired
- Describe the scene in detail
- Mention lighting and atmosphere
- Example: "Slow motion close-up of rain drops hitting a puddle, soft morning light, gentle ripples"

**Motion Prompts (Image to Video):**
- Describe specific movements
- Mention camera actions
- Keep it concise
- Example: "Gentle camera push-in, hair blowing in wind"

### Parameter Selection

**Duration:**
- Shorter (3-5s): Quick actions, simple motions
- Medium (5-10s): Complex scenes, smooth transitions
- Longer (10-30s): Narrative sequences, slow motion

**FPS:**
- 24 fps: Cinematic look, traditional film
- 30 fps: Standard video, smooth motion (recommended)
- 60 fps: Ultra-smooth, slow motion playback

**Resolution:**
- 512x512: Fast generation, social media
- 1024x576: Balanced quality/speed (16:9 recommended)
- 1280x720: Higher quality, slower generation

## Available Models

Video models are automatically detected and loaded. Common video model types include:
- Runway Gen-2/Gen-3
- Pika Labs
- Stability AI Video
- Kling AI
- OpenAI Sora (if available)

Check the Models tab to see which video models are available with your API key.

## Troubleshooting

### No models appearing
- Ensure API key is saved in Settings
- Click ↻ Refresh button
- Check browser console (F12) for errors
- Verify API key has video generation access

### Generation fails
- Check that model is selected
- Ensure prompt is not empty (text-to-video)
- Verify image is uploaded (image-to-video)
- Check network connection
- Try shorter duration or lower resolution

### Video not playing
- Ensure browser supports HTML5 video
- Try downloading and playing locally
- Check video format compatibility

### API endpoint not found (404)
- Venice API may not support /videos/generations endpoint yet
- Check Venice AI documentation for current video API endpoints
- Contact Venice AI support for video generation access

## Important Notes

**API Compatibility:**
- The video generation feature uses the `/videos/generations` endpoint
- This endpoint may vary based on Venice AI's actual implementation
- Check Venice AI's official documentation for the correct video API format
- You may need to adjust parameters based on their API specification

**Processing Time:**
- Video generation typically takes 2-10 minutes
- Longer videos take more time
- Higher resolutions increase processing time
- Be patient and don't refresh the page

**Resource Usage:**
- Video generation may consume more API credits
- Check your Venice AI usage limits
- Consider starting with shorter durations

**File Size:**
- Generated videos can be large (10-100+ MB)
- Ensure adequate storage space
- Download may take time on slow connections

## Example Workflows

### Creating a Social Media Video

1. Mode: Text to Video
2. Prompt: "Product showcase rotating on pedestal, white background, professional lighting"
3. Duration: 5 seconds
4. FPS: 30
5. Resolution: 1024x576 (16:9 for Instagram/TikTok)

### Animating a Portrait

1. Mode: Image to Video
2. Upload a portrait photo
3. Motion Prompt: "Subtle head turn, eyes blink naturally"
4. Duration: 3 seconds
5. FPS: 30

### Creating B-Roll Footage

1. Mode: Text to Video
2. Prompt: "Aerial view of a city at night, lights twinkling, slow forward movement"
3. Duration: 10 seconds
4. FPS: 24 (cinematic)
5. Resolution: 1280x720

## Future Enhancements

Potential features for future updates:
- Video editing capabilities
- Frame-by-frame control
- Multiple image keyframes
- Video upscaling
- Style transfer
- Audio generation and sync
- Batch processing
- Preset templates

## Resources

For more information about Venice AI's video capabilities:
- [Venice AI Official Site](https://venice.ai)
- [Venice API Documentation](https://docs.venice.ai)
- [Venice Community](https://discord.gg/venice) (if available)

Enjoy creating amazing videos with Venice AI! 🎥✨
