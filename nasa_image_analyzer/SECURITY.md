# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please email us instead of using the issue tracker.

**Please do not publicly disclose the vulnerability until we've had a chance to address it.**

### How to Report

1. Email your findings to the repository maintainers
2. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

3. Allow us time to investigate and patch the issue

## Security Best Practices

When using NASA Image Analyzer:

1. **API Key Management**
   - Never commit your NASA API key to the repository
   - Use environment variables or `.env` files (which are gitignored)
   - Rotate your API key if you suspect it has been compromised

2. **Dependencies**
   - Keep Python and all dependencies up to date
   - Review dependency security advisories regularly

3. **File Permissions**
   - Ensure your project directory has appropriate permissions
   - Protect your `.env` file and environment variables

4. **Data Handling**
   - Be aware that downloaded images are stored locally
   - Protect the `output/` directory if it contains sensitive data
   - Ensure compliance with NASA's terms of service

## NASA API Security

- All API requests use HTTPS
- The DEMO_KEY has rate limits; use your own key for production
- Refer to https://api.nasa.gov/ for official security guidelines

## Responsible Disclosure

We appreciate security researchers who:
- Report vulnerabilities responsibly
- Avoid unnecessary data exposure
- Give us time to patch before public disclosure
- Keep communication professional and respectful

Thank you for helping keep this project secure!
