# Summary

## Learnings

### Terms
- Scanning - identifying if a host is alive and its open ports
- Enumeration - extracting information from the services listening on ports
- Host Discovery - identifying live host(s) on a network
- Common Vulnerabilities and Exposures (CVEs) - a catalog for publicly disclosed software and hardware flaws 

### Commands
- `nmap [IP Address]` - full TCP scan, identifies live hosts and open ports
- `nmap -sV [IP Address]` - service/version scan, identifies services and their versions
- `nmap -sV --intensity-version [0-9] [IP Address]` - adjusts how thoroughly Nmap does the version scan
- `nmap -sC [IP Address]` - default script scan, Nmap performs scripts under default category against the target to extract information
- `nmap -sn [IP Address]` - ping scan, sends ICMP echo requests to identify live hosts
- `nmap -PR -sn [IP Address]` - ARP sweep, sends ARP broadcast requests to map a local network


### Technicalities
- Use full TCP scan to scan if the target is alive and to what ports it listens.
- Use service/version scan to identify the services and their version, which can be used to search for CVEs.
- Use default script scan to search for key details about the services that the target is using.
- Use ping scan for fast host discovery. However, ICMP echo requests can be blocked by firewalls.
- Use ARP sweep for accurate host discovery on a local network.
- ARP sweep switches back to ICMP ping scan if it is used on a remote network.

### Reflections
- After weeks of rest, this is a great start. I've enjoyed doing this more than I thought. 
- I didn't expect that all 256 hosts of scanme.nmap.org's network are up.
- I need to look for CVEs on every service that has the potential to be exploited.
