"""
Getting Started Guide - NASA Image Analyzer
Step-by-step instructions to get up and running
"""

# SETUP INSTRUCTIONS

# STEP 1: Get Your NASA API Key
# =============================
# 1. Open your browser and go to: https://api.nasa.gov/
# 2. Click "Get Started" and sign up (free)
# 3. You'll receive your API key via email
# 4. Save your API key somewhere safe
#
# Example API Key (this is fake, don't use it):
#   GvB4r3nP9kT5mQ2wL8xC1vD4fG7hJ9sK0nM3pR6uY
#
# The DEMO_KEY can be used for testing but has rate limits


# STEP 2: Set Up Your Environment
# ================================
# Windows Command Prompt:
#   set NASA_API_KEY=your_api_key_here
#   python main.py
#
# Windows PowerShell:
#   $env:NASA_API_KEY = "your_api_key_here"
#   python main.py
#
# macOS/Linux (Bash):
#   export NASA_API_KEY="your_api_key_here"
#   python main.py


# STEP 3: Verify Setup (Optional)
# ================================
# Run the test script to verify everything is working:
#   python test_setup.py
#
# Expected output:
#   Testing imports...
#   [OK] requests
#   [OK] PIL (Pillow)
#   [OK] numpy
#   [OK] config module
#   [OK] nasa_api_client module
#   [OK] image_analyzer module
#   [OK] data_processor module
#   [SUCCESS] All dependencies installed successfully!


# STEP 4: Run the Analyzer
# ========================
# Simply execute:
#   python main.py
#
# Or on Windows, double-click:
#   run_analyzer.bat
#
# The process will:
# 1. Fetch images from NASA APOD (Astronomy Picture of the Day)
# 2. Download each image
# 3. Analyze the images for:
#    - Dimensions and file size
#    - Color values (RGB)
#    - Brightness
#    - Scientific keywords
# 4. Export all data to CSV
#
# Estimated time for 100 images: 3-5 minutes


# STEP 5: View Your Results
# ==========================
# Open the generated file:
#   output/nasa_image_data.csv
#
# In Excel or Google Sheets:
# 1. Open the CSV file
# 2. View all columns with analysis results
# 3. Filter by brightness, keywords, or date
# 4. Sort by any column
# 5. Create charts and graphs


# STEP 6: Customize (Optional)
# =============================
# Edit config.py to customize:
#
# - MAX_IMAGES: How many images to fetch (default: 100)
# - CONFIDENCE_THRESHOLD: Analysis strictness (default: 0.5)
# - REQUEST_TIMEOUT: API timeout in seconds (default: 30)
# - OUTPUT_DIR: Where to save results (default: 'output')


# STEP 7: Use Advanced Features (Optional)
# =========================================
# Run advanced examples:
#   python advanced_example.py
#
# Examples include:
# - Fetching Mars Rover images
# - Batch analysis from multiple sources
# - Custom analysis pipelines
# - Performance monitoring


# TROUBLESHOOTING
# ===============

# Q: Where is my API key?
# A: Check your NASA.gov account at https://api.nasa.gov/

# Q: Do I need the API key?
# A: Yes, but you can test with DEMO_KEY (limited requests)

# Q: How long does it take?
# A: ~100 images take 3-5 minutes depending on connection

# Q: Can I analyze my own images?
# A: Yes, modify image_analyzer.py to add your own analysis logic

# Q: Where are the images saved?
# A: In output/images/ folder (can be cleaned up anytime)

# Q: Can I run this automatically?
# A: Yes, use Windows Task Scheduler or cron jobs

# Q: What if I get an error?
# A: Check nasa_analyzer.log for details
#    Run python test_setup.py to verify setup


# DETAILED EXAMPLE - Step by Step
# ================================

# 1. Open PowerShell and navigate to project folder:
#    cd "c:\Users\Welcome\VS code project 1\nasa_image_analyzer"

# 2. Set your API key (get from https://api.nasa.gov/):
#    $env:NASA_API_KEY = "YOUR_API_KEY_HERE"

# 3. Test the setup:
#    python test_setup.py

# 4. Run the analyzer:
#    python main.py

# 5. When complete, open the CSV file:
#    output\nasa_image_data.csv

# 6. View results in Excel/Google Sheets


# UNDERSTANDING THE OUTPUT
# ========================
# The CSV file contains:
#
# Column Name              | Description
# ========================|================================================
# title                    | Image title/name
# date                     | Publication date
# explanation              | Scientific description
# image_file              | Downloaded filename
# image_url               | Original image URL
# image_width             | Width in pixels
# image_height            | Height in pixels
# image_size_pixels       | Total pixels (width × height)
# brightness              | Average brightness (0-255)
# brightness_category     | Dark / Medium / Bright
# mean_red                | Average red value (0-255)
# mean_green              | Average green value (0-255)
# mean_blue               | Average blue value (0-255)
# file_size_kb            | File size in kilobytes
# detected_keywords       | Scientific terms found
# source                  | Copyright/source info
# has_hd_version          | True if HD version available
# analysis_timestamp      | When analysis was done


# NEXT STEPS
# ==========
# 1. ✓ Read this file (you are here)
# 2. → Get API key from https://api.nasa.gov/
# 3. → Set NASA_API_KEY environment variable
# 4. → Run: python test_setup.py
# 5. → Run: python main.py
# 6. → Open: output/nasa_image_data.csv
# 7. → Analyze your NASA image data!


# GETTING HELP
# ============
# - NASA API Docs: https://api.nasa.gov/
# - Full README: See README.md in this folder
# - Quick Start: See QUICKSTART.md in this folder
# - Project Info: See PROJECT_SUMMARY.md in this folder
# - Error Logs: Check nasa_analyzer.log


# TIPS FOR SUCCESS
# ================
# 1. Start with MAX_IMAGES=10 to test quickly
# 2. Use your personal API key, not DEMO_KEY
# 3. Keep your API key secret, don't share it
# 4. Check logs (nasa_analyzer.log) for any issues
# 5. Re-run anytime to get updated data
# 6. Customize the analysis to fit your needs
# 7. Use advanced_example.py as a template


# You're all set! Happy exploring! 🚀
