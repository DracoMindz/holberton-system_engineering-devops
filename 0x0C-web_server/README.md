# 0x0C. Web server

In this project, some of the tasks will be graded on 2 aspects:

Is your web-01 server configured according to requirements
Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

start an ubuntu:16.04 Docker container
run your script on it
see how  behaves
Check out the Docker concept page for more info about how to manipulate containers.

### Resources
Read or watch:

How the web works
Nginx
How to Configure Nginx
Child process
Root and sub domain
HTTP requests
HTTP redirection
Not found HTTP response code
Logs files on Linux
For reference:

RFC 7231 (HTTP/1.1)
RFC 7540 (HTTP/2)
man or help:

scp
curl

## Learning Objectives

**General**
What is the main role of a web server?
What is a child process?
Why web servers usually have a parent process and child processes?
What are the main HTTP requests?

**DNS**
What DNS stands for?
What is DNS main role?

**DNS Record Types**
A
CNAME
TXT
MX

## Requirements

**General**
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

**0. Transfer a file to your server mandatory**
Write a Bash script that transfers a file from our client to a server.

**1. Install nginx web server mandatory**
Web servers are the piece of software generating and serving HTML pages, let’s install one!

**2. Setup a domain name mandatory**

**3. Redirection mandatory**
Replace a line with multiple lines with sed
Configure your Nginx server so that /redirect_me is redirecting to another page.

**4. Not found page 404 mandatory**
Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.