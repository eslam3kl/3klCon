# 3klCon Project v2.0

## Description
New Version <3 Full Automation Recon tool which works with Large and Medium scopes. 
Recommended to use it on VPS machine, it'll discover secrets and searching for vulnerabilities 

**So, Welcome and let's deep into it <3**

### Here is the methedology and Tasks
![](https://github.com/eslam3kl/3klCon/blob/v2.0/3klcon-MEthedology.png)


![](https://github.com/eslam3kl/3klCon/blob/v2.0/3klconV2.png)


----------------------------------------
## Installation instructions

#### If you're using VPS, I highly recommended to setup your machine at first form here 
https://www.youtube.com/watch?v=YhUiAH5SIqk&t=133s&ab_channel=Nahamsec

#### Befor ANY installation instruction: You MUST be the _ROOT_ user
`  $ su - `



#### 1. Install GO language depending on your OS version from here 

https://www.tecmint.com/install-go-in-linux/
\
or 
\
https://tzusec.com/how-to-install-golang-in-kali-linux/
\
or 
\
` sudo apt-get install golang ` 


#### 2. Check that the GO path in the root direcrory is
`/root/go/` NOT `/root/go-projects` or anything else 



#### 3. Install required tools

` chmod +x install_tools.sh `

` ./install_tools.sh ` 



#### 4. Running tool

` python 3klcon.py -t target.com ` 

----------------------------------------
## Notes
[+] If you face any problem in the running process, check that: 
    
    1. You logged in as ROOT user not normal user 
    2. Check that you installed the GO language and this path is exist /root/go/bin  
   
[+] If you face any problem with `gf` so kindly install it manually from install instructions from here 
   \
   `https://github.com/1ndianl33t/Gf-Patterns`
  
[+] It will take almost 5 ~ 6 hours running so be _Patient_ or use VPS and sleep while running :) 

[+] It will collect all the result into one directory with your target name 

[+] Some of tools may need your reaction like entering your GitHub's 2FA or username, password, etc.

[+] Go to GitHound tool directory, enter you `github_username` and `github_password` info into `config.yml` 

----------------------------------------
## Tools useds
1. 3klector https://github.com/eslam3kl/3klector
2. crtfinder https://github.com/eslam3kl/crtfinder
3. Subfinder https://github.com/projectdiscovery/subfinder
4. Assetfinder https://github.com/tomnomnom/assetfinder
5. Altdns https://github.com/infosec-au/altdns
6. Dirsearch https://github.com/maurosoria/dirsearch
7. Httpx https://github.com/projectdiscovery/httpx
8. Waybackurls https://github.com/tomnomnom/waybackurls
9. Gau https://github.com/lc/gau
10. Git-hound https://github.com/tillson/git-hound
11. Gf https://github.com/tomnomnom/gf
12. Gf-pattern https://github.com/1ndianl33t/Gf-Patterns
13. Nuclei https://github.com/projectdiscovery/nuclei
14. Nuclei-templets https://github.com/projectdiscovery/nuclei-templates
15. Subjack https://github.com/haccer/subjack
16. Port_scan.sh 
17. Gitdorks.sh 


## Stay in touch <3 
**LinkedIn** > https://www.linkedin.com/in/eslam-akl-6b998614a/
\
**Blog** > https://eslam3kl.medium.com/
\
**Mail** > eslamakl199@gmail.com
