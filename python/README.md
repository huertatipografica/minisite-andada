# Python Image Conversion Tools

This directory contains Python scripts for image conversion and processing.

## Scripts

### convert_to_gif.py
Converts all JPG and PNG images in a folder to GIF format.

**Usage:**
```bash
python python/convert_to_gif.py [folder_path]
```
If no folder is specified, converts images in the python directory.

### resample_jpgs.py
Resamples JPG images to a maximum width whilst maintaining aspect ratio.

**Usage:**
```bash
python python/resample_jpgs.py [folder_path] [width] [quality]
```
- `folder_path`: Target folder (defaults to `../uso`)
- `width`: Maximum width in pixels (default: 1920)
- `quality`: JPEG quality 0-100 (default: 80)

## Setup

### 1. Create Virtual Environment

**On macOS/Linux:**
```bash
./setup_venv.sh
```

**On Windows:**
```cmd
setup_venv.bat
```

**Manual setup:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate.bat
pip install -r requirements.txt
```

### 2. Activate Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```cmd
venv\Scripts\activate.bat
```

### 3. Run Scripts

Once the virtual environment is activated, you can run the scripts:

```bash
# Convert images to GIF
python python/convert_to_gif.py /path/to/images

# Resample JPGs
python python/resample_jpgs.py /path/to/images 1920 80
```

### 4. Deactivate Virtual Environment

When you're finished:
```bash
deactivate
```

## Dependencies

- **Pillow** (>=10.0.0) - Python Imaging Library for image processing

All dependencies are listed in `requirements.txt` and will be installed automatically by the setup scripts.
