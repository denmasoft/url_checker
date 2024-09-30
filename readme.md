# URL Status Checker

This project provides a simple Python script to check the status of a given URL. It can detect if a website is online, protected by Cloudflare, or potentially presenting a CAPTCHA.

## Features

- Check if a URL is accessible
- Detect Cloudflare protection
- Identify potential CAPTCHA challenges
- Handle SSL certificate errors
- Custom User-Agent to mimic a real browser

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/denmasoft/url-checker.git
   cd url-checker
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line, providing a URL as an argument:

```
python src/url_checker.py https://example.com
```

## Output

The script will print one of the following messages:

- "{url} is online!"
- "{url} is online, but protected by Cloudflare."
- "{url} is online, but may be presenting a CAPTCHA."
- "{url} is blocking our request. This might be due to Cloudflare or other protection."
- "{url} is not accessible. Status code: {status_code}"

In case of errors (e.g., network issues, SSL problems), appropriate error messages will be displayed.

## Limitations

- This script cannot bypass Cloudflare protection or solve CAPTCHAs.
- It may not detect all types of website protection mechanisms.
- Automated access to websites may violate their terms of service. Always ensure you have permission to access a website in an automated manner.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
