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
print(colored("			(______/|_| \_)\_)____)___/|_| |_| V3.0 ", "red", attrs=['bold']))
print(" ")
print(colored("			         Coded by ", "white", attrs=['bold']) + colored("Eslam Akl           ", "yellow", attrs=['bold']))
print(colored("			Blog: ", "white", attrs=['bold']) + colored("https://eslam3kl.medium.com/",  "yellow", attrs=['bold']))
print(colored("			Twitter: ", "white", attrs=['bold']) + colored("https://twitter.com/eslam3kll", "yellow", attrs=['bold']))
print(colored("\n(+) Automation Recon Framework, Medium & Large scopes","cyan", attrs=['bold']))
print(colored("(+) ", "red") + colored("Collect all Acquisitions and ASN", "green"))
print(colored("(+) ", "red") + colored("Collect Live subdomains","green"))
print(colored("(+) ", "red") + colored("Collect Live sub-subdomains","green"))
print(colored("(+) ", "red") + colored("Internal and External subdomains","green"))
print(colored("(+) ", "red") + colored("Subdomains fuzzing","green"))
print(colored("(+) ", "red") + colored("Spider & wayback subdomains","green"))
print(colored("(+) ", "red") + colored("Extract JS files","green"))
print(colored("(+) ", "red") + colored("Content Discovery","green"))
print(colored("(+) ", "red") + colored("Port Scan","green"))
print(colored("(+) ", "red") + colored("GitHub dork links","green"))
print(colored("(+) ", "red") + colored("Extract possible vulnerable links ","green"))
print(colored("(+) ", "red") + colored("OSINT techniques","green"))
print(colored("(+) ", "red") + colored("Scan for Subdomain vulnerabilities Takeover & S3buckets","green"))
print(colored("(+) ", "red") + colored("Scan Links for CVE's","green"))
print(colored("(+) ", "red") + colored("Scan Security Headers ","green"))
print(colored("(+) ", "red") + colored("Scan Misconfiguration ","green"))
print(colored("(+) ", "red") + colored("Scan Vulnerabilities","green"))
print(colored("(+) ", "red") + colored("Scan for website technologies and services\n", "green"))
print(" ")

#get user input 
def get_user_input():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target_url", dest="target_url", help="\tTarget URL (google.com, microsoft.com)")
	(options, arguments) = parser.parse_args()
	if not options.target_url:
		print(colored("\n\n[-] Warning: ", "red", attrs=['bold']) + colored("Target url doesn't exist, see --help for more info", 'white'))
		print(colored("[+] Usage: ","red", attrs=['bold']) + colored("python 3klcon.py -t target.com", 'white'))
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
live_subdomains = "live_subdomains.txt"
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
subdomain_scan = "subdomain_scan.txt"
subdomain_takeover = "subdomain_takeover_scan.txt"
service_info = "service_info_scan.txt"
security_misconfiguration = "security_misconfiguration_scan.txt"
endpoint_check = "endpoints_scan.txt"
fuzzers_check = "fuzzers_check.txt"


########################[ START ]##############################
dir_check = input("[+] Perfrom directory brute forcing at all subdomains?\n[*] If [yes] it will take long time [yes/no] ")
port_check = input("\n[+] Scan ports on all subdomain?\n[*] If [yes] it will take long time [yes/no] ")
print(colored("\n[*] Be Patient if your target is large scope.", 'green', attrs=['bold']))
print(colored("[-] It will take more time to scan its subdomains :)\n", 'red', attrs=['bold']))
subprocess.call("mkdir " + word, shell=True)
os.chdir(word)

#get all asn and acquistions 
print(colored("\n--------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start collecting ASN & Acquisitions", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'green', attrs=['bold']))
try:
	subprocess.call("python ../tools/3klector/3klector.py -t " + word + " > asn_aquisitions.txt" , shell=True) 
	print(colored("Process DONE!\nFile Name: asn_aquisitions.txt\n" , 'white', attrs=['bold']))
except: 
	print(colored("\nSkipping to the next step...\n" , 'white', attrs=['bold']))
	pass
#=========================================#

