import requests
import sys
from urllib3.exceptions import InsecureRequestWarning

def check_url_status(url, verify_ssl=True):
    try:
        # Suppress only the InsecureRequestWarning
        requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, timeout=10, verify=verify_ssl, headers=headers)
        
        if response.status_code == 200:
            if "CF-Ray" in response.headers:
                print(f"{url} is online, but protected by Cloudflare.")
            elif "captcha" in response.text.lower():
                print(f"{url} is online, but may be presenting a CAPTCHA.")
            else:
                print(f"{url} is online!")
            return True
        elif response.status_code == 403:
            print(f"{url} is blocking our request. This might be due to Cloudflare or other protection.")
            return False
        else:
            print(f"{url} is not accessible. Status code: {response.status_code}")
            return False

    except requests.exceptions.SSLError as e:
        print(f"SSL Error occurred with {url}: {e}")
        print("Attempting to connect without SSL verification...")
        return check_url_status(url, verify_ssl=False)
    except requests.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python url_checker.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    check_url_status(url)
