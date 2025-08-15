#!/usr/bin/env python3
"""
Example Usage Script for Veo Video Generator

This script demonstrates various ways to use the VeoVideoGenerator class
with different types of prompts and configurations.
"""

import os
from veo_video_generator import VeoVideoGenerator


def example_dialogue_scene():
    """Generate a dialogue scene video."""
    print("\n🎬 Generating dialogue scene...")
    
    generator = VeoVideoGenerator()
    
    prompt = """Two friends sitting on a park bench at sunset, one consoling the other.
    The first person says 'Everything will be okay, you know that right?' 
    The second person nods and replies 'I hope you're right.'"""
    
    output_file = generator.generate_video(
        prompt=prompt,
        output_filename="dialogue_scene.mp4",
        poll_interval=15
    )
    
    return output_file


def example_nature_scene():
    """Generate a nature scene video."""
    print("\n🌲 Generating nature scene...")
    
    generator = VeoVideoGenerator()
    
    prompt = """A peaceful forest stream flowing over smooth rocks, 
    with sunlight filtering through tall pine trees. 
    Gentle breeze causing leaves to rustle softly."""
    
    output_file = generator.generate_video(
        prompt=prompt,
        output_filename="nature_scene.mp4",
        poll_interval=10
    )
    
    return output_file


def example_urban_scene():
    """Generate an urban scene video."""
    print("\n🏙️ Generating urban scene...")
    
    generator = VeoVideoGenerator()
    
    prompt = """A busy city intersection at rush hour, 
    with people crossing the street and cars waiting at traffic lights. 
    Neon signs reflecting on wet pavement from recent rain."""
    
    output_file = generator.generate_video(
        prompt=prompt,
        output_filename="urban_scene.mp4",
        poll_interval=12
    )
    
    return output_file


def example_fantasy_scene():
    """Generate a fantasy scene video."""
    print("\n🧙 Generating fantasy scene...")
    
    generator = VeoVideoGenerator()
    
    prompt = """A mystical wizard's tower at midnight, 
    with magical blue light emanating from the windows. 
    Glowing orbs floating around the tower, 
    and a full moon casting ethereal shadows."""
    
    output_file = generator.generate_video(
        prompt=prompt,
        output_filename="fantasy_scene.mp4",
        poll_interval=10
    )
    
    return output_file


def main():
    """Run all example scenarios."""
    print("🎥 Veo3 Video Generator - Example Usage")
    print("======================================")
    
    # Check if API key is set
    if not os.getenv('GOOGLE_AI_API_KEY'):
        print("\n❌ Error: GOOGLE_AI_API_KEY environment variable not set.")
        print("Please set your API key before running examples:")
        print("export GOOGLE_AI_API_KEY='your_api_key_here'")
        return
    
    examples = [
        ("Dialogue Scene", example_dialogue_scene),
        ("Nature Scene", example_nature_scene),
        ("Urban Scene", example_urban_scene),
        ("Fantasy Scene", example_fantasy_scene)
    ]
    
    print("\nAvailable examples:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"{i}. {name}")
    
    print("\nChoose an example to run (1-4), or 'all' to run all examples:")
    choice = input("> ").strip().lower()
    
    if choice == 'all':
        results = []
        for name, func in examples:
            print(f"\n{'='*50}")
            print(f"Running: {name}")
            print('='*50)
            result = func()
            results.append((name, result))
        
        print("\n\n📊 Summary of Results:")
        print("=" * 30)
        for name, result in results:
            status = "✅ Success" if result else "❌ Failed"
            print(f"{name}: {status}")
            if result:
                print(f"  📁 File: {result}")
    
    elif choice.isdigit() and 1 <= int(choice) <= len(examples):
        name, func = examples[int(choice) - 1]
        print(f"\nRunning: {name}")
        result = func()
        
        if result:
            print(f"\n✅ Success! Video saved to: {result}")
        else:
            print("\n❌ Video generation failed. Check the logs for details.")
    
    else:
        print("\n❌ Invalid choice. Please run the script again and choose 1-4 or 'all'.")


if __name__ == "__main__":
    main()
