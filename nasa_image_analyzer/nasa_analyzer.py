"""
Core NASA Image Analyzer - handles fetching, analyzing, and exporting data
"""

import logging
import csv
from pathlib import Path
from typing import List, Dict, Any
import json

from nasa_api_client import NASAAPIClient
from image_analyzer import ImageAnalyzer
from data_processor import DataProcessor


logger = logging.getLogger(__name__)


class NASAImageAnalyzer:
    """Main analyzer class that orchestrates image fetching and analysis."""
    
    def __init__(self, config):
        """Initialize the NASA Image Analyzer."""
        self.config = config
        self.api_client = NASAAPIClient(config)
        self.image_analyzer = ImageAnalyzer(config)
        self.data_processor = DataProcessor()
        self.image_data = []
        self.analysis_results = []
    
    def fetch_images(self) -> List[Dict[str, Any]]:
        """
        Fetch images from NASA archive.
        
        Returns:
            List of image metadata dictionaries
        """
        logger.info("Fetching images from NASA API...")
        
        try:
            # Fetch from APOD (Astronomy Picture of the Day)
            apod_images = self.api_client.fetch_apod_images(
                count=self.config.MAX_IMAGES
            )
            
            self.image_data = apod_images
            logger.info(f"Successfully fetched {len(apod_images)} images from APOD")
            
            return apod_images
            
        except Exception as e:
            logger.error(f"Failed to fetch images: {str(e)}")
            raise
    
    def analyze_images(self) -> List[Dict[str, Any]]:
        """
        Analyze fetched images for scientific data.
        
        Returns:
            List of analysis results
        """
        logger.info(f"Analyzing {len(self.image_data)} images...")
        
        self.analysis_results = []
        
        for idx, image_info in enumerate(self.image_data, 1):
            try:
                logger.info(f"Analyzing image {idx}/{len(self.image_data)}")
                
                # Download and analyze image
                image_path = self.image_analyzer.download_image(image_info)
                
                if image_path:
                    # Perform analysis
                    analysis = self.image_analyzer.analyze_image(image_path, image_info)
                    self.analysis_results.append(analysis)
                else:
                    # If download failed, still include metadata analysis
                    logger.info(f"Image download failed for image {idx}, using metadata only")
                    analysis = self.image_analyzer.analyze_image(None, image_info)
                    self.analysis_results.append(analysis)
                    
            except Exception as e:
                logger.warning(f"Failed to analyze image {idx}: {str(e)}")
                # Continue with next image even if this one fails
                try:
                    analysis = self.image_analyzer.analyze_image(None, image_info)
                    self.analysis_results.append(analysis)
                except:
                    continue
        
        logger.info(f"Completed analysis of {len(self.analysis_results)} images")
        return self.analysis_results
    
    def export_to_csv(self) -> str:
        """
        Export analysis results to CSV file.
        
        Returns:
            Path to the generated CSV file
        """
        logger.info(f"Exporting {len(self.analysis_results)} results to CSV...")
        
        if not self.analysis_results:
            logger.warning("No results to export")
            return str(self.config.CSV_OUTPUT_FILE)
        
        try:
            # Prepare data for CSV export
            csv_data = self.data_processor.prepare_csv_data(self.analysis_results)
            
            # Get fieldnames from first record
            fieldnames = csv_data[0].keys() if csv_data else []
            
            # Write to CSV
            csv_path = self.config.CSV_OUTPUT_FILE
            csv_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(csv_data)
            
            logger.info(f"Data exported successfully to {csv_path}")
            return str(csv_path)
            
        except Exception as e:
            logger.error(f"Failed to export CSV: {str(e)}")
            raise
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get summary of analysis results.
        
        Returns:
            Summary dictionary
        """
        return {
            'total_images_fetched': len(self.image_data),
            'total_images_analyzed': len(self.analysis_results),
            'output_file': str(self.config.CSV_OUTPUT_FILE)
        }
