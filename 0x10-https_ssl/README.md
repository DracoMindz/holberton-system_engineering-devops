# 0x10. HTTPS SSL

### Resources
**Read or watch:**

What is HTTPS?
What are the 2 main elements that SSL is providing
HAProxy SSL termination on Ubuntu16.04
SSL termination
Bash function

**man or help:**

awk
dig

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General
What is HTTPS SSL 2 main roles
What is the purpose encrypting traffic
What SSL termination means

## Requirements

### General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
**0. HTTPS ABC mandatory**
What is HTTPS?
Why do you need HTTPS?
You want to setup HTTPS on your website, where shall you place the certificate?

**1. World wide web mandatory**
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

**2. HAproxy SSL termination mandatory**
Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

