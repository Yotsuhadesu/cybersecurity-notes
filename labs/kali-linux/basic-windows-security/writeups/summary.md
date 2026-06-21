# Basic Windows Security Learning Summary

## Topics
- User, Filesystem, and Privileges
- Events and Services

## Commands
- `whoami /all` - show user, groups, and privileges information
- `net user [username]` - show specific user account details
- `net localgroup administrators` - show groups who has administrator-level privileges
- `icacls [directory/file]` - show permission settings for the directory of file
- `netsh advfirewall firewall show rule name=all dir=in` - show all firewall rules from programs going in the machine

## Terms
- NTFS - New Technology File System, file system for Windows that uses ACL
- ACL - Access Control List, uses specific letter(s) to show permission settings
- Windows Account Types:
  1. Local Account - account in the specific machine, stored in SAM
  2. Domain Account - account that can be opened in any machine, stored in AD
  3. Special Accounts
     1. Administrator 
     2. Guest - account with the least privileges, cannot make changes in the machine
     3. System - account with the most privileges, used by the OS
- SAM
  - Security Account Manager, stores the usernames and passwords of local users
  - Location: `C:\Windows\System32\config\SAM`
- AD - Active Directory, a database for domain accounts
- UAC - User Account Control, a confirmation popup for privilege escalation
- HKLM - Hive Key Local Machine, rules for all users in a machine
- HKCU - Hive Key Current User, rules for the current user
- Event - process that happened in the machine
- Key Event IDs:
  1. 4624 - successful logon
  2. 4625 - logon failure
- Logon Types:
  1. 5 - service logon
  2. 7 - a user unlocked the machine with a password
  3. 11 - a user with Microsoft Account logged on
- Service - a process in the background
- Firewall - a security tool that can block connections
  
## Tools
- eventvwr.msc - an Event Viewer, shows event logs
- services.msc -  show services
- regedit - Registry Editor
