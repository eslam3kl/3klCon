#!/usr/bin/env python 

# [+] This code is written by Eslam Akl - @eslam3kl #
# [+] Automation tool to perform Recon - Information gathering #
# [+] Happy Hacking #

import subprocess
import os 
from termcolor import colored 
import optparse 


print(" ")
print(colored("			 ______  _     _                  		", "red", attrs=['bold']))
print(colored("			(_____ \| |   | |						", "red", attrs=['bold']))
print(colored("			 _____) ) |  _| | ____ ___  _____  		", "red", attrs=['bold']))
print(colored("			(_____ (| |_/ ) |/ ___) _ \|  _  \ 		", "red", attrs=['bold']))
print(colored("			 _____) )  _ (| ( (__| |_| | | | |		", "red", attrs=['bold']))
print(colored("			(______/|_| \_)\_)____)___/|_| |_| V1.0 	", "red", attrs=['bold']))
print(" ")
print(colored("			         Coded by Eslam Akl           ", "yellow", attrs=['bold']))
print(colored("			Blog: https://medium.com/@eslam3kl",  "yellow", attrs=['bold']))
print(colored("			GitHub: https://github.com/eslam3kl", "yellow", attrs=['bold']))
print(colored("\n[+] Automation tool to perform Recon/Information Gathering on Small & Medium scopes","red", attrs=['bold']))
print(colored("[+] Medium Scope Tasks: ","red", attrs=['bold']))
print(colored("(+) Collect Live subdomains","green", attrs=[]))
print(colored("(+) Collect Live sub-subdomains","green", attrs=[]))
print(colored("(+) Spider & wayback subdomains","green", attrs=[]))
print(colored("(+) Extract JS files","green", attrs=[]))
print(colored("(+) Content Discovery","green", attrs=[]))
print(colored("(+) Port Scan","green", attrs=[]))
print(colored("(+) GitHub Secrets","green", attrs=[]))
print(colored("(+) GitHub dork links","green", attrs=[]))
print(colored("(+) Extract possible vulnerable links ","green", attrs=[]))
print(colored("(+) Scan for Subdomain vulnerabilities Takeover & S3buckets","green", attrs=[]))
print(colored("(+) Scan Links for CVE's","green", attrs=[]))
print(colored("(+) Scan Security Headers ","green", attrs=[]))
print(colored("(+) Scan Misconfiguration ","green", attrs=[]))
print(colored("(+) Scan Vulnerabilities","green", attrs=[]))
print(colored("(+) Scan for website technologies and services\n", "green", attrs=[]))
#get user input 
def get_user_input():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target_url", dest="target_url", help="\tTarget URL (google.com, microsoft.com)")
	(options, arguments) = parser.parse_args()
	if not options.target_url:
		print(colored("\n\n[-] Target url doesn't exist, see --help for more info", 'blue', attrs=['bold']))
		print(colored('[+] Usage: python 3klcon.py -t target.com', 'blue', attrs=['bold']))
		print(" ")
		raise SystemExit 
	else: 
		return options.target_url


#target
user_input = get_user_input()
target = user_input
word = target.split(".")[0]
#subdomain_stage_names 
subdomains_output = "subdomains.txt" 
httpx_output = "httpx_subfinder_without.txt" 
unique_subdomains = "unique_subdomains.txt"
resolved_subdomain = "resolved_subdomains.txt"
live_subdomains = "Live_subdomains.txt"
altdns_output = "altdns_output.txt"
git_secrets = "GitHub secrets.txt"
#scan
port_scan = "port_scan.txt"
#wayback files name 
waybackurls_output = "waybackurls.txt"
wayback = "wayback_urls.txt"
js_files = "js_files.txt"
#vulnerable files name 
ssrf = "gf_ssrf.txt"
redirect = "gf_redirect.txt"
xss = "gf_xss.txt"
sqli = "gf_sqli.txt"
lfi = "gf_lfi.txt"
rce = "gf_rce.txt"
idor = "gf_idor.txt"
#nuclei_output 
nuclei = "nuclei_vulnerable_links_results"
subdomain_takeover = "subdomain_takeover_scan.txt"

########################[ START ]##############################
subprocess.call("mkdir " + word, shell=True)
os.chdir(word)

#get subdomains from domain and filtering output 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start collecting resolved Subdomains", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
subprocess.call("assetfinder -subs-only " + target + " > " + subdomains_output, shell=True) 
subprocess.call("subfinder -silent -d " + target + " >> " + subdomains_output, shell=True) 
subprocess.call("cat " + subdomains_output + " | qsreplace | httpx -follow-redirects -silent > " + resolved_subdomain , shell=True) 
subprocess.call("cat " + resolved_subdomain + " | cut -d : -f2 | cut -c 3- > " + live_subdomains, shell=True) 
subprocess.call("rm " + subdomains_output + " " + resolved_subdomain, shell=True)
print(colored("Process DONE!\nFile Name: live_subdomains.txt\n" , 'blue', attrs=['bold']))


#get subdomain from subdomain using altdns 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start collecting Sub-subdomains", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
subprocess.call("altdns -i " + live_subdomains +" -o data_output_altdns.txt -w ../word_lists/words.txt -r -s " + altdns_output, shell=True)
print(colored("Process DONE!\nResults in altdns_output.txt", 'blue', attrs=['bold']))


