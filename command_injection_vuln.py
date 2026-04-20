# command_injection_vuln.py
import os

def ping_host(host):
    # Vulnerable to command injection
    command = f"ping -c 1 {host}"
    os.system(command)

if __name__ == "__main__":
    target = input("Enter host to ping: ")
    ping_host(target)
