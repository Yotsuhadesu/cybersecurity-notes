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
#### 1. Identify what file extension the server accepts
Tool: Burp Suite - used for web traffic interception and manipulation

1. Open Burp Suite and its browser
2. Enter the website's URL with its hidden directory
3. Turn the `Intercept` traffic on on Burp Suite
4. Upload a php file
5. Forward the traffic to `Intruder`
6. On `Payloads`, select `Sniper attack`
7. Create a text file with the following content by line:
    - `php`
    - `php3`
    - `php4`
    - `php5`
    - `phtml` 
8. Select `runtime file` and put the text file's directory.
9. On the `filename` field, click `Add §` to the extension. It should look like this: `filename="shell.§php§"`
10. Click `Start attack`
11. Look at the window that will appear after and look for an extension that has `Success` feedback in it.

#### 2. Get a Reverse Shell
