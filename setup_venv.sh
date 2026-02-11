#!/bin/bash
# Virtual Environment Setup Script for Image Conversion Tools

echo "Setting up virtual environment for Python image conversion scripts..."

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

echo ""
echo "✓ Virtual environment setup complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
echo "To run the scripts:"
echo "  python python/convert_to_gif.py [folder_path]"
echo "  python python/resample_jpgs.py [folder_path] [width] [quality]"
echo ""
echo "To deactivate the virtual environment when done:"
echo "  deactivate"
