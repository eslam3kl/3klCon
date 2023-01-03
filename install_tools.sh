#!/bin/sh

#this script was written by @eslam3kl
#happy hacking

#install script languages

sudo apt-get install golang
sudo apt-get install python3
sudo apt-get install python3-pip
# there is no more python-pip
# sudo apt-get install python-pip
sudo apt-get install ruby
sudo apt-get install screen
sudo apt-get install git
# there is no more pip, sho this is the same as below
# pip install requests
pip3 install requests
# can't find this subprocess anywhere
# pip install subprocess
pip3 install termcolor

cat << EOF 
'''
-----------
Tools Used
-----------
subfinder
assetfinder
amass
altdns
dirsearch
httpx
httprob
waybackurls
gau
git-hound
gitdorks.sh (build-in tool)
nmap
gf
gf-templetes
nuclei
nuclei-templets
s3scanner
subjack
webpwn3r
scan.sh
----------
 >> /root/3klcon
in directory --> word_lists , tools
'''
EOF

#install tools
cd tools/
# /root/3klcon/tools

#install subfinder
GO111MODULE=on go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

#install httpx
GO111MODULE=on go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

#install nuclei
GO111MODULE=on go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest

#install nuclei-templets
git clone https://github.com/projectdiscovery/nuclei-templates.git

#install nmap (instead of naabu)
sudo apt install nmap

#install assetfinder
# there is no "go -u flag in install"
go install github.com/tomnomnom/assetfinder@latest

#install waybackurls
go install github.com/tomnomnom/waybackurls@latest

#install githound
git clone https://github.com/tillson/git-hound
cd git-hound/
go build
cp git-hound /usr/local/bin
echo 'github_username:' > config.yml
echo 'github_password:' >> config.yml
cd ../
#you will need to enter your credentials into the config.yml file

#install gitdorks
mkdir git_dorks
cp ../gitdorks.sh git_dorks/
cp ../gitdorks.sh /usr/local/bin

#install port_scanner
mkdir port_scan
cp ../scan.sh port_scan/
cp ../scan.sh /usr/local/bin

#install subjck
go install github.com/haccer/subjack@latest

#install gau
# there is no -u flag in go install
GO111MODULE=on go install -v github.com/lc/gau@latest

#install amass
# fixing the error when installing
go install -v github.com/OWASP/Amass/v3/...@master

#install httprobe
# there is no -u flag in go install
go install github.com/tomnomnom/httprobe@latest

#install dirsearch
sudo apt-get install dirbuster -y #to get its wordlist
git clone https://github.com/maurosoria/dirsearch.git

#install altdns
pip install py-altdns

#install gf & gf-patterns
# there is no -u flag in go install
go install github.com/tomnomnom/gf@latest
git clone https://github.com/1ndianl33t/Gf-Patterns
echo 'source /root/go/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc
source ~/.bashrc
mkdir ~/.gf
cp -r /root/go/src/github.com/tomnomnom/gf/examples ~/.gf
cp Gf-Patterns/*.json ~/.gf

cp ~/go/bin/* /usr/local/bin
cd ../

