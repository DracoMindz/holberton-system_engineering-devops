# 0x17. Web stack debugging #3

Web debugging using puppet.

### General

All your files will be interpreted on Ubuntu 14.04 LTS
All your files should end with a new line
A README.md file at the root of the folder of the project is mandatory
Your Puppet manifests must pass puppet-lint without any errors (version >= 1.1.0):
Your Puppet manifests must run without error
Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
Your Puppet manifests files must end with the extension .pp
Files will be checked with Puppet v3.4

## Tasks

**0. Strace is your friend**

Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).
