0x05. Processes and signals

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is a PID
What is a process
How to find a process’ PID
How to kill a process
What is a signal
What are the 2 signals that cannot be ignored

0. What is my PID mandatory
Write a Bash script that displays its own PID.

1. List your processes mandatory
Write a Bash script that displays a list of currently running processes.

2. Show your Bash PID mandatory
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

3. Show your Bash PID made easy mandatory
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

4. To infinity and beyond mandatory
Write a Bash script that displays To infinity and beyond indefinitely.

5. Kill me now mandatory
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

6. Kill me now made easy mandatory
Write a Bash script that kills 4-to_infinity_and_beyond process.

7. Highlander mandatory
Write a Bash script that displays:

To infinity and beyond indefinitely
With a sleep 2 in between each iteration
I am invincible!!! when receiving a SIGTERM signal
Make a copy of your 6-kill_me_now_made_easy script, name it 67-kill_me_now_made_easy, that kills the 7-highlander process instead of the 4-to_infinity_and_beyond one.

8. Beheaded process mandatory
Write a Bash script that kills the process 7-highlander.



