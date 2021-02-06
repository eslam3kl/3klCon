# 3klCon Project v3.0

## What's 3klCon ? 
3klCon is an Automation Recon Framework which works with medium and large scopes. 
It performs more than 20 task and get all results into seperated files. 

![](https://github.com/eslam3kl/3klCon/blob/v3/Results.png)

**So, Welcome and let's deep into it <3**

### Here is the methedology and Tasks
![](https://github.com/eslam3kl/3klCon/blob/v2.0/3klcon-MEthedology.png)


![](https://github.com/eslam3kl/3klCon/blob/v3/start.png)


----------------------------------------
## Installation instructions

#### 1. Befor ANY installation instruction: You MUST be the _ROOT_ user
`  $ su - `



#### 2. GO Version 
Your GO version must be `go version go1.15.2 linux/amd64` and to check 
` go version` , If it doesn't the same,so delete the old version and install the updated one from here 

https://www.tecmint.com/install-go-in-linux/
\
or 
\
https://tzusec.com/how-to-install-golang-in-kali-linux/

and check again! 


#### 3. GO Path
Check that the GO path in the root direcrory is
`/root/go/` 
NOT
`/root/go-projects` 
or anything else 



#### 4. Install required tools (You MUST run it even if you install the used tools) 

` chmod +x install_tools.sh `

` ./install_tools.sh ` 



#### 5. Running tool (It works with python3 and python2)

` python3 3klcon.py -t target.com ` 

----------------------------------------

## Required VPS or VMware structure 

#### Don't WORRY! All this structure the automation script `install_tools` will create it automatically but kindly check it after running it.  

1. In the main directory you should have `/root` directory and `/usr/local/bin`
2. In the `/root` directory you must have `/go/bin` directory
3. In the tool's directory you will find `tools` directory after install tools_script 

![Structure](https://github.com/eslam3kl/3klCon/blob/v2.0/structure.png)

----------------------------------------
## Notes
[+] If you face any problem in the running process, check that: 
    
    1. You logged in as ROOT user not normal user 
    2. Check that you installed the GO language and this path is exist: /root/go/bin  
   
[+] If you face any problem with `gf` so kindly install it manually from install instructions from here 
   \
   `https://github.com/1ndianl33t/Gf-Patterns`
  
[+] It will take almost 5 ~ 6 hours running so be _Patient_ or use VPS and sleep while running :) 

[+] It will collect all the result into one directory with your target name 

----------------------------------------
## Tools and Scripts 
1. [3klector](https://github.com/eslam3kl/3klector)
2. [crtfinder](https://github.com/eslam3kl/crtfinder)
3. [Subfinder](https://github.com/projectdiscovery/subfinder)
4. [Assetfinder](https://github.com/tomnomnom/assetfinder)
5. [Altdns](https://github.com/infosec-au/altdns)
6. [Konan](https://github.com/m4ll0k/Konan)
7. [Httpx](https://github.com/projectdiscovery/httpx)
8. [Waybackurls](https://github.com/tomnomnom/waybackurls)
9. [Gau](https://github.com/lc/gau)
10. [Photon](https://github.com/s0md3v/Photon)
11. [Gf](https://github.com/tomnomnom/gf)
12. [Gf-pattern](https://github.com/1ndianl33t/Gf-Patterns)
13. [Nuclei](https://github.com/projectdiscovery/nuclei)
14. [Nuclei-templates](https://github.com/projectdiscovery/nuclei-templates)
15. Port_scan.sh 
16. Gitdorks.sh 

----------------------------------------
## Stay in touch <3 
[LinkedIn](https://www.linkedin.com/in/eslam-akl-6b998614a/) | [Blog](https://eslam3kl.medium.com/)  |  [Twitter](https://twitter.com/eslam3kll)
