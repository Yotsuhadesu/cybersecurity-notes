# OpenVPN

## Objective
- Connect on a TryHackMe lab machine using a local/virtual Kali Linux machine via OpenVPN.

## Walkthrough
1. Download the OpenVPN configuration file.
2. Download OpenVPN.
    - Commands:
      - `sudo apt install openvpn`
      - `sudo apt update && sudo apt upgrade -y` - update software
3. Use the downloaded OpenVPN configuration file.
    - Command: `sudo openvpn /path/to//file.ovpn`
    - A text `Initialization Sequence Completed` must appear.
    - Keep the window open.
4. Start the lab machine.
5. Verify the connection.
    - Command: `ping [lab machine ip]`
6. Get the flag.
    - Open browser.
    - Visit `http://10.49.186.51`.
