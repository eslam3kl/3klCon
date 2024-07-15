# 3klCon Project [Archived]

## Description
Automated Recon tool which works with Large and Medium scopes. 

ّIt's recommended to use it on VPS, it'll discover secrets and search for vulnerabilities 

**So, Welcome, and let's get deep into it <3**

![logo](https://github.com/eslam3kl/3klCon/assets/65075282/ee087d0e-41ab-4909-8adc-345028858983)


----------------------------------------
## What are the tasks it will do? 
1. Search for subdomains using different tools and resources (Subfinder - Findomain - Amass - Assetfinder - Archive.Org - RapidDNS.io - Riddler.io - JLDC - GitHub-Subdomains - Chaos)
2. Search for the 3rd level of subdomains by extracting them using a simple Python script and enumerate them using (Subfinder - Findomain - Assetfinder - Archive.Org)
3. Resolving Subdomains with basic web ports 80 and 443
4. Resolving Subdomains with Special Web ports 81,3000,3001,8000,8080,8443,10000,9000,9443
5. Port scanning for all discovered assets using Naabu
6. Search for Wayback records using (Hakrawler - GauPlus)
7. Enumerate JavaScript files using (SubJs - Wayback Records)
8. Extract the files with interesting extensions
9. Search for Admin and login panels
10. Scan the assets using Nuclei

----------------------------------------
## Installation instructions
#### 1. Run the following script to check what tools you need to install 
```
# ./check_tools.sh 
Checking for tool installation...
--> subfinder is installed.
--> findomain is installed.
--> assetfinder is installed.
--> amass is installed.
--> anew is installed.
--> github-subdomains is not installed. You can install it from https://github.com/gwen001/github-search/releases
--> chaos is installed.
--> hakrawler is installed.
--> gauplus is installed.
--> subjs is installed.
--> httpx is installed.
--> python3 is installed.
--> naabu is installed.
--> nuclei is installed.
```

#### 2. Create your targets.txt file (Target per line)
```
hackerone.com
bugcrowd.com
google.com
```

#### 3. Open 3klcon.sh file and put your CHAOS API Key
```
export CHAOS_KEY=""; # please insert your chaos key here
```

#### 4. Open `github_tokens.txt`z file and put in your API keys.

#### 5. Run the tool
```
./3klcon.sh targets.txt
```

----------------------------------------
## Notes
1. It will take almost 1 ~ 2 hours to run if your target is a medium. So, be _Patient_ or use VPS and sleep while running :) 
2. It will collect all the results for every target into a separate directory. 

----------------------------------------
## Tools
- subfinder
- findomain
- assetfinder
- amass
- anew
- github-subdomains
- chaos
- hakrawler
- gauplus
- subjs
- httpx
- python3
- naabu
- nuclei

----------------------------------------

## Stay in touch <3 
[LinkedIn](https://www.linkedin.com/in/eslam3kl/) | [Blog](https://eslam3kl.gitbook.io/)