#get subdomains from domain and filtering output 
print(colored("\n-------------------------------------------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start collecting Resolved Subdomains", 'red', attrs=['bold']))
print(colored("[*] Extract all subdomains using 3 tools CrtFinder, assetfinder and sunfinder" , 'white', attrs=['bold']))
print(colored("-------------------------------------------------------------------------------", 'green', attrs=['bold']))
try:
	subprocess.call("python ../tools/crtfinder/crtfinder.py -u " + target + " > " + subdomains_output, shell=True) 
	subprocess.call("assetfinder -subs-only " + target + " >> " + subdomains_output, shell=True) 
	subprocess.call("subfinder -silent -d " + target + " >> " + subdomains_output, shell=True) 
	subprocess.call("cat " + subdomains_output + " | qsreplace | httpx -follow-redirects -silent > " + resolved_subdomain , shell=True) 
	subprocess.call("cat " + resolved_subdomain + " | cut -d : -f2 | cut -c 3- > " + live_subdomains, shell=True) 
	subprocess.call("rm " + resolved_subdomain, shell=True)
	print(colored("Process DONE!\nFile Name: live_subdomains.txt\n" , 'white', attrs=['bold']))
except:
	print(colored("\nSkipping to the next step...\n" , 'white', attrs=['bold']))
	pass
#=========================================#

#get all available endpoint using wayback machine and filter the results 
print(colored("\n--------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start collecting waybackurls", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'green', attrs=['bold']))
try:
	subprocess.call("cat " + live_subdomains + " | waybackurls | grep -v -e .css -e .jpg -e .jpeg -e png -e ico -e svg > wayback.txt" , shell=True)
	subprocess.call("cat wayback.txt | qsreplace | httpx -silent -follow-redirects > " + waybackurls_output, shell=True)
	subprocess.call("rm wayback.txt ", shell=True)
	print(colored("Process DONE!\nFile Name: waybackurls.txt" , 'white', attrs=['bold']))
except: 
	print(colored("\nSkipping to the next step...\n" , 'white', attrs=['bold']))
	pass
#=========================================#

#get the js files from the output wayback machine results 
print(colored("\n--------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start collecting JS files", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'green', attrs=['bold']))
try:
	subprocess.call('cat ' + waybackurls_output + ' | grep ".js" > ' + js_files , shell=True) 
	print(colored("Process DONE!\nFile Name: js_files.txt", 'white', attrs=['bold']))
except:
	print(colored("\nSkipping to the next step...\n" , 'white', attrs=['bold']))
	pass
#=========================================#
#GitHub scan 
#create github search links 
print(colored("\n--------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start create GitHub secret links", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'green', attrs=['bold']))
try:	
	subprocess.call("gitdorks.sh " + target + " > github_dorking.txt", shell=True)
	print(colored("Process DONE!\nFile name: github_dorking.txt", 'white', attrs=['bold'])) 
except: 
	print(colored("There's an problem, please check [gitdorks.sh] again", 'white'))
	print(colored("Skipping to the next step...\n" , 'white', attrs=['bold']))
	pass 

#=========================================#

