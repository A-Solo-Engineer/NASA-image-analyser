# Contributing to NASA Image Analyzer

Thank you for your interest in contributing! We welcome contributions of all kinds.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/nasa-image-analyzer.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Install dependencies: `pip install -r requirements.txt`

## Development Setup

```bash
# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up your NASA API key
export NASA_API_KEY="your_key_here"  # macOS/Linux
# or
set NASA_API_KEY=your_key_here  # Windows Command Prompt
```

## Making Changes

1. Make your changes in your feature branch
2. Test your changes: `python -m pytest` (when tests are available)
3. Ensure your code follows PEP 8 style guidelines
4. Add meaningful commit messages

## Submitting a Pull Request

1. Push to your fork: `git push origin feature/your-feature-name`
2. Open a Pull Request on GitHub
3. Describe your changes clearly in the PR description
4. Link any related issues

## Guidelines

- Keep commits atomic and well-documented
- Include comments for complex logic
- Update documentation if you change functionality
- Test your changes before submitting

## Code Standards

- Follow PEP 8 style guide
- Use descriptive variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular

## Reporting Bugs

1. Check if the bug has already been reported
2. Include steps to reproduce
3. Provide details about your environment (OS, Python version, etc.)
4. Include error messages and logs

## Feature Requests

1. Check if the feature has been requested
2. Describe the use case and expected behavior
3. Provide examples if possible

## Questions?

Feel free to open an issue for questions or discussions!

Thank you for contributing!
