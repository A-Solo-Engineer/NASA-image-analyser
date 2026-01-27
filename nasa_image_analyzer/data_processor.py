"""
Data Processor - handles data transformation and CSV preparation
"""

import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


class DataProcessor:
    """Processes and prepares data for export."""
    
    def prepare_csv_data(self, analysis_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Prepare analysis results for CSV export.
        
        Args:
            analysis_results: List of analysis result dictionaries
            
        Returns:
            Processed data ready for CSV export
        """
        csv_data = []
        
        for result in analysis_results:
            # Flatten and clean the data
            flattened = self._flatten_result(result)
            csv_data.append(flattened)
        
        logger.info(f"Prepared {len(csv_data)} records for CSV export")
        return csv_data
    
    def _flatten_result(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Flatten nested dictionaries for CSV output.
        
        Args:
            result: Result dictionary to flatten
            
        Returns:
            Flattened dictionary
        """
        flattened = {}
        
        for key, value in result.items():
            # Convert lists to strings
            if isinstance(value, list):
                flattened[key] = '; '.join(str(v) for v in value)
            # Convert dicts to JSON string
            elif isinstance(value, dict):
                flattened[key] = str(value)
            # Handle None values
            elif value is None:
                flattened[key] = ''
            # Round floats to 2 decimal places
            elif isinstance(value, float):
                flattened[key] = round(value, 2)
            else:
                flattened[key] = str(value)
        
        return flattened
    
    def get_summary_stats(self, analysis_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculate summary statistics from analysis results.
        
        Args:
            analysis_results: List of analysis results
            
        Returns:
            Dictionary of summary statistics
        """
        if not analysis_results:
            return {}
        
        stats = {
            'total_images': len(analysis_results),
            'images_with_brightness_data': sum(
                1 for r in analysis_results if 'brightness' in r
            ),
        }
        
        # Calculate average brightness if available
        brightness_values = [
            r.get('brightness') for r in analysis_results
            if r.get('brightness') is not None
        ]
        
        if brightness_values:
            stats['average_brightness'] = round(sum(brightness_values) / len(brightness_values), 2)
        
        return stats
