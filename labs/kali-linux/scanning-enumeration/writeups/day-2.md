# Enumeration

## Objectives
- Perform enumeration on scanme.nmap.org.
- Use service/version and safe script scan.

## Tools
- Kali Linux Virtual Machine
- nmap - a powerful tool for scanning and enumeration
- scanme.nmap.org (45.33.32.156) - a legal testing site for scanning

## Actions Performed

### 1. Version Scan
Command: nmap -sV -p 22,80 45.33.32.156
- `-sV` - service version scan/--version-intensity 7
- `-p` - scan specific ports

![default version scan](../screenshots/day-2/nmap-scan-version-default.png)

### 2. Maximum Version Scan
Command: nmap -sV --version-intensity 9 -p 22,50 45.33.32.156
- `--version-intensity` - adjusts how thoroughly Nmap does the service/version scan, from 0 as the lowest, 7 as default, and 9 as the maximum

![max version scan](../screenshots/day-2/nmap-scan-version-default.png)

### 3. Safe Script Scan
Command: nmap -sC -p 22,80 45.33.32.156
- `-sC` - tells Nmap to perform safe, default scripts on the target

![safe script scan](../screenshots/day-2/nmap-scan-script-safe.png)
