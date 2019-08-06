#0x0B. SSH

Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away. But contrary to level 2, you will not connect using a password but an RSA key. 

##Learning Objectives

**General**
What is a server
Where servers usually live
What is SSH
How to create an SSH RSA key pair
How to connect to a remote host using an SSH RSA key pair
The advantage of using #!/usr/bin/env bash instead of /bin/bash

##Requirements

**General**
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

##Tasks

0. Use a private key mandatory
Write a Bash script that uses ssh to connect to your server using the private key 

1. Create an SSH key pair mandatory
Write a Bash script that creates an RSA key pair.

2. Client configuration file mandatory
Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

3. Let me in! mandatory
Now that you have successfully connected to your server, we would also like to join the party.

4. Client configuration file (w/ Puppet) #advanced
Let’s practice using Puppet to make changes to our configuration file.
