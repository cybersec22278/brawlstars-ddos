# BrawlStars Servers Crash API Script

This script sends an attack to the Brawl Stars server using the [EpicStresser](https://epicstresser.net/) API.

## 1. How to Get API Access from EpicStresser

1. Go to [EpicStresser](https://epicstresser.net/).
2. Register and log into your account.
3. Add funds and purchase API access.
4. Navigate to the API section and copy your **API Token**.
5. Paste the token into the `API_TOKEN` variable in the script.

## 2. How to Find Brawl Stars Server IP on Android

### Method 1: Using Termux

1. Install **Termux** from Google Play.
2. Open **Termux** and enter the following command:
   ```bash
   netstat -anp | grep brawlstars
   ```
3. Look for the line containing the Brawl Stars server IP address.

### Method 2: Using Wireshark (Requires a PC)

1. Enable Developer Mode on your phone.
2. Enable USB Tethering and connect your phone to the PC.
3. Open **Wireshark** and select the Android network interface.
4. Filter traffic by `brawlstars` or `supercell`.
5. Find the server IP address in the **Destination** column.

## 3. How to Use the Script

### Configuration

1. Open the script and paste your API token into `API_TOKEN`.
2. Specify the attack method in `ATTACK_METHOD`.

### Launching an Attack

```bash
python3 script.py <IP> <PORT> <TIME>
```

- **IP** – Brawl Stars server IP address.
- **PORT** – Server port (usually `9339`).
- **TIME** – Attack duration in seconds.

### Example

```bash
python3 script.py 123.456.78.90 9339 60
```

This command will send a 60-second attack to the server.

---

🚨 **Warning!** Using this script for DDoS attacks is illegal. It is intended for educational and testing purposes only.

