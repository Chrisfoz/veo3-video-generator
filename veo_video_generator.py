#!/usr/bin/env python3
"""
Veo Video Generation Script

This script uses Google's Veo 3.0 model to generate videos from text prompts.
It demonstrates dialogue scene generation with proper error handling and logging.

Requirements:
- Google GenAI library
- Valid Google AI API credentials

Author: Your Name
Date: 2025-08-14
"""

import time
import logging
import os
import sys
from pathlib import Path
from google import genai

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('video_generation.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)


class VeoVideoGenerator:
    """A class to handle Veo video generation operations."""
    
    def __init__(self, api_key=None):
        """
        Initialize the Veo video generator.
        
        Args:
            api_key (str, optional): Google AI API key. If not provided,
                                   will attempt to use environment variable.
        """
        if api_key:
            genai.configure(api_key=api_key)
        elif os.getenv('GOOGLE_AI_API_KEY'):
            genai.configure(api_key=os.getenv('GOOGLE_AI_API_KEY'))
        else:
            logger.error("No API key provided. Set GOOGLE_AI_API_KEY environment variable or pass api_key parameter.")
            sys.exit(1)
            
        self.client = genai.Client()
        logger.info("Veo Video Generator initialized successfully")
    
    def generate_video(self, prompt, output_filename="generated_video.mp4", poll_interval=10):
        """
        Generate a video from a text prompt.
        
        Args:
            prompt (str): The text prompt for video generation
            output_filename (str): Name of the output video file
            poll_interval (int): Polling interval in seconds
            
        Returns:
            str: Path to the generated video file
        """
        try:
            logger.info(f"Starting video generation with prompt: '{prompt[:50]}...'")
            
            # Start the generation job
            operation = self.client.models.generate_videos(
                model="veo-3.0-generate-preview",
                prompt=prompt,
            )
            
            logger.info(f"Generation job started. Operation ID: {operation.name}")
            
            # Poll for the result
            while not operation.done:
                logger.info("Waiting for video generation to complete...")
                time.sleep(poll_interval)
                operation = self.client.operations.get(operation)
            
            # Check if operation completed successfully
            if hasattr(operation, 'error') and operation.error:
                logger.error(f"Video generation failed: {operation.error}")
                return None
            
            # Download the final video
            video = operation.response.generated_videos[0]
            output_path = Path(output_filename)
            video.video.save(str(output_path))
            
            logger.info(f"Generated video saved to {output_path.absolute()}")
            return str(output_path.absolute())
            
        except Exception as e:
            logger.error(f"Error during video generation: {str(e)}")
            return None


def main():
    """Main function to demonstrate video generation."""
    
    # Define the prompt for dialogue scene
    prompt = """A close up of two people staring at a cryptic drawing on a wall, torchlight flickering.
A man murmurs, 'This must be it. That's the secret code.' The woman looks at him and whispering excitedly, 'What did you find?'"""
    
    # Initialize the video generator
    generator = VeoVideoGenerator()
    
    # Generate the video
    output_file = generator.generate_video(
        prompt=prompt,
        output_filename="dialogue_example.mp4",
        poll_interval=10
    )
    
    if output_file:
        logger.info(f"Video generation completed successfully: {output_file}")
        print(f"\n✅ Success! Your video has been saved to: {output_file}")
    else:
        logger.error("Video generation failed")
        print("\n❌ Video generation failed. Check the logs for more details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