#make possible vulnerable files by gf 
print(colored("\n--------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start creating vulnerable files", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'green', attrs=['bold']))
try:
	subprocess.call("mkdir vulnerable_files", shell=True) 
	subprocess.call("cat " + waybackurls_output + " | grep = | gf ssrf > vulnerable_files/" + ssrf, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf sqli > vulnerable_files/" + sqli, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf xss > vulnerable_files/" + xss, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf lfi > vulnerable_files/" + lfi, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf idor > vulnerable_files/" + idor, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf redirect > vulnerable_files/" + redirect, shell=True)
	subprocess.call("cat " + waybackurls_output + " | grep = | gf rce > vulnerable_files/" + rce, shell=True)
	print(colored("Process DONE!", 'white', attrs=['bold'])) 
except: 
	print(colored("There's an error in GF-Templete, Please check its installation again after ending automation", 'white'))
	print(colored("Skipping to the next step...\n" , 'white', attrs=['bold']))
	pass 

#=========================================#

#photon tool 
print(colored("\n--------------------------------------------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start executing Photon", 'red', attrs=['bold']))
print(colored("[*] The results will be inside Photon directory :)", 'white', attrs=['bold']))
print(colored("--------------------------------------------------------------------------------", 'green', attrs=['bold']))
try: 
	subprocess.call("python3 ../tools/Photon/photon.py -u " + target + " -l 3 -t 50 --keys -o ../" + word , shell=True)
	print(colored("Process DONE!", 'white', attrs=['bold'])) 
except: 
	print(colored("Skipping to the next step...\n" , 'white', attrs=['bold']))	
	pass 

#=========================================#

#vulnerability scanners 
print(colored("\n--------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start Automation Scanners", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'green', attrs=['bold']))
try: 
	subprocess.call("mkdir automation_scanners", shell=True) 
	#test all subdomains for service and vulnerabilities - nuclei
	subprocess.call("cat " + live_subdomains + " | nuclei -t ../tools/nuclei-templates -o automation_scanners/" + subdomain_scan, shell=True )
	#test subdomain takeover, cves 
	subprocess.call("nuclei -silent -l " + live_subdomains + " -t ../tools/nuclei-templates/subdomain-takeover/ -t ../tools/nuclei-templates/dns/ -t ../tools/nuclei-templates/cves/  -o automation_scanners/" + subdomain_takeover, shell=True)
	subprocess.call("subjack -w " + live_subdomains +" -timeout 30 -ssl -c /root/go/src/github.com/haccer/subjack/fingerprints.json -v -m >> automation_scanners/" + subdomain_takeover, shell=True)
	#test services info & technologies 
	subprocess.call("nuclei -silent -l " + live_subdomains + " -t ../tools/nuclei-templates/files -t ../tools/nuclei-templates/technologies -o automation_scanners/" + service_info, shell=True)
	#security_misconfiguration 
	subprocess.call("nuclei -silent -l " + live_subdomains + " -t ../tools/nuclei-templates/security-misconfiguration -o automation_scanners/" + security_misconfiguration, shell=True)
	#vulnerabilities, generic detection, cves & payload 
	subprocess.call("nuclei -silent -l " + waybackurls_output + "  -t ../tools/nuclei-templates/cves/ -t ../tools/nuclei-templates/payloads  -t ../tools/nuclei-templates/vulnerabilities -t ../tools/nuclei-templates/generic-detections -o automation_scanners/" + endpoint_check , shell=True)
	subprocess.call("nuclei -silent -l fuzzable.txt  -t ../tools/nuclei-templates/cves/ -t ../tools/nuclei-templates/payloads  -t ../tools/nuclei-templates/vulnerabilities -t ../tools/nuclei-templates/generic-detections -o automation_scanners/" + fuzzers_check , shell=True)
except: 
	print(colored("There's an problem, please check it again", 'white'))
	print(colored("Skipping to the next step...\n" , 'white', attrs=['bold']))
	pass

#=========================================#

#directory bruteforcing 
print(colored("\n--------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start directory brute-forcing", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'green', attrs=['bold']))
try:
	if dir_check == "yes": 
		subprocess.call("python3 ../tools/konan/konan.py -U live_subdomains.txt -w ../tools/konan/db/small.txt -o 200,301,302 -t 40  > directory_brute_forcing.txt", shell=True)
	else: 
		subprocess.call("python3 ../tools/konan/konan.py -u " + target +" -w ../tools/konan/db/small.txt -o 200,301,302 -t 20  > directory_brute_forcing.txt", shell=True)
	print(colored("Process DONE!\nFile Name: directory_brute_forcing.txt", 'white', attrs=['bold'])) 
except: 
	print(colored("\nSkipping to the next step...\n" , 'white', attrs=['bold']))
	pass

#=========================================#

#get subdomain from subdomain using altdns 
print(colored("\n--------------------------------------------", 'green', attrs=['bold']))
print(colored("[+] Start collecting Sub-subdomains", 'red', attrs=['bold']))
print(colored("--------------------------------------------", 'green', attrs=['bold']))
try: 
	subprocess.call("altdns -i " + live_subdomains +" -o data_output_altdns.txt -w ../word_lists/words.txt -r -s " + altdns_output, shell=True)
	print(colored("Process DONE!\nResults in altdns_output.txt", 'white', attrs=['bold']))
except: 
	print(colored("There's an problem in resolving subdomains, please check it again", 'white'))
	print(colored("Skipping to the next step...\n" , 'white', attrs=['bold']))
	pass 

#=========================================#

#perform port scan 
print(colored("---------------------------", 'green', attrs=['bold']))
print(colored("[+] Start Port Scanning", 'red', attrs=['bold']))
print(colored("---------------------------", 'green', attrs=['bold']))
try:
	subprocess.call("scan.sh -d " + target + " | tee -a port_scan.txt" , shell=True) 
	print(colored("Process DONE!\nFile Name: port_scan.txt", 'white', attrs=['bold']))
except: 
	print(colored("There's an error, Please check it again after ending automation", 'white'))
	print(colored("Skipping to the next step...\n" , 'white', attrs=['bold']))
	pass 

try:
	if port_check == "yes": 
		subprocess.call("scan.sh -f " + live_subdomains + " | tee -a port_scan.txt" , shell=True) 
	else: 
		subprocess.call("scan.sh -d " + target + " | tee -a port_scan.txt" , shell=True) 
	print(colored("Process DONE!\nFile Name: port_scan.txt", 'white', attrs=['bold']))
except: 
	print(colored("\nSkipping to the next step...\n" , 'white', attrs=['bold']))
	pass

#=========================================#

