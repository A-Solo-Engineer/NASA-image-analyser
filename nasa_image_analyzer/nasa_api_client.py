"""
NASA API Client - handles communication with NASA APIs
"""

import logging
import requests
from typing import List, Dict, Any
from datetime import datetime, timedelta
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)


class NASAAPIClient:
    """Client for interacting with NASA APIs."""
    
    def __init__(self, config):
        """Initialize NASA API client."""
        self.config = config
        self.session = self._create_session()
    
    def _create_session(self) -> requests.Session:
        """Create a requests session with retry strategy."""
        session = requests.Session()
        
        retry_strategy = Retry(
            total=self.config.RETRY_ATTEMPTS,
            backoff_factor=self.config.RETRY_DELAY,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"]
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        return session
    
    def fetch_apod_images(self, count: int = 10) -> List[Dict[str, Any]]:
        """
        Fetch Astronomy Picture of the Day (APOD) images.
        
        Args:
            count: Number of images to fetch
            
        Returns:
            List of image metadata
        """
        logger.info(f"Fetching {count} APOD images from NASA API")
        
        url = f"{self.config.base_url}/planetary/apod"
        
        params = {
            'api_key': self.config.api_key,
            'count': count,
            'thumbs': True  # Request thumbnail URLs
        }
        
        try:
            response = self.session.get(
                url,
                params=params,
                timeout=self.config.REQUEST_TIMEOUT
            )
            response.raise_for_status()
            
            data = response.json()
            
            # Filter to only image entries (exclude videos)
            images = [
                img for img in data
                if img.get('media_type') == 'image' and img.get('url')
            ]
            
            logger.info(f"Retrieved {len(images)} image entries from APOD")
            return images
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch APOD images: {str(e)}")
            raise
    
    def fetch_mars_rover_images(self, rover: str = 'curiosity', count: int = 10) -> List[Dict[str, Any]]:
        """
        Fetch Mars Rover images.
        
        Args:
            rover: Rover name (curiosity, opportunity, spirit)
            count: Number of images to fetch
            
        Returns:
            List of image metadata
        """
        logger.info(f"Fetching {count} {rover} Mars Rover images")
        
        url = f"{self.config.base_url}/mars-photos/api/v1/rovers/{rover}/latest_photos"
        
        params = {
            'api_key': self.config.api_key,
            'page': 1
        }
        
        try:
            response = self.session.get(
                url,
                params=params,
                timeout=self.config.REQUEST_TIMEOUT
            )
            response.raise_for_status()
            
            data = response.json()
            photos = data.get('latest_photos', [])[:count]
            
            logger.info(f"Retrieved {len(photos)} Mars Rover images")
            return photos
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch Mars Rover images: {str(e)}")
            raise
    
    def test_connection(self) -> bool:
        """
        Test NASA API connection.
        
        Returns:
            True if connection is successful
        """
        try:
            url = f"{self.config.base_url}/planetary/apod"
            params = {'api_key': self.config.api_key, 'count': 1}
            
            response = self.session.get(
                url,
                params=params,
                timeout=self.config.REQUEST_TIMEOUT
            )
            response.raise_for_status()
            
            logger.info("NASA API connection successful")
            return True
            
        except requests.exceptions.RequestException as e:
            logger.error(f"NASA API connection failed: {str(e)}")
            return False
