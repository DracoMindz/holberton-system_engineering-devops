# 0x14. Mysql

For this project, students are expected to look at these concepts:

Database administration
Web stack debugging

man or help: mysqldump

##Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

###General

What is the main role of a database?
What is a database replica?
What is the purpose of a database replica?
Why database backups need to be stored in different physical locations?
What operation should you regularly perform to make sure that your database backup strategy actually works?

##Tasks

**0. Install MySQL mandatory**
First things first, let’s get MySQL installed on both your servers.

**1. Let us in! mandatory**
Create a user and password for both MySQL databases

**2. If only you could see what I've seen with your eyes mandatory**
Create a database with at least one table and one row in your primary MySQL server to replicate from.

**3. Quite an experience to live in fear, isn't it? mandatory**
On your primary MySQL server, create a new user for the replica server.

**4. Setup a Primary-Replica infrastructure using MySQL mandatory**
Having a replica member on for your MySQL database has 2 advantages redundancy and load distribution.

**5. MySQL backup mandatory**
Write a Bash script that generates a MySQL dump and creates a compressed archive out of it
