#!/bin/bash
#Performs port scan using nmap

print_usage() {
cat << _EOF_
        Utility to scan open ports. Can be used to scan ports for a domain or a list of domains specified in a file.
        Example Usage:
                -h, --help              Show brief help
                -d, --domain            Domain name or ip to scan
                -f, --file              Spefify a file containing domains/IPs to scan
_EOF_
}

scan_port() {
        domain=$1
        echo "Scanning ports for $1...."
        nmap -T4 $domain | sed '/^\(Nmap scan\|PORT\|[0-9]\)/!d' | tee -a $port_scan_result_file
	echo "======================================================="
	echo " "
}

create_port_scan_result_file() {
        port_scan_result_file=port_scan.txt
	touch $port_scan_result_file
}

while getopts "f:d:" opt; do
        case "$opt" in
                d) domain=$OPTARG    ;;
                f) file=$OPTARG      ;;
                *) print_usage; exit 1 ;;
        esac
done

if [ ! -n "$domain" ] && [ ! -f "$file" ]; then
        echo "Option -d $domain or -f $file missing or designates to wrong entry" >&2
        exit 1
fi

scan_port_flow() {

if [ -n "$domain" ]; then
	create_port_scan_result_file
	scan_port $domain
	echo "Scan result:$port_scan_result_file"
fi

if [ -n "$file" ]; then
	create_port_scan_result_file
	for domain in $(cat $file)
	do
		scan_port $domain

	done
	echo "Scan result: $port_scan_result_file"
fi
}
scan_port_flow
