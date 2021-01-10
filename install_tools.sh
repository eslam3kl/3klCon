#!/usr/bin/env bash

#this script was written by @eslam3kl 
#some pieces of this code is taken form @nahamsec bbht
#happy hacking 

sudo apt-get update; 
#remove old version of go-lang 
sudo rm -rf /usr/local/go; 
sudo rm -rf /root/go; 
echo "Installing Golang"
wget -c https://golang.org/dl/go1.15.2.linux-amd64.tar.gz
shasum -a 256 go1.15.2.linux-amd64.tar.gz;
tar -C /usr/local -xvzf go1.15.2.linux-amd64.tar.gz
mkdir -p ~/go/{bin,src,pkg}
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bash_profile;
echo 'export GOPATH="/root/go"' >> ~/.bash_profile;
echo 'export GOBIN=$GOPATH/bin' >> ~/.bash_profile;
echo 'export GOROOT=/usr/local/go' >> ~/.bash_profile;
echo 'export PATH=$PATH:$GOROOT/bin' >> ~/.bash_profile;
source ~/.bash_profile
cp /usr/local/go/bin/go /usr/local/bin/; 


#sudo apt install golang-go
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

sudo add-apt-repository universe;
sudo apt install -y python2;
sudo apt install -y python;
curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py; 
sudo python2 get-pip.py; 

pip install requests; 
pip3 install requests;
pip install subprocess; 
pip install termcolor; 
pip3 install termcolor; 
pip3 install subprocess; 

mkdir word_lists; 
mkdir tools; 
mv words.txt word_lists/; 

#install tools 

#install crtfinde and 3klector 
mkdir tools/crtfinder; 
mkdir tools/3klector; 
mv crtfinder.py tools/crtfinder; 
mv 3klector.py tools/3klector; 

#change priv of bash scripts 
chmod +x scan.sh; 
chmod +x gitdorks.sh; 

cd tools/; 
# current directory --> ~/3klcon/tools

#install konan
git clone https://github.com/m4ll0k/Konan.git konan; 
cd konan && pip install -r requirements.txt; 
cd ../ 

#install photon
git clone https://github.com/s0md3v/Photon.git; 
cd Photon; 
pip install -r requirements.txt; 
cd ../

#install subfinder 
git clone https://github.com/projectdiscovery/subfinder.git; 
cd subfinder/v2/cmd/subfinder;
go build; 
cp subfinder /usr/local/bin/; 
cd ../../../../ ;
#3klcon/tools/

#install nmap 
sudo apt-get install nmap; 

#install httpx 
git clone https://github.com/projectdiscovery/httpx.git; 
cd httpx/cmd/httpx; 
go build; 
cp httpx /usr/local/bin/;
cd ../../../ ;
#3klcon/tools/

###
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

#install subjack 
go get github.com/haccer/subjack; 
cp /root/go/bin/subjack /usr/local/bin; 

#install waybackurls 
go get github.com/tomnomnom/waybackurls; 
cp /root/go/bin/waybackurls /usr/local/bin/; 

#install gitdorks 
mkdir git_dorks; 
cp ../gitdorks.sh git_dorks/;
mv ../gitdorks.sh /usr/local/bin;

#install qsreplace 
go get -u github.com/tomnomnom/qsreplace; 
cp /root/go/bin/qsreplace /usr/local/bin; 

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
snap install amass;

#install httprobe
go get -u github.com/tomnomnom/httprobe; 
cp /root/go/bin/httprobe /usr/local/bin/; 

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
cp /root/go/bin/gf /usr/local/bin/

cd ../ ;

