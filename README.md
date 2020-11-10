# Git-Config-Manager
Ever got in a situation? Where :
- You work in different networks and need to switch proxy settings for git
-  You have multiple Github IDs(e.g. 1 personal and 1 official) and you need to switch them quickly
- You have some settings of `git config` which you keep switching
  
Then Git-Config-Manager can save your time, reduce errors and efforts.

Just edit the `profiles.cfg` file to have your git profiles, and use this utility to switch them with ease. You can simply add git variables you want to get(unset and then) set when you run **Git-Config-Manager**:
```
[office_proxy]
http.sslVerify = false
http.proxy = http://myoffice.com:8000

[no_proxy]
http.sslVerify = true
http.proxy = UNSET

[office]
http.sslVerify = false
http.proxy = http://myoffice.com:8000
user.email = rohit.rawat@myoffice.com
user.name = official-rohit-id
core.autocrlf = false

[home]
http.sslVerify = true
http.proxy = UNSET
user.email = xordux@gmail.com
user.name = xordux
core.autocrlf = false
```

## Instructions to run:
### Installation:
 - [Install Python3](https://www.python.org/downloads/)
 - If you don't have git installed, then [click here to install git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

 ### To Run:
 - To start run following command:
	 ```
	python config_manager.py <profile_name>
	```
