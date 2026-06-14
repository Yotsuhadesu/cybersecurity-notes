# Summary

## Commands
- `ps aux` - show a snapshot of processes
- `top` - show live processes
- `ss -tulnp` -  show listening ports and services\
- `sleep [seconds]` - a process that puts itself to sleep for 5 minutes
- `PID` - process ID
- `kill [PID]` - gracefully terminate a process
- `kill -9 [PID]` - forcefully terminate a process

## Terminologies
- Process - a running program
- Service - a process on the background
- Daemons - services that are not directly controlled by the user
- Ports - a doorway where services 'listen'
- Attack Surface - an opening where an attacker can enter and mess with a system

## Technicalities
- `/etc/hosts`
  - A directory where the OS resolver checks first when you enter a URL.
  - If the domain name is found, it will immediately use the IP address beside it. 
- `/etc/resolv.conf`
  - A directory where the OS checks next if the domain name isn't on `/etc/hosts`.
  - This points to the DNS Resolver that will be used for DNS lookup.
- When exposed to an attacker, it can be edited to redirect you to a fake website or server.
- Open ports are atatck surfaces.
- Close or block unfamilliar/unused ports.  
