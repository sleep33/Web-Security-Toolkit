import re

def scan_for_vulnerabilities(url):
    vulnerabilities = []
    
    # Dummy patterns for demonstration purposes
    xss_pattern = re.compile(r'<script>')
    sql_injection_pattern = re.compile(r'\' OR \'1\'=\'1')
    
    # Dummy content to simulate scanning
    content = "<html><body><script>alert('XSS')</script></body></html>"
    
    if xss_pattern.search(content):
        vulnerabilities.append('XSS detected')
        
    if sql_injection_pattern.search(content):
        vulnerabilities.append('SQL Injection detected')
    
    return vulnerabilities

if __name__ == "__main__":
    url = "http://example.com"
    results = scan_for_vulnerabilities(url)
    
    if results:
        for vuln in results:
            print(f"Vulnerability found: {vuln}")
    else:
        print("No vulnerabilities found.")
