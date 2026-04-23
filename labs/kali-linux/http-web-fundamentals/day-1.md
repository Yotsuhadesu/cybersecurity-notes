# HTTP & Web Fundamentals

## Tools
- Kali Linux Virtual Machine
- curl
- Wireshark

## Objective
Read a full HTTP exchange without the browser summarizing it.

--- 

##  Actions Performed

---

## Wireshark
- Look at and analyze real-time http traffic.
 
1. Open an insecure website via a browser.

![http forever](screenshots/day-1/website-http-forever.png)

- HTTP Forever is an intentional insecure website.
- Use your own safe network or use VPN!

2. Capture HTTP traffic

![http filter](screenshots/day-1/wireshark-http-filter.png)

- Filter HTTP traffic

3. Follow HTTP Stream 

![http filter](screenshots/day-1/wireshark-http-get.png)

- Look for the GET / HTTP/1.1

![http filter](screenshots/day-1/wireshark-follow-http-stream.png)

- Right-click the packet, select Follow, and then HTTP Stream.

![http filter](screenshots/day-1/wireshark-http-packet.png)

- Voila! The whole HTTP communication in a window.
- After the first HTTP request header, there are encrypted-like lines of data. However, through research, I've found out that it's binary data.

4. HTTP Communication Analysis

![http filter](screenshots/day-1/wireshark-http-get-header.png)

- GET method - the client is requesting web resources
- Host: httpforever.com
  - This is the server, where the client requested resources from

![http filter](screenshots/day-1/wireshark-http.png)

HTTP Request

- GET /js/... - the client requests for JavaScript files
- User-Agent - refers to the tool used for requesting resources
  - Gecko - open-source layout engine of Firefox
  - Firefox/140.0 - the browser with its version 
- Accept
  - */* - accepts anything the website/server has

HTTP Response

- 200 OK - the process is successful
- Server
  - nginx - an open-source HTTP server
  - 1.18.0 - nginx version
  - Ubuntu - the Operating System of the server
- Date
  - the exact timestamp of the response
  - the time isn't local time
- Content-Type - the type of resources sent

There's another HTTP request for CSS but it didn't get a response.

---
