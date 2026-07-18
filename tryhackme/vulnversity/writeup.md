# Vulnversity

## Introduction
"Learn about active recon, web app attacks and privilege escalation."

## Tasks
1. Reconnaissance
2. Locate directories using Gobuster
3. Compromise the Webserver
4. Privilege Escalation

## Walktrough

### Reconnaissance 
Command: `nmap -Pn -sV [target IP]`
- Scans for open ports and listening services and their versions without the ping scan (host discovery)

----

### Locate directories using Gobuster
Command: `gobuster dir -u http://[target IP]:[target port] -w /usr/share/wordlists/dirb/common.txt`
- Gobuster - a tool for reconnasissance and ethical hacking that is used for force browsing website's directories in this case
- `gobuster dir` - a command for finding a website's hidden directories and files
- `-u` - target URL specification
- `-w` - wordlist file to be used
- `/usr/share/wordlists/dirb/common.txt` - a relatively small but effective list of directory names

---

### Compromise the Webserver
Tool: Burp Suite - used for web traffic interception and manipulation

1. Open Burp Suite and its browser
2. Enter the website's URL with its hidden directory
3. Turn the `Intercept` traffic on on Burp Suite
4. Upload a php file
5. Forward the traffic on `Intruder`
6. On Payloads, select `Sniper attack`
7. Create a text file with the following content:
    - `php`
    - `php3`
    - `php4`
    - `php5`
    - `phtml`
