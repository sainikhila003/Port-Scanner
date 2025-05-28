import socket

def scan_port(ip, port):
    """
    Scan a specific port on the target IP address.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Set a timeout for the connection attempt

        # Attempt to connect to the port
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        else:
            print(f"Port {port} is closed on {ip}")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def scan_ports(ip, start_port, end_port):
    """
    Scan a range of ports on the target IP address.
    """
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

if __name__ == "__main__":
    # Input target IP and port range
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    # Start scanning
    scan_ports(target_ip, start_port, end_port)
