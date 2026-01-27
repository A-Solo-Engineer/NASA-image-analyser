@echo off
REM NASA Image Analyzer - Windows Launch Script

setlocal enabledelayedexpansion

echo.
echo ================================================
echo NASA Image Analyzer
echo ================================================
echo.

REM Check if NASA_API_KEY is set
if "%NASA_API_KEY%"=="" (
    echo WARNING: NASA_API_KEY environment variable not set
    echo.
    echo Please set your API key first:
    echo   set NASA_API_KEY=your_api_key_here
    echo.
    echo Then run this script again.
    echo.
    echo Get a free API key from: https://api.nasa.gov/
    echo.
    pause
    exit /b 1
)

REM Check if venv exists
if not exist ".venv" (
    echo Virtual environment not found.
    echo Run: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Run test setup
echo Running setup test...
.venv\Scripts\python.exe test_setup.py

if %errorlevel% neq 0 (
    echo.
    echo Setup test failed. Fix errors above.
    pause
    exit /b 1
)

REM Run main analyzer
echo.
echo Starting analysis...
echo.
.venv\Scripts\python.exe main.py

if %errorlevel% neq 0 (
    echo.
    echo Analysis failed. Check the error above.
    pause
    exit /b 1
)

echo.
echo Analysis complete!
echo Results saved to: output\nasa_image_data.csv
echo.
pause
