
#logs 

- https://tryhackme.com/room/introtologanalysis
- 
- https://tryhackme.com/jr/introtologs
- https://tryhackme.com/jr/logoperations
- https://tryhackme.com/room/splunkdashboardsandreports

Log analysis is an essential aspect of cyber security and system monitoring. At a high level, log analysis examines and interprets log event data generated by various sources (devices, applications, and systems) to monitor metrics and identify security incidents.

- collecting, parsing, and processing log files to turn data
- data to respond to security incidents

Logs are recorded events or transactions within a system, device, or application.
- app errors
- system faults
- audited user actions
- resource uses
- network connections
- logs: event, timestamp, source, extra info

example
```
%WARNING% general: Unusual network activity detected from 10.10.0.15 to IP 203.0.113.25. Source Zone: Internal, Destination Zone: External, Application: web-browsing, Action: Alert.
```

the firewall's policy was configured to notify when such unusual activity occurs

Logs are important
- system troubleshooting - system errors, warning logs, response to issues, improve system
- cyber security incidents - detect & respond to security incidents
- threat hunting - actively search for advanced threats, look for patterns, indicators of compromise (IOCs) 
- compliance - regulations , regular log analysis

## Types of Logs

- **Application Logs:** Messages from specific applications, providing insights into their status, errors, warnings, and other operational details.
- **Audit Logs:** Events, actions, and changes occurring within a system or application, providing a history of user activities and system behaviour.
- **Security Logs:** Security-related events like logins, permission alterations, firewall activities, and other actions impacting system security.
- **Server Logs:** System logs, event logs, error logs, and access logs, each offering distinct information about server operations.
- **System Logs:** Kernel activities, system errors, boot sequences, and hardware status, aiding in diagnosing system issues.
- **Network Logs:** Communication and activity within a network, capturing information about events, connections, and data transfers.
- **Database Logs:** Activities within a database system, such as queries performed, actions, and updates.
- **Web Server Logs:** Requests processed by web servers, including URLs, source IP addresses, request types, response codes






## Investigation theory

When conducting log analysis, creating a timeline is a fundamental aspect of understanding the sequence of events within systems, devices, and applications.

The ability to visualize a timeline is a powerful tool for contextualizing and comprehending the events that occurred over a specific period.

