# Pickle Rick

![pickle rick](screenshots/tryhackme_pickle_rick.png)

## Introduction
"This Rick and Morty-themed challenge requires you to exploit a web server and find three ingredients to help Rick make his potion and transform himself back into a human from a pickle."

## Machines 

![machines](screenshots/machines.png)

- Two machines: the attacker and the target

![machines information](screenshots/machines_information.png)

- Attacker's IP: `10.48.139.173`
- Target's IP: `10.48.148.236`

## Questions
1. What is the first ingredient that Rick needs?
2. What is the second ingredient in Rick’s potion?
3. What is the last and final ingredient?
- I need to look for the three ingedients in the web server and rick's account.

## Walkthrough

---

### Scan the Target
Command: `nmap -sT 10.48.148.236`
- This scan looks for open ports and completes the three-way handshake with the target.

![full scan](screenshots/nmap_full_scan.png)

Notes:
- There are two open ports: 22 and 80, presumably ssh and http services

### Scan for Versions
Command: `nmap -sV -p 22,80 10.48.148.236`

![version scan](screenshots/version_scan.png)

Note:
- The target is running a web server on http using Apache.

### Scan for Vulnerabilities
Command: `nmap -sC --script=vuln 10.48.148.236`

![vuln scan](screenshots/nmap_search_vulnerabilities.png)

![exposed files](screenshots/exposed_directories.png)

Notes:
- The scan revealed that there are two exposed files:
  1. `login.php` - a folder
  2. `robots.txt` - a critical file

### Perform HTTP Query
Command: `curl 10.48.148.236`
- This command sends a http request to the target.

![http request](screenshots/curl_http_request.png)

- In the body, there is a comment that revealed Rick's username for the web server.

![username](screenshots/http_comment_username.png)

Note:
- Username: `R1ckRul3s`

### Visit the Website 
Open the browser and enter the target's Ip in the search bar to visit Rick's Website, `Rick is sup4r cool`.

![website](screenshots/website.png)

![website2](screenshots/website_2.png)

- As Morty, I need to logon to Rick's computer and find the three ingredients to turn him back into a human again.

### Visit Exposed Files
- Go to `10.48.148.236/login.php` and `10.48.148.236/robots.txt`.

![password](screenshots/robots.txt_password.png)

- `robots.txt` contains the string `Wubbalubbadubdub`, which is likely to be Rick's password.

![login portal](screenshots/login_page.png)

- `login.php` is the login portal.

### Login
- On `login.php`'s input fields, enter:
  - Username: `R1ckRul3s`
  - Password: `Wubbalubbadubdub`
 
![command panel](screenshots/command_panel.png)

- After logging in, you'll see a command panel.

### The First Ingredient
Commands:
- `whoami` - show your username
- `pwd` - show the current working directory
- `ls` - show all the files in the current directory
- `nl [file]` - opens a text file with number lines

![username](screenshots/ls_files.png)

- I am logged in as `www-data`.

![working directory](screenshots/pwd.png)

 - After logging in, the page redirected me to `/var/www/html`.

![file list](screenshots/ls_files.png)

- There are 8 files in my current working directory.
- The first text file, `Sup3rS3cretPickl3ingred.txt` is the first ingredient.
- Run `nl Sup3rS3cretPickl3ingred.txt`

![first ingredient](screenshots/first_ingredient.png)

- First Ingredient: `mr. meeseek hair`

### Look for Users
Commands:
- `ls -la /home` - shows the user directories in a long list format

![users](screenshots/ls_users.png)

Notes: 
- two user directories:
  1. rick
  2. ubuntu
 
### The Second Ingredient
Commands:
- `ls -la /home/rick` - shows the files in rick's directory
- `nl`

![rick's directory](screenshots/ls_rick.png)

- There is the second ingredient's file.
- Run `nl /home/rick/"second ingredients"`

![second ingredient](screenshots/second_ingredient.png)

- Second Ingredient: `jerry tear`

### The Third Ingredient
Commands:
- `ls -la /home/ubuntu` - shows the files in ubuntu's directory
- `nl`

![ubuntu's directory](screenshots/ls_ubuntu.png)

- ubuntu's directory shows the exposed `.bash_history` file, which contains the commands executed by the user ubuntu.
- Open it using the command: `sudo nl /home/ubuntu/.bash_history`

![third ingredient](screenshots/third_ingredient.png)

- Third Ingredient: `fleeb juice`
