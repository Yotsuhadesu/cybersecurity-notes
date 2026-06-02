# Scanning vs Enumeration

## Objectives
- Define scanning and enumeration.
- Scan and enumerate a target.

## Tools
- Kali Linux Virtual Machine
- nmap - a powerful tool for scanning and enumeration
- nmap.scanme.org - a free testing ground for scanning

## Key Terms
1. Scanning
- checking for alive IP addresses (host discovery) and open ports
  
2. Enumeration
- asking about the services that the host is using

## Actions Performed
1. Scanning
Command: nmap 45.33.32.156
- 45.33.32.156 - IPv4 address of nmap.scanme.org (the host)
- Baseline Scan/Full TCP Scan

![scanning](../screenshots/day-1/nmap-scan-baseline.png)

Obserations:
1. The host is up.
2. 2 open ports: 22 and 80 - guessed as ssh and http.
3. 962 filtered ports - blocked by a firewall.
4. 36 closed ports - no services listening.