#get all available hidden direcotories from subdomains 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start Content Discovery ", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
subprocess.call("python3 ../tools/dirsearch/dirsearch.py -L " + live_subdomains + " -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -e js,php,bak,txt,asp,aspx,jsp,html,zip,jar,sql,json,old,gz,shtml,log,swp,yaml,yml,config,save,rsa,ppk,tar --simple-report dirsearch_output.txt > subdomains_content_discovery.txt ", shell=True)
subprocess.call("python3 ../tools/dirsearch/dirsearch.py -L " + altdns_output + " -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -e js,php,bak,txt,asp,aspx,jsp,html,zip,jar,sql,json,old,gz,shtml,log,swp,yaml,yml,config,save,rsa,ppk,tar --simple-report dirsearch_output_altdns.txt > altdns_subdomains_content_discovery.txt ", shell=True)
print(colored("Process DONE!\nFile's Names: subdomains_content_discovery.txt & altdns_subdomains_content_discovery.txt", 'blue', attrs=['bold']))


#get all available endpoint using wayback machine and filter the results 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start collecting waybackurls", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
subprocess.call("cat " + live_subdomains + " | waybackurls | grep -v -e .css -e .jpg -e .jpeg -e png -e ico -e svg > wayback.txt" , shell=True)
subprocess.call("cat " + live_subdomains + " | gau | grep -v -e .css -e .jpg -e .jpeg -e png -e ico -e svg >> wayback.txt" , shell=True)
subprocess.call("cat wayback.txt | qsreplace | httpx -silent -follow-redirects > " + waybackurls_output, shell=True)
subprocess.call("rm wayback.txt ", shell=True)
print(colored("Process DONE!\nFile Name: waybackurls.txt" , 'blue', attrs=['bold']))
 

#get the js files from the output wayback machine results 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start collecting JS files", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
subprocess.call('cat ' + waybackurls_output + ' | grep ".js" > ' + js_files , shell=True) 
print(colored("Process DONE!\nFile Name: js_files.txt", 'blue', attrs=['bold']))


#perform port scan 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start Port Scanning", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
try:
	subprocess.call("scan.sh -f " + live_subdomains + " > port_scan.txt" , shell=True) 
	print(colored("Process DONE!\nFile Name: port_scan.txt", 'blue', attrs=['bold']))
except OSError: 
	print(colored("There's an error, Please check it again after ending automation", 'blue', attrs=[]))
	pass 

#GitHub scan 
subprocess.call("mkdir GitHub_Secrets", shell=True) 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start Searching at GitHub", 'red', attrs=['bold']))
print(colored("[-] You Must create file 'config.yml' into git-hound dir and set your GitHub username and password", 'blue', attrs=[]))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
try:
	subprocess.call("cat Live_subdomains.txt | git-hound --config-file ../tools/git-hound/config.yml --dig-files --dig-commits > " + git_secrets)
	subprocess.call("mv " + git_secrets + " GitHub_secrets/", shell=True)
	print(colored("Process DONE!\nFile Name: Github_Secrets.txt", 'blue', attrs=['bold']))
except: 
	print(colored("[-] Git-hound asked for 2FA so it stopped in your automation, So Kindly perform this process maually\n[+] Get into domain folder 'Results directory' and run this command", 'red', attrs=[]))
	print(colored("[+] Command: cat Live_subdomains.txt | git-hound --config-file ../tools/git-hound/config.yml --dig-files --dig-commits", 'blue', attrs=[]))
	pass

#create github search links 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start create GitHub secret links", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
with open("Live_subdomains.txt", "r") as subdomains: 
	for subdomain in subdomains: 
		subprocess.call("gitdorks.sh " + target + " > GitHub_Secrets/github_dorks.txt", shell=True) 
print(colored("Process DONE!\nFile Name: github_dorks.txt", 'blue', attrs=['bold'])) 

#make possible vulnerable files by gf 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start creating vulnerable files", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
try:
	subprocess.call("mkdir vulnerable_files", shell=True) 
	subprocess.call("cat " + waybackurls_output + " | grep = | gf ssrf > vulnerable_files/" + ssrf, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf sqli > vulnerable_files/" + sqli, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf xss > vulnerable_files/" + xss, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf lfi > vulnerable_files/" + lfi, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf idor > vulnerable_files/" + idor, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf redirect > vulnerable_files/" + redirect, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf rce > vulnerable_files/" + rce, shell=True)
	print(colored("Process DONE!", 'blue', attrs=['bold'])) 
except OSError: 
	print(colored("There's an error in GF-Templete, Please check its installation again after ending automation", 'blue', attrs=[]))
	pass 

#vulnerability scanners 
print(colored("\n--------------------------------------------", 'red', attrs=['bold']))
print(colored("[+] Start Automation Scanners", 'red', attrs=['bold']))
print(colored("[+] Please check updates for Nuclei", 'cyan'))
print(colored("--------------------------------------------", 'red', attrs=['bold']))
subprocess.call("mkdir automation_scanners", shell=True) 
#test all subdomains for service and vulnerabilities - nuclei
subprocess.call("cat " + live_subdomains + " | nuclei -t nuclei-templates -o automation_scanners/" + nuclei, shell=True )
subprocess.call("subjack -w " + live_subdomains +" -timeout 30 -ssl -c /root/go/src/github.com/haccer/subjack/fingerprints.json -v -m >> automation_scanners/" + subdomain_takeover, shell=True)
#=========================================#
