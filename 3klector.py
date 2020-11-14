#!/usr/bin/env python 
#coded by eslam akl - eslam3kl

import requests 
import re 
from termcolor import colored 
import optparse 
'''
print(" ")
print(colored("		 ____  _    _           _             			", "red", attrs=['bold']))
print(colored("		(___ \| |  | |         | |            			", "red", attrs=['bold']))
print(colored("		  __) | | _| | ___  ___| |_ ___  _ __ 			", "red", attrs=['bold']))
print(colored("		 (__ <| |/ / |/ _ \/ __| __/ _ \| '__|			", "red", attrs=['bold']))
print(colored("		 ___) |   <| |  __/ (__| || (_) | |   			", "red", attrs=['bold']))
print(colored("		(____/|_|\_\_|\___|\___|\__\___/|_|   			", "red", attrs=['bold']))
print(" ")
print(colored("		          Coded by Eslam Akl             ", "yellow", attrs=['bold']))
print(colored("		 Blog: https://medium.com/@eslam3kl      ", "yellow", attrs=['bold']))
print(colored("		 GitHub: https://github.com/eslam3kl     ", "yellow", attrs=['bold']))
print(" ")
print(colored("[+] Acquisitions results based on: ", "green", attrs=['bold']) + colored("https://index.co", 'white'))                                
print(colored("[+] ASN results based on: ", "green", attrs=['bold']) + colored("https://www.ultratools.com", 'white'))                                
print(colored("[+] Start collecting informations...", "red"))
print(' ')
'''
#function to get user input 
def get_user_input():
	parser = optparse.OptionParser()
	parser.add_option("-t", "--target", dest="target", help="\tTarget Name (google, microsoft)")
	(options, arguments) = parser.parse_args()
	if not options.target:
		print(colored('\n(-) No target specified, use --help for more info', 'red', attrs=['bold']))
		print(colored('(+) Usage: python 3klector.py -t target', 'green', attrs=[]))
		print(" ")
		raise SystemExit 
	else: 
		return options.target

#function to send request 
def send_request(url): 
	headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:82.0) Gecko/20100101 Firefox/82.0"}
	req = requests.get(url) 
	return req


#function to get company name 
def get_company_name(url):
	response_code = send_request(url) 
	content = response_code.content 
	names = []
	companies = re.findall('(?:<strong class="c_identityChip-name">)(.*?)</strong>', content)
	for line in companies: 
		line = line.lower()
		if target not in line:
			if line not in names: 
				names.append(line)
	return names

#function to get company date 
def get_company_date(url):
	response_code = send_request(url) 
	content = response_code.content 
	dates = []
	date = re.findall('(?:<span>20)(.*?)</span>', content)
	for line in date:
		dates.append(line)
	return dates

#function to get ASN 
def get_company_asn(url):
	response_code = send_request(url) 
	content = response_code.content 
	asn_result = []
	asn_info = []
	asn_results = re.findall('(?:<div class="tool-results-heading">)(.*?)</div>', content)
	asn_information = re.findall('(?:<span class="value">)(.*?)</span>', content)
	for line in asn_results:
		if line not in asn_results:
			asn_results.append(line) 
	return asn_results

#function to get asn information country and owner  
def get_asn_info(url): 
	response_code = send_request(url) 
	content = response_code.content 
	asn_info = []
	asn_information = re.findall('(?:<span class="value">)(.*?)</span>', content)
	for line in asn_information: 
		asn_info.append(line) 
	return asn_info

#function to get ip ranges from asn 
def get_ip_range(url):
	response_code = send_request(url)
	content = response_code.content 
	ip = re.findall('(?:<a href="/AS)(.*?)" >', content)
	return ip

#DATA 
target =  get_user_input() 
target_cap = target.capitalize()
aq_url = "https://index.co/company/" + target +"/acquirees"
asn_url = "https://www.ultratools.com/tools/asnInfoResult?domainName=" + target 
asn_info_url = "https://ipinfo.io/"

#variables 
name = get_company_name(aq_url) 
date = get_company_date(aq_url)
asn_records = get_company_asn(asn_url)
asn_info = get_asn_info(asn_url)
country = []
owner = []


#create country array 
for line in range(0,len(asn_info),4): 
	country.append(asn_info[line])
#create owner array 
for line in range(3,len(asn_info)+3,4):
	owner.append(asn_info[line])

#print asn and it's information 
print(colored('\n----------------------\n [+] ASN Information\n----------------------', "red", attrs=['bold']))
if asn_records:	
	for line in range(len(asn_records)): 
		print(colored("\n(+) ASN number: ", 'red', attrs=['bold']) + colored(asn_records[line], "white", attrs=['bold']))
		print(colored("(+) Country: ", 'green', attrs=['bold']) + colored(country[line], "white"))
		print(colored("(+) Owner: ", 'green', attrs=['bold']) + colored(owner[line], "white"))
		print(colored("(+) For more info: " , "green", attrs=['bold']) + colored(asn_info_url + asn_records[line], "white"))
else:
	print(colored(" [-] ", "red", attrs=['bold']) + colored("No ASN found!", "green", attrs=['bold']))
#print acquisitions and its date 
print(colored('\n---------------------------\n [+] Comapany acquisitions \n---------------------------', 'red', attrs=['bold']))
if name:
	for line in range(len(name)): 
		print(colored('(+) ', 'green', attrs=['bold']) + colored(name[line], 'white'))
else: 
	print(colored(" [-] ", 'red', attrs=['bold']) + colored('No Acquisitions found!\n', "green", attrs=['bold']))



