
#Subscribers 
https://tryhackme.com/room/typosquatters


Scenario

Just working on a typical day as a software engineer, Perry received an encrypted 7z archive from his boss containing a snippet of a source code that must be completed within the day. Realising that his current workstation does not have an application that can unpack the file, he spins up his browser and starts to search for software that can aid in accessing the file. Without validating the resource, Perry immediately clicks the first search engine result and installs the application.

Last **September 26, 2023**, one of the security analysts observed something unusual on the workstation owned by Perry based on the generated endpoint and network logs. Given this, your SOC lead has assigned you to conduct an in-depth investigation on this workstation and assess the impact of the potential compromise.

Connection Details﻿

Deploy the attached machine by clicking the Start Machine button in the upper-right-hand corner of the task. The provided virtual machine runs an Elastic Stack (ELK), which contains the logs that will be used throughout the room. 

Once the machine is up, access the Kibana console (via the AttackBox or VPN) using the following credentials below. The Kibana instance may take up to 3-5 minutes to initialise.


```
What is the URL of the malicious software that was downloaded by the victim user?



What is the IP address of the domain hosting the malware?





What is the PID of the process that executed the malicious software?





Following the execution chain of the malicious payload, another remote file was downloaded and executed. What is the full command line value of this suspicious activity?




The newly downloaded script also installed the legitimate version of the application. What is the full file path of the legitimate installer?






What is the name of the service that was installed?







The attacker was able to establish a C2 connection after starting the implanted service. What is the username of the account that executed the service?





After dumping LSASS data, the attacker attempted to parse the data to harvest the credentials. What is the name of the tool used by the attacker in this activity?




What is the credential pair that the attacker leveraged after the credential dumping activity? (format: username:hash)




After gaining access to the new account, the attacker attempted to reset the credentials of another user. What is the new password set to this target account?




What is the name of the workstation where the new account was used?





After gaining access to the new workstation, a new set of credentials was discovered. What is the username, including its domain, and password of this new account?





Aside from mimikatz, what is the name of the PowerShell script used to dump the hash of the domain admin?



What is the AES256 hash of the domain admin based on the credential dumping output?






After gaining domain admin access, the attacker popped ransomware on workstations. How many files were encrypted on all workstations?






```












































































