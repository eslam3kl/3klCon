#!/bin/bash

# subdomain enumeration
collect_subdomains() {
    local target="$1"; 
    local main_dir=$(pwd)

    mkdir "$target"
    cd "$target" || exit
    mkdir "subdomains"
    cd "subdomains" || exit

    echo -e "(*) Starting Findomain";
    findomain -o -q -t "$1" >/dev/null 2>&1; 
    
    echo -e "(*) Starting subfinder"
    subfinder -silent -d "$1" -all -recursive -o "subfinder_$1.txt" >/dev/null 2>&1;
    
    echo -e "(*) Starting assetfinder"
    assetfinder -subs-only "$1" | anew "assetfinder_$1.txt" >/dev/null 2>&1;
    
    echo -e "(*) Starting Amass"
    amass enum -passive -norecursive -d "$1" -o "amass_$1.txt" >/dev/null 2>&1; 
    
    echo -e "(*) Starting RapidDNS.io"
    curl -s "https://rapiddns.io/subdomain/$1?full=1#result" | ggrep "<td><a" | cut -d '"' -f 2 | grep http | cut -d '/' -f3 | sed 's/#results//g' | anew "rapiddns_$1.txt" >/dev/null 2>&1;
    
    echo -e "(*) Starting Riddler.io"
    curl -s "https://riddler.io/search/exportcsv?q=pld:$1" | ggrep -Po "(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew "riddler_$1.txt" >/dev/null 2>&1;
    
    echo -e "(*) Starting Archive.Org"
    curl -s "http://web.archive.org/cdx/search/cdx?url=*.$1/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e "s/\/.*//" | anew "archive_$1.txt" >/dev/null 2>&1;
    
    echo -e "(*) Starting JLDC"
    curl -s "https://jldc.me/anubis/subdomains/$1" | ggrep -Po "((http|https):\/\/)?(([\w.-]*)\.([\w]*)\.([A-z]))\w+" | anew "jldc_$1.txt" >/dev/null 2>&1;
    
    # Check if github_tokens_file exists before running github-subdomains
    if [ -s "github_tokens.txt" ]; then
        echo -e "(*) Starting GitHub-subdomains"
        github-subdomains -d "$1" -t "$github_tokens_file" -o "gitHub-subdomains_$1.txt" >/dev/null 2>&1;
    else
        echo -e "(-) GitHub tokens file ($github_tokens_file) is empty or not found. Skipping GitHub-subdomains."
    fi

    # Check if chaos token exists before running chaos
    if [ -n "$CHAOS_KEY" ]; then
        echo -e "(*) Starting Chaos"
        chaos -d "$1" -o "chaos_$1.txt" >/dev/null 2>&1;
    else
        echo -e "(-) CHAOS_KEY is empty. Skipping Chaos."
    fi
    
    cat *.txt | anew ../all_collected_subdomains.txt >/dev/null 2>&1; 


    cd ../ || exit

}

collect_subdomains_from_third_level() {
    local third_level_domains_file="$1"
    echo -e "(*) 3klCon will use Findomain, Subfinder, Assetfinder and Archive.Org tools for every subdomain"; 
    for j in $(cat "$third_level_domains_file"); do

        findomain -q -t "$j" | anew new_subdomains_from_third_level.txt >/dev/null 2>&1; 
        subfinder -silent -d "$j" -all -recursive | anew new_subdomains_from_third_level.txt >/dev/null 2>&1;
        assetfinder -subs-only "$j" | anew new_subdomains_from_third_level.txt >/dev/null 2>&1;
        curl -s "http://web.archive.org/cdx/search/cdx?url=*.$j/*&output=text&fl=original&collapse=urlkey" | sed -e 's_https*://__' -e "s/\/.*//" | anew new_subdomains_from_third_level.txt >/dev/null 2>&1; 
        echo -e "\033[1;36m-> $j ... Done.\033[0m"

    done
}

wayback_machines(){
    local subdomains_file="$1"
    echo -e "(*) 3klCon will use HakRawler and GauPlus tools for every subdomain"; 
    for k in $(cat "$subdomains_file"); do    

            echo $k | hakrawler | anew wayback_results.txt >/dev/null 2>&1;
            echo $k | gauplus | anew wayback_results.txt >/dev/null 2>&1;
            echo -e "\033[1;36m-> $k ... Done.\033[0m"

    done

    # check for interesting extensions
    cat wayback_results.txt | grep -iE ".*\.(dat|rtf|xls|ppt|sdf|odf|pptx|xlsx|exe|lnk|7z|bin|part|pdb|cgi|crdownload|ini|zipx|bak|torrent|jar|sys|deb|sh|docm|mdb|xla|zip|tar.gz|txt|json|csv|doc|docx|git|pem|bash_history|db|key|tar|log|sql|accdb|dbf|apk|cer|cfg|rar|sln|tmp|dll|iso)$" | anew interesting_files_from_wayback.txt >/dev/null 2>&1;
    # check for admin and login pages
    cat wayback_results.txt | grep -iE 'login|admin|usuarios|moderator|adm|moderator|controlpanel|affiliate' | anew admin_and_login_panel_from_wayback_record.txt >/dev/null 2>&1;

}


