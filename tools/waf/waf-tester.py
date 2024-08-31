import requests

def test_waf(url):
    attacks = [
        "' OR '1'='1",   # SQL Injection
        "<script>alert('XSS')</script>",  # XSS
    ]
    
    for attack in attacks:
        response = requests.get(url, params={"input": attack})
        if response.status_code == 403:
            print(f"WAF detected for attack: {attack}")
        else:
            print(f"No WAF detected for attack: {attack}")

if __name__ == "__main__":
    url = "http://example.com"
    test_waf(url)
