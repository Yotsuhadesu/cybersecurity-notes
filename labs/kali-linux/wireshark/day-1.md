# Wireshark - DNS Query Analysis

## Operating System
Kali Linux

## Objectives
Capture, identify, read, and inspect DNS query traffic.

--- 

## Actions Performed
1. Start capturing traffic
2. Open a website
3. Filter DNS traffic
4. Inspect DNS Query
5. Analyze DNS Response

--- 

## 1. Capture traffic

![wireshark](screenshots/day-1/wireshark-interface.png)

Steps:
- Open wireshark; either by clicking the app or typing "wireshark" on the terminal.
- Select a target: eth0 is my local machine.
- Click the blue fin at the top left corner to start capturing the traffic.

## 2. Open a website

![youtube website](screenshots/day-1/browser-website-open.png)

- I've never visited youtube, so I chose it since I'm worried that the DNS of the websites I've visited before might be cached - preventing unusual results on the DNS traffic.
  
## 3. Filter DNS traffic

![dns traffic](screenshots/day-1/wireshark-dns-traffic.png)

- Beside the blue bookmark, type dns.qry.name == "youtube.com" to filter DNS communication between my machine and youtube.
  
## 4. Query inspection

![dns query](screenshots/day-1/wireshark-dns-query.png)

Observations:
- My machine asked for 3 things:
  1. HTTPS record
  2. A - IPv4 address for youtube
  3. AAAA - IPv6 address for youtube
- I can see the website I'm trying to visit. I'm concerned of whether other people who inspected my network can see this or not.
- 10.169.13.10 is my Source IP (the client)
- 10.169.13.251 is the Destination IP (the server), which is my router acting as a DNS resolver

## 5. Response Analysis

![dns response](screenshots/day-1/wireshark-dns-response.png)

- My router returned 3 responses
  1. HTTPS record
  2. IPv4 address of the youtube server
  3. IPv6 address of the youtube server
- I can see still the website and the returned IP addresses.
