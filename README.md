# 3klCon Project V1.0

## Description
Full Automation Recon tool which works with Small and Medium scopes. 
Recommended to use it on VPS machine, it'll discover secrets and searching for vulnerabilities 

**So, Welcome and let's deep into it <3**

![Welcome](Welcome.png)

----------------------------------------
## Updates 
### Version 1.1, what's new? 
1. Editing the tool's methedology. 
2. Using more tools.  

----------------------------------------
## Installation instructions

#### 1. Befor ANY installation instruction: You MUST be the _ROOT_ user
`  $ su - `
Because some of tools and dependencies will need the root permission


#### 2. Install required tools (You MUST run it even if you install the used tools) 

` chmod +x install_tools.sh `

` ./install_tools.sh ` 


#### 3. Running tool (Preferred to use python2 not python3)

` python 3klcon.py -t target.com ` 

----------------------------------------
## Notes
[+] If you face any problem at the installation process, check that: 
    
    1. You logged in as ROOT user not normal user 
    2. Check that you installed the GO language and this path is exist /root/go/bin  
  
[+] It will take almost 3 ~ 4 hours running if your target is a medium. So, be _Patient_ or use VPS and sleep while running :) 

[+] It will collect all the result into one directory with your target name 

[+] Some of tools may need your reaction like entering your GitHub's 2FA or username, password, etc.

----------------------------------------
## Tools useds
1. Subfinder
2. Assetfinder 
3. Altdns
4. Dirsearch
5. Httpx
6. Waybackurls
7. Gau
8. Git-hound
9. Gitdorks.sh
10. Naabu
11. Gf
12. Gf-templetes
13. Nuclei
14. Nuclei-templets
15. Subjack
16. Port_scan.sh


#### Wait the NEXT version with more and more new interesting features <3 
