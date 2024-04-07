#!/bin/bash

# Define the tools to check along with their installation URLs
tools=("subfinder=https://github.com/projectdiscovery/subfinder/releases" 
       "findomain=https://github.com/Edu4rdSHL/findomain/releases"
       "assetfinder=https://github.com/tomnomnom/assetfinder/releases"
       "amass=https://github.com/OWASP/Amass/releases"
       "anew=https://github.com/tomnomnom/anew/releases"
       "github-subdomains=https://github.com/gwen001/github-search/releases"
       "chaos=https://github.com/projectdiscovery/chaos-client/releases"
       "hakrawler=https://github.com/hakluke/hakrawler/releases"
       "gauplus=https://github.com/lc/gau/releases"
       "subjs=https://github.com/lc/subjs/releases"
       "httpx=https://github.com/projectdiscovery/httpx/releases"
       "python3=https://www.python.org/downloads/"
       "naabu=https://github.com/projectdiscovery/naabu/releases"
       "nuclei=https://github.com/projectdiscovery/nuclei/releases")


echo "Checking for tool installation...\n"
# Loop through the tools array
for tool_info in "${tools[@]}"; do
    tool_name="${tool_info%%=*}"
    tool_url="${tool_info#*=}"
    
    if command -v "$tool_name" >/dev/null 2>&1; then
        echo "--> $tool_name is installed."
    else
        echo -e "\033[1;31m--> $tool_name\033[0m is not installed. You can install it from \033[1;33m$tool_url\033[0m"
    fi
done
