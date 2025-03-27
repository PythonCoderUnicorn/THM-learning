#Subscribers 
https://tryhackme.com/room/benign


We will investigate host-centric logs in this challenge room to find suspicious process execution. To learn more about Splunk and how to investigate the logs, look at the rooms [splunk101](https://tryhackme.com/room/splunk101) and [splunk201](https://tryhackme.com/room/splunk201).

One of the client’s IDS indicated a potentially suspicious process execution indicating one of the hosts from the HR department was compromised. Some tools related to network information gathering / scheduled tasks were executed which confirmed the suspicion. Due to limited resources, we could only pull the process execution logs with Event ID: 4688 and ingested them into Splunk with the index **win_eventlogs** for further investigation.  

About the Network Information

The network is divided into three logical segments. It will help in the investigation.  

IT Department 
- James
- Moin
- Katrina

**HR department  
- Haroon
- Chris
- Diana

**Marketing department**
- Bell
- Amelia
- Deepak


index `win_eventlogs`

```splunk search
index="win_eventlogs"
```

```
How many logs are ingested from the month of March, 2022?

13959

Imposter Alert: There seems to be an imposter account observed in the logs, what is the name of that user?

Amel1a

Which user from the HR department was observed to be running scheduled tasks?

Chris.fort

Which user from the HR department executed a system process (LOLBIN) to download a payload from a file-sharing host.

haroon


To bypass the security controls, which system process (lolbin) was used to download a payload from the internet?

certutil.exe

What was the date that this binary was executed by the infected host? format (YYYY-MM-DD)

2022-03-04


Which third-party site was accessed to download the malicious payload?

controlc.com


What is the name of the file that was saved on the host machine from the C2 server during the post-exploitation phase?

benign.exe



The suspicious file downloaded from the C2 server contained malicious content with the pattern THM{..........}; what is that pattern?

THM{KJ&*H^B0}




What is the URL that the infected host connected to?

https://controlc.com/e4d11035

```


https://www.youtube.com/watch?v=elgflkcMz_s




![[Pasted image 20250315165133.png]]

300 points


























