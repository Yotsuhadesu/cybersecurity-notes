# OpenVPN
![openvpn room](screenshots/room.png)

## Objective
- Connect on a TryHackMe lab machine using a local/virtual Kali Linux machine via OpenVPN.

## Walkthrough
1. Download the OpenVPN configuration file.

![options](screenshots/openvpn-option.png)

![config file](screenshots/download-config.png)

- Copy/Move the file if it is downloaded on the host machine.

2. Download OpenVPN.
    - Commands:
        - `sudo apt install openvpn`
        - `sudo apt update && sudo apt upgrade -y` - update software
3. Use the downloaded OpenVPN configuration file.
    - Command: `sudo openvpn /path/to//file.ovpn`
    - Wait for the text `Initialization Sequence Completed` to appear.
    - Keep the window open.
4. Start the lab machine.

![lab machine](screenshots/lab-machine.png)

5. Verify the connection.
    - Command: `ping [lab machine ip]`
6. Get the flag.
    - Open browser.
    - Visit `http://10.49.186.51`.

![website](screenshots/connection-verified.png)
- The flag is under the last text.
