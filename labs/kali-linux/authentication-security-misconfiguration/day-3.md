# Security Concepts

## Input validation
- The system's way of deciding whether an user input makes sense or not.

## Input sanitation
- The developer's action to make sure that the user's input won't mess with the system.
- This includes removing character(s) that might get mistaken as a SQL command by the database engine.

## Information disclosure
- This happens when a website accidentally leaks a sensitive information.

## Forced browsing
- An attacker find paths that are otherwise hidden to normal users.
- This is done by manually or using a program to type a website's paths in the search bar.

## Reconnaissance
- The act of studying a website, database, or user to attack.
- For websites, this includes finding input fields, finding vulnerabilities, and deciding how they can break in and attack.
- To put it simply, it is like a thief creating a map of the house they want to break in.

## Defense in depth
- This is adding an extra layer of defense on a website/database.
- It ensures that an attack won't do as much damage all at once, which gives the developers and cybersecurities to enclose, mitigate, and track the attack.

## SQL injection
- This is when the database engine mistakenly accepts a user input as a SQL command.
- For example, an attacker enters `admin' --` to the username input field. The `'` encloses the `admin`, which results in the database engine accepting `--`, or a comment symbol, as a SQL command. This comments out the rest of the SQL query, which includes the password inputting.
