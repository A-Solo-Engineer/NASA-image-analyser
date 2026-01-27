"""
Image Analyzer - performs automated analysis on downloaded images
"""

import logging
import requests
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
import hashlib

try:
    from PIL import Image
    import numpy as np
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

logger = logging.getLogger(__name__)


class ImageAnalyzer:
    """Analyzes downloaded images for scientific data."""
    
    def __init__(self, config):
        """Initialize image analyzer."""
        self.config = config
        self.images_dir = config.IMAGES_DIR
    
    def download_image(self, image_info: Dict[str, Any]) -> Optional[Path]:
        """
        Download image from URL.
        
        Args:
            image_info: Image metadata dictionary
            
        Returns:
            Path to downloaded image or None if failed
        """
        try:
            url = image_info.get('url') or image_info.get('img_src')
            if not url:
                logger.warning("No URL found in image info")
                return None
            
            # Generate filename from URL hash
            filename = f"{hashlib.md5(url.encode()).hexdigest()}.jpg"
            filepath = self.images_dir / filename
            
            # Skip if already downloaded
            if filepath.exists():
                logger.debug(f"Image already exists: {filepath}")
                return filepath
            
            # Download image with retries
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    response = requests.get(url, timeout=self.config.REQUEST_TIMEOUT)
                    response.raise_for_status()
                    
                    # Save image
                    filepath.write_bytes(response.content)
                    logger.debug(f"Downloaded image to {filepath}")
                    
                    return filepath
                    
                except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                    if attempt < max_retries - 1:
                        logger.debug(f"Download attempt {attempt + 1} failed, retrying...")
                        continue
                    else:
                        logger.warning(f"Failed to download image after {max_retries} attempts: {str(e)}")
                        return None
            
        except Exception as e:
            logger.warning(f"Failed to download image: {str(e)}")
            return None
    
    def analyze_image(self, image_path: Path, image_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze image for scientific data.
        
        Args:
            image_path: Path to the image file (or None if download failed)
            image_info: Original image metadata
            
        Returns:
            Dictionary of analysis results
        """
        analysis_result = {
            'title': image_info.get('title', 'Unknown'),
            'date': image_info.get('date', 'Unknown'),
            'explanation': image_info.get('explanation', ''),
            'image_file': image_path.name if image_path else 'Not downloaded',
            'image_url': image_info.get('url', ''),
            'analysis_timestamp': datetime.now().isoformat(),
        }
        
        if image_path and PIL_AVAILABLE:
            try:
                # Perform image analysis
                img_analysis = self._perform_image_analysis(image_path)
                analysis_result.update(img_analysis)
            except Exception as e:
                logger.warning(f"Failed to perform image analysis: {str(e)}")
        
        # Extract scientific data from description
        scientific_data = self._extract_scientific_data(image_info)
        analysis_result.update(scientific_data)
        
        return analysis_result
    
    def _perform_image_analysis(self, image_path: Path) -> Dict[str, Any]:
        """
        Perform technical analysis on the image.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Dictionary of technical analysis results
        """
        try:
            img = Image.open(image_path)
            
            # Basic image properties
            analysis = {
                'image_width': img.width,
                'image_height': img.height,
                'image_size_pixels': img.width * img.height,
                'image_format': img.format,
                'image_mode': img.mode,
                'file_size_kb': image_path.stat().st_size / 1024,
            }
            
            # Color analysis if RGB
            if img.mode in ['RGB', 'RGBA']:
                img_array = np.array(img)
                
                # Calculate mean colors
                if img.mode == 'RGB':
                    analysis['mean_red'] = float(np.mean(img_array[:, :, 0]))
                    analysis['mean_green'] = float(np.mean(img_array[:, :, 1]))
                    analysis['mean_blue'] = float(np.mean(img_array[:, :, 2]))
                
                # Calculate brightness
                if img.mode == 'RGB':
                    brightness = np.mean(img_array)
                    analysis['brightness'] = float(brightness)
                    
                    # Classify brightness
                    if brightness < 85:
                        analysis['brightness_category'] = 'Dark'
                    elif brightness < 170:
                        analysis['brightness_category'] = 'Medium'
                    else:
                        analysis['brightness_category'] = 'Bright'
            
            return analysis
            
        except Exception as e:
            logger.warning(f"Image analysis failed: {str(e)}")
            return {}
    
    def _extract_scientific_data(self, image_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract scientific metadata from image information.
        
        Args:
            image_info: Image metadata
            
        Returns:
            Dictionary of extracted scientific data
        """
        scientific_data = {}
        
        # Extract copyright/source information
        if 'copyright' in image_info:
            scientific_data['source'] = image_info['copyright']
        
        # Check if image has HD URL
        scientific_data['has_hd_version'] = 'hdurl' in image_info
        
        # Extract keywords from explanation
        explanation = image_info.get('explanation', '')
        keywords = self._extract_keywords(explanation)
        if keywords:
            scientific_data['detected_keywords'] = ', '.join(keywords)
        
        return scientific_data
    
    def _extract_keywords(self, text: str) -> list:
        """
        Extract scientific keywords from text.
        
        Args:
            text: Text to analyze
            
        Returns:
            List of detected keywords
        """
        keywords = [
            'galaxy', 'nebula', 'supernova', 'black hole', 'planet', 'star',
            'moon', 'comet', 'asteroid', 'cosmic', 'universe', 'solar',
            'radiation', 'wavelength', 'spectrum', 'photon', 'gravity',
            'atmosphere', 'crater', 'surface', 'orbit', 'constellation'
        ]
        
        text_lower = text.lower()
        found_keywords = [kw for kw in keywords if kw in text_lower]
        
        return found_keywords
