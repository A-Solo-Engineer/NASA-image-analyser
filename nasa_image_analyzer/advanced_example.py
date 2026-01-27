"""
Advanced usage example - Custom NASA image analysis pipeline
"""

import sys
from pathlib import Path
import logging

sys.path.insert(0, str(Path(__file__).parent))

from nasa_analyzer import NASAImageAnalyzer
from config import Config


def setup_logging():
    """Setup logging."""
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def custom_analysis_example():
    """
    Example: Custom analysis with specific settings
    """
    print("=" * 60)
    print("NASA Image Analyzer - Advanced Usage Example")
    print("=" * 60)
    
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        # Initialize with custom configuration
        config = Config()
        
        # You can customize config here
        # config.MAX_IMAGES = 10  # Analyze only 10 images
        # config.CONFIDENCE_THRESHOLD = 0.6  # Higher confidence threshold
        
        logger.info("Initializing NASA Image Analyzer with custom settings")
        analyzer = NASAImageAnalyzer(config)
        
        # Test API connection first
        logger.info("Testing API connection...")
        if not analyzer.api_client.test_connection():
            print("[WARNING] API test returned False - may indicate connection issues")
            print("If using DEMO_KEY, this is expected due to rate limits")
        
        # Fetch images
        print("\n1. Fetching images from NASA archive...")
        images = analyzer.fetch_images()
        print(f"   Fetched {len(images)} images")
        
        if not images:
            print("[ERROR] No images fetched!")
            return
        
        # Analyze images
        print("\n2. Analyzing images...")
        results = analyzer.analyze_images()
        print(f"   Successfully analyzed {len(results)} images")
        
        if results:
            # Show sample result
            print("\n3. Sample Analysis Result:")
            sample = results[0]
            for key, value in list(sample.items())[:5]:
                print(f"   {key}: {value}")
        
        # Export to CSV
        print("\n4. Exporting to CSV...")
        csv_file = analyzer.export_to_csv()
        print(f"   Exported to: {csv_file}")
        
        # Show summary
        print("\n5. Summary:")
        summary = analyzer.get_summary()
        for key, value in summary.items():
            print(f"   {key}: {value}")
        
        print("\n[SUCCESS] Analysis complete!")
        print(f"View results in: {csv_file}")
        
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        print(f"\n[ERROR] {str(e)}")
        sys.exit(1)


def mars_rover_example():
    """
    Example: Analyze Mars Rover images instead of APOD
    """
    print("\n" + "=" * 60)
    print("Mars Rover Image Analysis Example")
    print("=" * 60)
    
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        config = Config()
        analyzer = NASAImageAnalyzer(config)
        
        logger.info("Fetching Mars Rover images...")
        
        # Fetch Mars Rover images
        mars_images = analyzer.api_client.fetch_mars_rover_images(
            rover='curiosity',
            count=10
        )
        
        print(f"Fetched {len(mars_images)} Mars Rover images")
        
        if mars_images:
            # Process first image as example
            sample = mars_images[0]
            print("\nSample Mars Rover Image:")
            for key in ['id', 'sol', 'camera', 'earth_date']:
                if key in sample:
                    print(f"  {key}: {sample[key]}")
        
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        print(f"\n[ERROR] {str(e)}")


def batch_analysis_example():
    """
    Example: Analyze multiple sources and combine results
    """
    print("\n" + "=" * 60)
    print("Batch Analysis Example - Multiple Sources")
    print("=" * 60)
    
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        config = Config()
        analyzer = NASAImageAnalyzer(config)
        
        all_results = []
        
        # Fetch from APOD
        print("Fetching APOD images...")
        apod_images = analyzer.fetch_images()
        all_results.extend(apod_images)
        print(f"  Added {len(apod_images)} APOD images")
        
        # You could add Mars Rover or other sources here
        # mars_images = analyzer.api_client.fetch_mars_rover_images(rover='curiosity', count=5)
        # all_results.extend(mars_images)
        # print(f"  Added {len(mars_images)} Mars Rover images")
        
        print(f"\nTotal images collected: {len(all_results)}")
        
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        print(f"\n[ERROR] {str(e)}")


if __name__ == "__main__":
    # Run the main example
    custom_analysis_example()
    
    # Uncomment to run other examples:
    # mars_rover_example()
    # batch_analysis_example()
