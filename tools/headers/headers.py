import requests

def check_headers(url):
    response = requests.get(url)
    headers = response.headers
    
    security_headers = [
        'X-Content-Type-Options',
        'X-Frame-Options',
        'Content-Security-Policy',
        'Strict-Transport-Security'
    ]
    
    for header in security_headers:
        if header in headers:
            print(f"{header}: {headers[header]}")
        else:
            print(f"{header} is missing!")

if __name__ == "__main__":
    url = "http://example.com"
    check_headers(url)