[Splunk](https://docs.splunk.com/Documentation/Splunk/9.1.0/Search/Abouttimezones), for example, automatically detects and processes time zones when data is indexed and searched
- time is converted to UNIX time `_time`

[Plaso (Python Log2Timeline)](https://github.com/log2timeline/plaso) is an open-source tool created by Kristinn Gudjonsson and many contributors that automates the creation of timelines from various log sources. It's specifically designed for digital forensics and log analysis and can parse and process log data from a wide range of sources to create a unified, chronological timeline.
- https://plaso.readthedocs.io/en/latest/

DATA VIZ

Data visualization tools, such as Kibana (of the Elastic Stack) and Splunk, help to convert raw log data into interactive and insightful visual representations through a user interface.

Log monitoring & alerting
In addition to visualization, implementing effective log monitoring and alerting allows security teams to _proactively_ identify threats and immediately respond when an alert is generated.

Many SIEM solutions (like Splunk and the Elastic Stack) allow the creation of custom alerts based on metrics obtained in log events.

- https://tryhackme.com/jr/splunkdashboardsandreports


External Research and Threat Intel

threat intelligence are pieces of information that can be attributed to a malicious actor. Examples of threat intelligence include:

- IP Addresses
- File Hashes
- Domains

Using a threat intelligence feed like [ThreatFox](https://threatfox.abuse.ch/), we can search our log files for known malicious actors' presence.


TIMELINE  | TIMESTAMP | SUPER TIMELINES | DATA VIZ | LOG MONITORING | THREAT INTEL

https://threatfox.abuse.ch/

## Common Log File Locations

```
web servers
	Nginx - access logs    /var/log/nginx/access.log
	Nginx - error logs     /var/log/nginx/error.log
	Apache - access logs   /var/log/apache2/access.log
	Apache - error logs    /var/log/apache2/error.log

Databases
	MySQL - error logs         /var/log/mysql/error.log
	PostgreSQL - error logs    /var/log/postgresql/postgresql-{version}-main.log

Web Apps
	PHP - error logs           /var/log/php/error.log

OS
	Linux - general logs       /var/log/syslog
	Linux - auth logs          /var/log/auth.log

Firewalls & IDS/IPS
	iptables - firewall logs   /var/log/iptables.log
	snort - snort logs         /var/log/snort
```

In a security context, recognizing common patterns and trends in log data is crucial for identifying potential security threats. These "patterns" refer to the identifiable artifacts left behind in logs by threat actors or cyber security incidents.

some examples
- multiple failed login attempts
- unusual login times
- geographic anomalies
- frequent password changes
- unusual user-agent strings 

## Common attack signatures

### SQL

SQL injection attempts to exploit vulnerabilities in web applications that interact with databases. Look for unusual or malformed SQL queries in the application or database logs to identify common SQL injection attack patterns.

Suspicious SQL queries might contain unexpected characters, such as single quotes (`'`), comments (`--`, `#`), union statements (`UNION`), or time-based attacks (`WAITFOR DELAY`, `SLEEP()`).
```
10.10.61.21 - - [2023-08-02 15:27:42] "GET /products.php?q=books' UNION SELECT null, null, username, password, null FROM users-- HTTP/1.1" 200 3122
```

### Cross Site Scripting

Exploiting cross-site scripting (XSS) vulnerabilities allow attackers to inject malicious scripts into web pages. To identify common XSS attack patterns, it is often helpful to look for log entries with unexpected or unusual input that includes script tags (`<script>`) and event handlers (`onmouseover`, `onclick`, `onerror`). A useful XSS payload list to reference can be found [here](https://github.com/payloadbox/xss-payload-list).

In the example below, a cross-site scripting attempt can be identified by the `<script>alert(1);</script>` payload inserted into the `search` parameter, which is a common testing method for XSS vulnerabilities.
```
10.10.19.31 - - [2023-08-04 16:12:11] "GET /products.php?search=<script>alert(1);</script> HTTP/1.1" 200 5153
```

### Path Traversal

Exploiting path traversal vulnerabilities allows attackers to access files and directories outside a web application's intended directory structure, leading to unauthorized access to sensitive files or code. To identify common traversal attack patterns, look for traversal sequence characters (`../` and `../../`) and indications of access to sensitive files (`/etc/passwd`, `/etc/shadow`). A useful directory traversal payload list to reference can be found [here](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Directory%20Traversal/README.md).

It is important to note, like with the above examples, that directory traversals are often URL encoded (or double URL encoded) to avoid detection by firewalls or monitoring tools. Because of this, `%2E` and `%2F` are useful URL-encoded characters to know as they refer to the `.` and `/` respectively.

In the below example, a directory traversal attempt can be identified by the repeated sequence of `../` characters, indicating that the attacker is attempting to "back out" of the web directory and access the sensitive `/etc/passwd` file on the server.

```
10.10.113.45 - - [2023-08-05 18:17:25] "GET /../../../../../etc/passwd HTTP/1.1" 200 505
```

## Automated vs Manual analysis

Automated analysis involves the use of tools. For example, these often include commercial tools such as XPLG or SolarWinds Loggly. Automated analysis tools allow for processing and data analysis of logs. These tools often utilize Artificial Intelligence / Machine Learning to analyze patterns and trends. As the AI landscape evolves, we expect to see more effective automated analysis solutions.

- saves time but often these tools are commercial only
- effective recognizing patterns but depends on the model, risks of false positives
- manually with linux commands but time consuming
- manual analysis reduces false positive risk but things can get missed
- manual analysis allows for context

## Log Analysis Command Line

When analyzing collected logs, sometimes the most readily available tool we have is the command line itself. Analyzing logs through the command line provides a quick and powerful way to gain insights into system activities, troubleshoot issues, and detect security incidents, even if we don't have an SIEM system configured.

You can locate the `apache.log` file on the AttackBox under `/root/Rooms/introloganalysis/task6` to follow along with this task.

```
cat apache.log
less apache.log
tail apache.log
wc apache.log
cut -d ' ' -f 1 apache.log                   # just the IP addresses
cut -d ' ' -f 1 apache.log | sort -n
cut -d ' ' -f 1 apache.log | sort -n -r      # reverse sort
cut -d ' ' -f 1 apache.log | sort -n -r | uniq
cut -d ' ' -f 1 apache.log | sort -n -r | uniq -c   # counts

replace all occurrences of "31/Jul/2023" with "July 31, 2023"
sed 's/31\/Jul\/2023/July 31, 2023/g' apache.log

awk for conditional actions, HTTP response codes >= 400
awk '$9 >= 400' apache.log

grep 'admin' apache.log
grep -n 'admin' apache.log

find lines that don't match -v
grep -v '/index.php' apache.log | grep "203.64.77.11"


```


```
cut -d ' ' -f 7 apache.log | grep flag
awk '$9 == 200' apache.log | wc -l
cut -d ' ' -f 1 apache.log| sort -n  | uniq -c 
grep '/index.php' apache.log | grep 110.122.65.76

```


## regex logs

`203.0.113.1 - - [02/Aug/2023:10:15:23 +0000] "GET /blog.php?post=12 HTTP/1.1" 200 - "Mozilla/5.0" `

```
grep -E 'post=1[0-9]'
grep -E 'post=2[2-6]' apache-ex2.log

```

cyberchef

regex pattern `\b([0-9]{1,3}\.){3}[0-9]{1,3}\b` to search for values that are IP addresses

```
cut -d ' ' -f 1 access.log | grep 212
cut -d ' ' -f 7 access.log | grep '==' 
THM{CYBERCHEF_WIZARD}

```

`\b([0-9A-F]{2}(:[0-9A-F]{2}){5})\b`

`encodedflag.txt` = from Base64 + Extract MAC addresses
