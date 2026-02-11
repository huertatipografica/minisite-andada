#!/usr/bin/env python3
"""
Image to GIF Converter
Converts all JPG and PNG images in a folder to GIF format with the same names.
"""

from PIL import Image
import os
import glob

def convert_images_to_gif(folder_path=None):
    """
    Convert all JPG and PNG images in the specified folder to GIF format.

    Args:
        folder_path: Path to the folder containing images.
                    If None, uses the current directory.
    """
    if folder_path is None:
        folder_path = os.path.dirname(os.path.abspath(__file__))

    converted_count = 0
    failed_files = []

    # Find all jpg and png files (case-insensitive)
    image_files = (glob.glob(os.path.join(folder_path, "*.jpg")) +
                   glob.glob(os.path.join(folder_path, "*.png")) +
                   glob.glob(os.path.join(folder_path, "*.JPG")) +
                   glob.glob(os.path.join(folder_path, "*.PNG")))

    print(f"Found {len(image_files)} image files to convert")

    for image_path in image_files:
        try:
            # Get the base name without extension
            base_name = os.path.splitext(image_path)[0]
            gif_path = base_name + ".gif"

            # Open and convert the image
            img = Image.open(image_path)

            # Convert RGBA to RGB if necessary (GIF doesn't support RGBA)
            if img.mode == 'RGBA':
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[3])
                img = rgb_img
            elif img.mode != 'RGB' and img.mode != 'P':
                img = img.convert('RGB')

            # Save as GIF
            img.save(gif_path, 'GIF')
            converted_count += 1
            print(f"✓ Converted: {os.path.basename(image_path)} → {os.path.basename(gif_path)}")

        except Exception as e:
            failed_files.append((os.path.basename(image_path), str(e)))
            print(f"✗ Failed: {os.path.basename(image_path)} - {str(e)}")

    print(f"\n=== Conversion Complete ===")
    print(f"Successfully converted: {converted_count} files")
    if failed_files:
        print(f"Failed: {len(failed_files)} files")
        for filename, error in failed_files:
            print(f"  - {filename}: {error}")

    return converted_count, failed_files


if __name__ == "__main__":
    import sys

    # Use provided folder path or default to script's directory
    target_folder = sys.argv[1] if len(sys.argv) > 1 else None

    convert_images_to_gif(target_folder)
