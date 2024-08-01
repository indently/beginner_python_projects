# 1. Import necessary functionality
import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict


# 2. Create a function that checks the status of any URL
def check_status(url: str) -> None:
    try:
        response: Response = requests.get(url)

        # 3. Extract information from the response
        status_code: int = response.status_code
        headers: CaseInsensitiveDict[str] = response.headers
        content_type: str = headers.get('Content-Type', 'Unknown')
        server: str = headers.get('Server', 'Unknown')
        response_time: float = response.elapsed.total_seconds()

        # 4. Display the information regarding the URL
        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time:.2f} seconds')
    except RequestException as e:
        print(f'ERROR: {e}')


# 5. Create a main entry point
def main() -> None:
    url_to_check: str = 'https://www.indently.io'
    check_status(url_to_check)


# 6. Run the script
if __name__ == '__main__':
    main()
