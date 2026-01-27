"""
NASA Image Archive Analyzer
Main entry point for automated NASA image analysis and data extraction.
"""

import sys
import logging
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from nasa_analyzer import NASAImageAnalyzer
from config import Config


def setup_logging():
    """Configure logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('nasa_analyzer.log'),
            logging.StreamHandler()
        ]
    )


def main():
    """Main entry point for the NASA image analyzer."""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Starting NASA Image Analyzer")
        
        # Initialize configuration
        config = Config()
        
        # Initialize analyzer
        analyzer = NASAImageAnalyzer(config)
        
        # Run analysis
        logger.info("Fetching images from NASA archive...")
        analyzer.fetch_images()
        
        logger.info("Analyzing images...")
        analyzer.analyze_images()
        
        logger.info("Exporting data to CSV...")
        csv_file = analyzer.export_to_csv()
        
        logger.info(f"Analysis complete! Data saved to {csv_file}")
        print(f"\n[SUCCESS] Analysis complete! Results saved to: {csv_file}")
        
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}", exc_info=True)
        print(f"\n[ERROR] {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