js_enumeration(){
    local subdomains_file="$1"
    echo -e "(*) 3klCon will use SubJS tool for every subdomain + Wayback Records";
    cat wayback_results.txt | grep -i ".*\.(js)$" | anew js_files.txt >/dev/null 2>&1;  #js_files from waybackurls records
    
    for y in $(cat "$subdomains_file"); 
    do
        # SubJS
        echo "$y" | subjs | anew js_files.txt >/dev/null 2>&1;
        echo -e "\033[1;36m-> $y ... Done.\033[0m"

    done

    # httpx
    echo "- Checking the connectivity of the file.."
    httpx -silent -l js_files.txt -stats -status-code -random-agent -o javascript_files.txt >/dev/null 2>&1;
    rm js_files.txt
 
}



main() {

    echo -e "\033[1;31m-> Domain: $i\033[0m";
    main_dir=$(pwd)
    echo -e "\033[1;32m--------------------------------------------\n[+] Start collecting Subdomains\n--------------------------------------------\033[0m"
    export CHAOS_KEY=""; # please insert your chaos key here
    github_tokens_file=github_tokens.txt; 
    collect_subdomains "$i"; 

    # Get subdomains from collected third level subdomains and filter output
    echo -e "\n\033[1;32m--------------------------------------------\n[+] Start collecting Third Level of Subdomains\n--------------------------------------------\033[0m"
    python3 $main_dir/get_third.py all_collected_subdomains.txt | anew third_level.txt >/dev/null 2>&1;
    collect_subdomains_from_third_level "third_level.txt"; 
    cat new_subdomains_from_third_level.txt | anew all_collected_subdomains.txt >/dev/null 2>&1;

    echo -e "\n\033[1;32m--------------------------------------------\n[+] Start Resolving all the subdomains\n--------------------------------------------\033[0m"
    echo -e "(*) Starting httpx with basic ports"
    httpx -silent -l all_collected_subdomains.txt -sc -cl -title -fr -o resolved_subdomains.txt >/dev/null 2>&1;
    echo -e "(*) Starting httpx with Specific Web ports 81,3000,3001,8000,8080,8443,10000,9000,9443"
    httpx -silent -l all_collected_subdomains.txt -sc -cl -title -fr -p 81,3000,3001,8000,8080,8443,10000,9000,9443 | anew resolved_subdomains.txt >/dev/null 2>&1;
    echo -e "(*) Starting Naabu with Port scan"
    naabu -silent -l all_collected_subdomains.txt -o port_scan_results.txt >/dev/null 2>&1;

    echo -e "\n\033[1;32m--------------------------------------------\n[+] Start Wayback Machines\n--------------------------------------------\033[0m"
    cat resolved_subdomains.txt | cut -d " " -f 1 | anew clear_httpx_output.txt >/dev/null 2>&1; 
    wayback_machines clear_httpx_output.txt;

    echo -e "\n\033[1;32m--------------------------------------------\n[+] Start JS files enumeration\n--------------------------------------------\033[0m"
    js_enumeration clear_httpx_output.txt; 

    echo -e "\n\033[1;32m--------------------------------------------\n[+] Start Nuclei Scan\n--------------------------------------------\033[0m"
    nuclei -silent -si 30 -stats -l clear_httpx_output.txt -es info,low -etags network -o nuclei_output.txt -rl 100; 

    cd main_dir || exit; 


}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo " "
    echo -e "\033[1;31m\t\t ______  _     _\033[0m"
    echo -e "\033[1;31m\t\t(_____ \| |   | |\033[0m"
    echo -e "\033[1;31m\t\t _____) ) |  _| | ____ ___  _____\033[0m"
    echo -e "\033[1;31m\t\t(_____ (| |_/ ) |/ ___) _ \|  _  |\033[0m"
    echo -e "\033[1;31m\t\t _____) )  _ (| ( (__| |_| | | | |\033[0m"
    echo -e "\033[1;31m\t\t(______/|_| \_)\_)____)___/|_| |_|\033[0m"
    echo " "
    echo -e "\033[1;33m\t\t\tCoded by Eslam Akl\033[0m"
    echo -e "\033[1;33m\t\tBlog: https://eslam3kl.gitbook.io\033[0m"
    echo -e "\033[1;33m\t\tGitHub: https://github.com/eslam3kl\033[0m"
    echo " "

    for i in $(cat "$1"); do
        main "$i"
    done
fi
