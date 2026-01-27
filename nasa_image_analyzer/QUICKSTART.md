# Quick Start Guide - NASA Image Analyzer

## Installation (One-Time Setup)

### 1. Get NASA API Key
- Visit https://api.nasa.gov/
- Sign up for a free account
- Get your API key

### 2. Install Dependencies
```bash
cd nasa_image_analyzer
pip install -r requirements.txt
```

### 3. Set API Key (Choose One Method)

**Option A: Environment Variable (PowerShell)**
```powershell
$env:NASA_API_KEY = "your_api_key_here"
python main.py
```

**Option B: Environment Variable (Command Prompt)**
```cmd
set NASA_API_KEY=your_api_key_here
python main.py
```

**Option C: Create .env File**
Create a file named `.env` in the nasa_image_analyzer folder:
```
NASA_API_KEY=your_api_key_here
```

Then run:
```bash
python main.py
```

## Basic Usage

### 1. Test Your Setup
```bash
python test_setup.py
```

### 2. Run the Analyzer
```bash
python main.py
```

This will:
- Fetch images from NASA's APOD
- Download and analyze each image
- Extract scientific data
- Create `output/nasa_image_data.csv` with results

### 3. View Results
Open `output/nasa_image_data.csv` in Excel or your favorite spreadsheet application.

## Advanced Usage

### Custom Analysis
Edit `config.py` to customize:
```python
MAX_IMAGES = 50              # Analyze 50 images instead of 100
CONFIDENCE_THRESHOLD = 0.7   # Higher accuracy requirement
REQUEST_TIMEOUT = 60         # Longer timeout for slow connections
```

### Run Advanced Examples
```bash
python advanced_example.py
```

This includes examples for:
- Custom analysis pipeline
- Mars Rover image analysis
- Batch analysis from multiple sources

## CSV Output Columns

The generated CSV includes:

| Column | Description |
|--------|-------------|
| title | Image title/name |
| date | Publication date |
| explanation | Detailed scientific explanation |
| image_file | Downloaded image filename |
| image_url | Original image URL |
| image_width | Image width (pixels) |
| image_height | Image height (pixels) |
| image_size_pixels | Total pixel count |
| brightness | Average brightness (0-255) |
| brightness_category | Dark/Medium/Bright classification |
| mean_red | Average red channel (0-255) |
| mean_green | Average green channel (0-255) |
| mean_blue | Average blue channel (0-255) |
| file_size_kb | Image file size (KB) |
| detected_keywords | Scientific keywords found |
| source | Copyright/source attribution |
| has_hd_version | Whether HD version available |
| analysis_timestamp | When analysis was performed |

## Troubleshooting

### Problem: "No module named 'requests'"
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Problem: "NASA API key not found"
**Solution:** 
1. Get free key from https://api.nasa.gov/
2. Set NASA_API_KEY environment variable
3. Verify it's set: `echo $env:NASA_API_KEY` (PowerShell)

### Problem: "Connection timeout"
**Solution:** Increase timeout in config.py
```python
REQUEST_TIMEOUT = 60  # seconds
```

### Problem: "Permission denied" when creating output folder
**Solution:** Run from a directory where you have write permissions

### Problem: API returns rate limit error
**Solution:** 
- Use your personal API key instead of DEMO_KEY
- Wait a few minutes between requests
- Reduce MAX_IMAGES in config.py

## Features

✓ Automatic image downloading from NASA
✓ Multi-source support (APOD, Mars Rover, etc.)
✓ Image analysis (dimensions, colors, brightness)
✓ Scientific keyword extraction
✓ CSV data export
✓ Error handling and retry logic
✓ Detailed logging
✓ Extensible architecture

## Project Structure

```
nasa_image_analyzer/
├── main.py                 # Entry point
├── config.py              # Configuration
├── nasa_analyzer.py       # Main analyzer class
├── nasa_api_client.py     # NASA API communication
├── image_analyzer.py      # Image analysis engine
├── data_processor.py      # Data transformation
├── test_setup.py          # Dependency tester
├── advanced_example.py    # Usage examples
├── requirements.txt       # Python dependencies
├── README.md              # Full documentation
└── output/                # Results folder (auto-created)
    ├── images/            # Downloaded images
    └── nasa_image_data.csv # Analysis results
```

## Performance Tips

1. **Start small**: Set `MAX_IMAGES = 10` first to test
2. **Image download**: Takes 1-2 seconds per image
3. **Analysis**: Takes 0.5-1 second per image
4. **Total time**: 100 images ≈ 3-5 minutes

## Next Steps

1. ✓ Install dependencies
2. ✓ Get NASA API key
3. ✓ Run `python main.py`
4. ✓ Check `output/nasa_image_data.csv`
5. Analyze results in Excel or your data analysis tool
6. Customize analysis for your research needs

## Support

- NASA API Docs: https://api.nasa.gov/
- Image Analysis: See `image_analyzer.py` for extension points
- Data Export: See `data_processor.py` for custom export formats

Happy exploring! 🚀
