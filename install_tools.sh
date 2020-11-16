#!/usr/bin/env bash

#this script was written by @eslam3kl 
#some pieces of this code is taken form @nahamsec bbht
#happy hacking 


#install go-lang 
if [[ -z "$GOPATH" ]];then
echo "It looks like go is not installed, would you like to install it now"
PS3="Please select an option : "
choices=("yes" "no")
select choice in "${choices[@]}"; do
        case $choice in
                yes)

					echo "Installing Golang"
					wget https://dl.google.com/go/go1.13.4.linux-amd64.tar.gz
					sudo tar -xvf go1.13.4.linux-amd64.tar.gz
					export GOROOT=~/go
					export GOPATH=~/go
					export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
					echo 'export GOROOT=/root/go' >> ~/.bash_profile;echo 'export GOPATH=$HOME/go'	>> ~/.bash_profile			
					echo 'export PATH=$GOPATH/bin:$GOROOT/bin:$PATH' >> ~/.bash_profile	
					source ~/.bash_profile
					sleep 1
					break
					;;
				no)
					echo "Please install go and rerun this script"
					echo "Aborting installation..."
					exit 1
					;;
	esac	
done
fi

#install script languages 
sudo apt-get install -y python3;
sudo apt-get install -y python3-pip;
sudo apt-get install -y python-pip; 
sudo apt-get install -y ruby;
sudo apt-get install -y screen;
sudo apt-get install -y git;
sudo apt-get install -y jq;
sudo apt-get install -y ruby-full;
sudo apt-get install -y libcurl4-openssl-dev libxml2 libxml2-dev libxslt1-dev ruby-dev build-essential libgmp-dev zlib1g-dev;
sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev;
sudo apt-get install -y python-setuptools;
sudo apt-get install -y libldns-dev;
sudo apt-get install -y python-dnspython;
sudo apt-get install -y rename;
sudo apt-get install -y xargs;
pip install requests; 
pip3 install requests;
pip install subprocess; 
pip install termcolor; 


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
naabu 
gf 
gf-templetes
nuclei 
nuclei-templets 
s3scanner 
subjack 
webpwn3r
scan.sh
----------
'''

mkdir word_lists; 
mkdir tools; 
mv words.txt word_lists/; 

#install tools 

#install crtfinde and 3klector 
mkdir tools/crtfinder; 
mkdir tools/3klector; 
mv crtfinder.py tools/crtfinder; 
mv 3klector.py tools/3klector; 


cd tools/; 
# current directory --> ~/3klcon/tools

#install subfinder 
git clone https://github.com/projectdiscovery/subfinder.git; 
cd subfinder/v2/cmd/subfinder;
go build; 
cp subfinder /usr/local/bin/; 
cd ../../../../ ;
#3klcon/tools/

#install httpx 
git clone https://github.com/projectdiscovery/httpx.git; 
cd httpx/cmd/httpx; 
go build; 
cp httpx /usr/local/bin/;
cd ../../../ ;
#3klcon/tools/

#install nuclei 
git clone https://github.com/projectdiscovery/nuclei.git; 
cd nuclei/v2/cmd/nuclei/; 
go build; 
cp nuclei /usr/local/bin/; 
cd ../../../../ ;
#3klcon/tools/

#install nuclei-templets 
git clone https://github.com/projectdiscovery/nuclei-templates; 

#install assetfinder 
go get -u github.com/tomnomnom/assetfinder; 
cp /root/go/bin/assetfinder /usr/local/bin/; 

#install waybackurls 
go get github.com/tomnomnom/waybackurls; 
cp /root/go/bin/waybackurls /usr/local/bin/; 

#install githound 
git clone https://github.com/tillson/git-hound;
cd git-hound/; 
go build; 
cp git-hound /usr/local/bin ;
echo 'github_username:' > config.yml ; 
echo 'github_password:' >> config.yml ;
cd ../ ;
#you will need to enter your credentials into the config.yml file 

#install gitdorks 
mkdir git_dorks; 
cp ../gitdorks.sh git_dorks/;
mv ../gitdorks.sh /usr/local/bin; 

#install port_scanner 
mkdir port_scan; 
cp ../scan.sh port_scan/;
mv ../scan.sh /usr/local/bin; 

#install subjck 
go get github.com/haccer/subjack; 
cp /root/go/bin/subjack /usr/local/bin;


#install gau 
GO111MODULE=on go get -u -v github.com/lc/gau 
cp /root/go/bin/gau /usr/local/bin; 

#install amass 
apt-get install amass; 

#install httprobe
go get -u github.com/tomnomnom/httprobe; 
cp /root/go/bin/httprobe /usr/local/bin/; 

#install dirsearch 
sudo apt-get install -y dirbuster; #to get its wordlist 
git clone https://github.com/maurosoria/dirsearch.git;

#install altdns 
pip install py-altdns; 

#install gf & gf-templete 
go get -u github.com/tomnomnom/gf;
git clone https://github.com/1ndianl33t/Gf-Patterns;
echo 'source /root/go/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc;
source ~/.bashrc;
sleep 1; 
mkdir ~/.gf;
cp -r /root/go/src/github.com/tomnomnom/gf/examples ~/.gf;
cp Gf-Patterns/*.json ~/.gf;

cd ../ ;

