# NASA Image Archive Analyzer

An automated tool to fetch images from NASA archives, analyze them for scientific data, and export findings to CSV format.

## Features

- **Automatic Image Fetching**: Retrieves images from NASA's public APIs (APOD - Astronomy Picture of the Day)
- **Image Analysis**: Performs automated analysis on downloaded images including:
  - Image dimensions and file size
  - Color analysis (mean RGB values)
  - Brightness detection and categorization
  - Scientific keyword extraction from descriptions
- **Data Export**: Stores all analysis results in structured CSV format
- **Error Handling**: Robust error handling with retry logic and detailed logging
- **Extensible Design**: Easy to add new data sources and analysis methods

## Setup

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd nasa_image_analyzer
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

### NASA API Key Setup

You'll need a NASA API key to use this tool. 

1. Get a free API key from: https://api.nasa.gov/
2. Set the API key in one of these ways:

   **Option A: Environment Variable (Recommended)**
   ```bash
   # On Windows (PowerShell)
   $env:NASA_API_KEY = "your_api_key_here"
   
   # On Windows (Command Prompt)
   set NASA_API_KEY=your_api_key_here
   
   # On macOS/Linux
   export NASA_API_KEY="your_api_key_here"
   ```

   **Option B: Create .env file**
   Create a `.env` file in the project directory:
   ```
   NASA_API_KEY=your_api_key_here
   ```

3. For testing, the tool can use the demo key 'DEMO_KEY', but it has rate limits.

## Usage

### Basic Usage

Run the analyzer:

```bash
python main.py
```

This will:
1. Fetch images from NASA's APOD (Astronomy Picture of the Day)
2. Download and analyze each image
3. Extract scientific data from descriptions
4. Save all results to `output/nasa_image_data.csv`

### Output

The tool creates an `output/` directory containing:
- `nasa_image_data.csv` - Main data export with analysis results
- `images/` - Folder containing downloaded images

### CSV Output Format

The CSV file includes the following columns:

| Column | Description |
|--------|-------------|
| title | Image title |
| date | Publication date |
| explanation | Scientific explanation |
| image_file | Downloaded image filename |
| image_url | Original image URL |
| image_width | Image width in pixels |
| image_height | Image height in pixels |
| brightness | Average brightness value (0-255) |
| brightness_category | Brightness classification (Dark/Medium/Bright) |
| mean_red/green/blue | Average color channel values |
| detected_keywords | Scientific keywords found in description |
| source | Copyright/source information |
| has_hd_version | Whether HD version is available |
| analysis_timestamp | When the analysis was performed |

## Configuration

Edit `config.py` to customize:

```python
MAX_IMAGES = 100              # Number of images to fetch
IMAGE_ANALYSIS_MODEL = 'yolov8n'  # Model for analysis
CONFIDENCE_THRESHOLD = 0.5    # Detection confidence
REQUEST_TIMEOUT = 30          # API request timeout (seconds)
RETRY_ATTEMPTS = 3            # Number of retry attempts
```

## Logging

All operations are logged to:
- **Console**: Real-time output
- **File**: `nasa_analyzer.log`

## Supported NASA Data Sources

- **APOD** (Astronomy Picture of the Day) - Currently enabled
- **Mars Rover Images** - Available via `nasa_api_client.fetch_mars_rover_images()`
- **NEO API** - Can be extended
- **Exoplanet Data** - Can be extended

## Extending the Tool

### Add a New Data Source

1. Add a new fetch method in `nasa_api_client.py`
2. Call it from `NASAImageAnalyzer.fetch_images()`
3. The analyzer will automatically process results

### Add Custom Analysis

1. Modify `image_analyzer.py` to add analysis methods
2. Add new columns to output via `_perform_image_analysis()`
3. Results automatically included in CSV export

## Troubleshooting

### "No module named 'requests'"
```bash
pip install -r requirements.txt
```

### API Key errors
- Verify your API key is set correctly
- Check that the key is active on https://api.nasa.gov/
- Try regenerating your API key

### Image download failures
- Check internet connection
- Verify NASA APIs are accessible
- Check logs in `nasa_analyzer.log`

### "Permission denied" errors
- Ensure you have write permissions in the project directory
- Try running from a directory where you have full permissions

## Performance Notes

- First run will be slower as it downloads all images
- Subsequent runs will skip already-downloaded images
- Use `MAX_IMAGES` in config to limit processing time
- Image analysis requires PIL/Pillow - install via requirements

## License

This project uses NASA's public APIs which are free to use under the terms outlined at: https://api.nasa.gov/

## Support

For issues with:
- **NASA APIs**: Visit https://api.nasa.gov/
- **This tool**: Check logs and error messages for details

## Next Steps

1. Get your free NASA API key from https://api.nasa.gov/
2. Set the NASA_API_KEY environment variable
3. Run `python main.py`
4. Check `output/nasa_image_data.csv` for results

Happy exploring! 🚀
