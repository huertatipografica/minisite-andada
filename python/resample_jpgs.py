#!/usr/bin/env python3
"""
JPG Resampler
Resamples all JPG images in a specified folder to a maximum width while maintaining aspect ratio.
Applies quality compression and replaces the original files.
"""

from PIL import Image
import os
import glob

def resample_jpgs(folder_path, target_width=1920, quality=80):
    """
    Resample all JPG images in the specified folder.

    Args:
        folder_path: Path to the folder containing JPG images
        target_width: Target width in pixels (default: 1920)
        quality: JPEG quality 0-100 (default: 80)
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist")
        return

    processed_count = 0
    failed_files = []

    # Find all JPG files (case-insensitive)
    jpg_files = (glob.glob(os.path.join(folder_path, "*.jpg")) +
                 glob.glob(os.path.join(folder_path, "*.jpeg")) +
                 glob.glob(os.path.join(folder_path, "*.JPG")) +
                 glob.glob(os.path.join(folder_path, "*.JPEG")))

    print(f"Found {len(jpg_files)} JPG files in '{folder_path}'")
    print(f"Settings: Target width = {target_width}px, Quality = {quality}%\n")

    for jpg_path in jpg_files:
        try:
            # Open the image
            img = Image.open(jpg_path)
            original_width, original_height = img.size

            # Preserve ICC color profile and EXIF data
            icc_profile = img.info.get('icc_profile')
            exif = img.info.get('exif')

            # Only resize if image is larger than target width
            if original_width > target_width:
                aspect_ratio = original_height / original_width
                new_height = int(target_width * aspect_ratio)
                img_resized = img.resize((target_width, new_height), Image.LANCZOS)
                resized = True
            else:
                img_resized = img
                new_height = original_height
                resized = False

            # Convert to RGB if necessary (removes alpha channel)
            if img_resized.mode in ('RGBA', 'LA', 'P'):
                rgb_img = Image.new('RGB', img_resized.size, (255, 255, 255))
                if img_resized.mode == 'P':
                    img_resized = img_resized.convert('RGBA')
                rgb_img.paste(img_resized, mask=img_resized.split()[-1] if img_resized.mode in ('RGBA', 'LA') else None)
                img_resized = rgb_img
            elif img_resized.mode != 'RGB':
                img_resized = img_resized.convert('RGB')

            # Save with specified quality, preserving color profile
            save_kwargs = {'quality': quality, 'optimize': True, 'dpi': (72, 72), 'subsampling': 0}
            if icc_profile:
                save_kwargs['icc_profile'] = icc_profile
            if exif:
                save_kwargs['exif'] = exif
            img_resized.save(jpg_path, 'JPEG', **save_kwargs)

            processed_count += 1
            if resized:
                print(f"✓ Resampled: {os.path.basename(jpg_path)} ({original_width}x{original_height} → {target_width}x{new_height})")
            else:
                print(f"✓ Recompressed: {os.path.basename(jpg_path)} ({original_width}x{original_height}, kept size)")

        except Exception as e:
            failed_files.append((os.path.basename(jpg_path), str(e)))
            print(f"✗ Failed: {os.path.basename(jpg_path)} - {str(e)}")

    print(f"\n=== Resampling Complete ===")
    print(f"Processed: {processed_count} files")
    if failed_files:
        print(f"Failed: {len(failed_files)} files")
        for filename, error in failed_files:
            print(f"  - {filename}: {error}")

    return processed_count, failed_files


if __name__ == "__main__":
    import sys

    # Default to 'uso' folder relative to script location
    if len(sys.argv) > 1:
        target_folder = sys.argv[1]
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        target_folder = os.path.join(os.path.dirname(script_dir), "uso")

    # Optional: custom width and quality
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 1920
    quality = int(sys.argv[3]) if len(sys.argv) > 3 else 80

    resample_jpgs(target_folder, width, quality)
