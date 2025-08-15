# Veo3 Video Generator

A Python script for generating videos using Google's Veo 3.0 model with text prompts.

## Features

- Generate videos from text descriptions using Google's Veo 3.0 model
- Comprehensive error handling and logging
- Configurable polling intervals for generation status
- Support for environment variable or direct API key configuration
- Example dialogue scene generation

## Requirements

- Python 3.7+
- Google GenAI library
- Valid Google AI API credentials

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Chrisfoz/veo3-video-generator.git
cd veo3-video-generator
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your Google AI API key:
```bash
export GOOGLE_AI_API_KEY="your_api_key_here"
```

Or pass it directly when initializing the `VeoVideoGenerator` class.

## Usage

### Basic Usage

```python
from veo_video_generator import VeoVideoGenerator

# Initialize the generator
generator = VeoVideoGenerator()

# Generate a video
prompt = "A serene sunset over a calm lake with birds flying in the distance"
output_file = generator.generate_video(
    prompt=prompt,
    output_filename="sunset_video.mp4",
    poll_interval=10
)

if output_file:
    print(f"Video saved to: {output_file}")
```

### Running the Example

```bash
python veo_video_generator.py
```

This will generate a dialogue scene video using the predefined prompt.

## Configuration

### API Key Setup

You can configure your API key in several ways:

1. **Environment Variable** (Recommended):
   ```bash
   export GOOGLE_AI_API_KEY="your_api_key_here"
   ```

2. **Direct Parameter**:
   ```python
   generator = VeoVideoGenerator(api_key="your_api_key_here")
   ```

### Logging

The script logs both to console and to a file (`video_generation.log`). You can adjust the logging level in the script configuration.

## Example Prompts

Here are some example prompts that work well with Veo 3.0:

- **Dialogue Scene**: "Two people having a conversation in a cozy coffee shop, warm lighting, steam rising from coffee cups"
- **Nature Scene**: "A majestic eagle soaring over snow-capped mountains during golden hour"
- **Urban Scene**: "Busy city street at night with neon lights reflecting on wet pavement"
- **Fantasy Scene**: "A magical forest with glowing mushrooms and fireflies dancing in the twilight"

## Error Handling

The script includes comprehensive error handling:

- API key validation
- Network connectivity issues
- Generation timeout handling
- File saving errors

All errors are logged with timestamps for easy debugging.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This project uses Google's Veo 3.0 model. Please ensure you comply with Google's usage policies and terms of service when using this tool.
