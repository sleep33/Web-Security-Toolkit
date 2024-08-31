import ssl
import socket

def get_ssl_expiry_date(hostname):
    context = ssl.create_default_context()
    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    
    # 3-second timeout
    conn.settimeout(3.0)
    
    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    return ssl_info['notAfter']

if __name__ == "__main__":
    hostname = "example.com"
    expiry_date = get_ssl_expiry_date(hostname)
    print(f"SSL certificate for {hostname} expires on {expiry_date}")
