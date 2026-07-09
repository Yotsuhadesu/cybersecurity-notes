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
- This command will show the target machine's listening ports/services, their versions, and vulnerabilities while showing the current process by line.

Determine how many ports under 1000 are open and what is the machine vulnerable to.
