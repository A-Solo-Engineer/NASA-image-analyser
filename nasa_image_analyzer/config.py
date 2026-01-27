"""
Configuration file for NASA Image Analyzer
"""

import os
from pathlib import Path


class Config:
    """Configuration class for NASA Image Analyzer."""
    
    # NASA API Configuration
    NASA_API_KEY = os.getenv('NASA_API_KEY', 'DEMO_KEY')  # Get from environment or use demo key
    NASA_API_BASE_URL = 'https://api.nasa.gov'
    
    # Image Analysis Configuration
    IMAGE_ANALYSIS_MODEL = 'yolov8n'  # YOLOv8 nano model for fast analysis
    CONFIDENCE_THRESHOLD = 0.5
    
    # Data Collection Configuration
    MAX_IMAGES = 10  # Maximum number of images to fetch (reduced for faster testing)
    OUTPUT_DIR = Path('output')
    IMAGES_DIR = OUTPUT_DIR / 'images'
    CSV_OUTPUT_FILE = OUTPUT_DIR / 'nasa_image_data.csv'
    
    # Request Configuration
    REQUEST_TIMEOUT = 60  # Increased timeout for reliability
    RETRY_ATTEMPTS = 5  # More retries
    RETRY_DELAY = 3  # seconds
    
    # Image Download Configuration
    MIN_IMAGE_SIZE = 1000  # Minimum pixels
    MAX_IMAGE_SIZE = 10000  # Maximum pixels
    
    def __init__(self):
        """Initialize configuration and create necessary directories."""
        self.OUTPUT_DIR.mkdir(exist_ok=True)
        self.IMAGES_DIR.mkdir(exist_ok=True)
    
    @property
    def api_key(self):
        """Get NASA API key."""
        return self.NASA_API_KEY
    
    @property
    def base_url(self):
        """Get NASA API base URL."""
        return self.NASA_API_BASE_URL
