#!/usr/bin/env python3

import socket
import sys
  
  
def scan_ports(host, start_port, end_port):
    print(f"\n[~] Scanning {host} from port {start_port} to {end_port}...\n")

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f"[+] Port {port} is OPEN")
    except KeyboardInterrupt:
        print("\n[!] Scan cancelled by user (Ctrl+C).")
    except socket.gaierror:
        print(f"[!] Oops! Couldn’t resolve host: {host}")
    except Exception as e:
        print(f"[!] Something went wrong: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python port-scanner.py <host> <start_port> <end_port>")
        return

    host = sys.argv[1]

    try:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
        if start_port > end_port or start_port < 0 or end_port > 65535:
            print("[!] Invalid port range. Please choose between 0 and 65535.")
            return
    except ValueError:
        print("[!] Please enter valid numbers for ports.")
        return

    scan_ports(host, start_port, end_port)

if __name__ == "__main__":
    main()
