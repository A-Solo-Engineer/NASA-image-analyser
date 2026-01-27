"""
Test script to verify NASA Image Analyzer setup
"""

import sys
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test that all required modules are importable."""
    print("Testing imports...")
    
    try:
        import requests
        print("[OK] requests")
    except ImportError as e:
        print(f"[FAIL] requests: {e}")
        return False
    
    try:
        import PIL
        print("[OK] PIL (Pillow)")
    except ImportError as e:
        print(f"[FAIL] PIL: {e}")
        return False
    
    try:
        import numpy
        print("[OK] numpy")
    except ImportError as e:
        print(f"[FAIL] numpy: {e}")
        return False
    
    try:
        from config import Config
        print("[OK] config module")
    except ImportError as e:
        print(f"[FAIL] config: {e}")
        return False
    
    try:
        from nasa_api_client import NASAAPIClient
        print("[OK] nasa_api_client module")
    except ImportError as e:
        print(f"[FAIL] nasa_api_client: {e}")
        return False
    
    try:
        from image_analyzer import ImageAnalyzer
        print("[OK] image_analyzer module")
    except ImportError as e:
        print(f"[FAIL] image_analyzer: {e}")
        return False
    
    try:
        from data_processor import DataProcessor
        print("[OK] data_processor module")
    except ImportError as e:
        print(f"[FAIL] data_processor: {e}")
        return False
    
    return True

def test_api_connection():
    """Test connection to NASA API."""
    print("\nTesting NASA API connection...")
    
    try:
        from config import Config
        from nasa_api_client import NASAAPIClient
        
        config = Config()
        client = NASAAPIClient(config)
        
        if client.test_connection():
            print("[OK] NASA API connection successful")
            return True
        else:
            print("[WARN] NASA API connection failed")
            print("  Note: If using DEMO_KEY, this is expected due to rate limits")
            return False
            
    except Exception as e:
        print(f"[FAIL] API test error: {e}")
        return False

def main():
    """Run all tests."""
    print("=" * 50)
    print("NASA Image Analyzer - Setup Test")
    print("=" * 50)
    
    imports_ok = test_imports()
    
    if not imports_ok:
        print("\n[FAILED] Some imports failed!")
        print("Run: pip install -r requirements.txt")
        sys.exit(1)
    
    api_ok = test_api_connection()
    
    print("\n" + "=" * 50)
    if imports_ok:
        print("[SUCCESS] All dependencies installed successfully!")
        print("\nNext steps:")
        print("1. Get your NASA API key from: https://api.nasa.gov/")
        print("2. Set the NASA_API_KEY environment variable")
        print("3. Run: python main.py")
    else:
        print("[WARNING] Dependencies OK, but API key may need setup")
    print("=" * 50)

if __name__ == "__main__":
    main()
