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
Look at and analyze real-time http traffic.
 
1. Open an insecure website via a browser.

![http forever](screenshots/wireshark/day-1/website-http-forever.png)

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

## CURL
- A command-line tool for tranferring resources.

1. Send a get request to an HTTP website.

![http filter](screenshots/day-1/curl-get.png)

- `-v` - verbose, see the details of the whole process

2. Analyze Results

![http filter](screenshots/day-1/curl-http-process.png)

Process Details
- the A and AAAA records of the website server has been returned at port 80
- failed to connect through IPv6, but succeeded using the IPv4 address

![http filter](screenshots/day-1/curl-http-request.png)

HTTP Request Details
- `>` - lines starting with this is the request
- GET / HTTP/1.1
 - GET - request web resources
 - / - from the root directory
 - HTTP/1.1 - using this HTTP version
- Host - the domain/website
- User-Agent - tool used to request resources
- Accept
 - */* - any type of media the website has

![http filter](screenshots/day-1/curl-http-response.png)

HTTP Response Details
- `<` - lines starting with this is the response
- HTTP/1.1 200 OK
 - 200 OK - means success, the server understood the request, found the resources, and sent it to me
- Server
 - nginx/1.18.0 (Ubuntu) - open-source web server and HTTP cache on Ubuntu OS
- Date - the exact date the response sent
- Content-Type - the type of media sent

![http filter](screenshots/day-1/curl-http-body.png)

The Body
- the data/web resource sent
- You can see the elements of the website on plain text
