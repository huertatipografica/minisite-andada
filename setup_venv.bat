@echo off
REM Virtual Environment Setup Script for Image Conversion Tools (Windows)

echo Setting up virtual environment for Python image conversion scripts...

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install requirements
pip install -r requirements.txt

echo.
echo Virtual environment setup complete!
echo.
echo To activate the virtual environment, run:
echo   venv\Scripts\activate.bat
echo.
echo To run the scripts:
echo   python python\convert_to_gif.py [folder_path]
echo   python python\resample_jpgs.py [folder_path] [width] [quality]
echo.
echo To deactivate the virtual environment when done:
echo   deactivate
