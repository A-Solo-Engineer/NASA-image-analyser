# Development Guide

## Project Structure

```
nasa_image_analyzer/
├── main.py                    # Entry point
├── config.py                  # Configuration management
├── nasa_api_client.py         # NASA API interactions
├── image_analyzer.py          # Image analysis logic
├── data_processor.py          # Data processing utilities
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variable template
├── output/                   # Generated output (gitignored)
│   ├── images/              # Downloaded images
│   └── nasa_image_data.csv  # Analysis results
└── tests/                    # Test files
```

## Key Components

### nasa_api_client.py
Handles all NASA API requests:
- `fetch_apod_images()` - Fetch Astronomy Picture of the Day
- `fetch_mars_rover_images()` - Fetch Mars Rover images
- Includes retry logic and error handling

### image_analyzer.py
Performs image analysis:
- Extracts image metadata (dimensions, file size)
- Calculates color statistics (mean RGB)
- Detects brightness levels
- Extracts scientific keywords

### data_processor.py
Processes and exports data:
- Structures analysis results
- Writes CSV output
- Handles data validation

### config.py
Centralized configuration:
- API settings
- Image analysis parameters
- Output paths
- Request timeouts and retry settings

## Running Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/nasa-image-analyzer.git
cd nasa_image_analyzer

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up API key
export NASA_API_KEY="your_key"  # macOS/Linux
# or
set NASA_API_KEY=your_key       # Windows

# Run the analyzer
python main.py
```

## Adding New Features

### Add a new NASA API source:

1. Add method to `nasa_api_client.py`:
```python
def fetch_new_source(self):
    """Fetch data from new source."""
    # Implementation
    return data
```

2. Call it in `main.py`
3. Handle the response in `image_analyzer.py`

### Add new analysis:

1. Add method to `image_analyzer.py`
2. Call it in the main analysis pipeline
3. Add output columns in `data_processor.py`

## Testing

Run the setup test:
```bash
python test_setup.py
```

This validates:
- All imports work correctly
- Dependencies are installed
- Configuration loads properly
- API client initializes

## Debugging

Enable verbose logging:
- Check `nasa_analyzer.log` for detailed operation logs
- All major operations log to console and file

## Performance Optimization

- Adjust `MAX_IMAGES` in config.py for faster testing
- Use smaller `IMAGE_ANALYSIS_MODEL` variants for speed
- Increase `RETRY_ATTEMPTS` for reliability
- Adjust `REQUEST_TIMEOUT` for slow connections

## Common Issues

**"No module named 'requests'"**
```bash
pip install -r requirements.txt
```

**API Key errors**
- Verify key is set: `echo $NASA_API_KEY` (macOS/Linux) or `echo %NASA_API_KEY%` (Windows)
- Check key is active on https://api.nasa.gov/

**Permission errors**
- Ensure write access to project directory
- Run from a directory where you have full permissions
