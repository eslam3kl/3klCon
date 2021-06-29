#!/bin/sh 

#this script was written by @eslam3kl 
#happy hacking 

#install script languages 

sudo apt-get install golang;
sudo apt-get install python3;
sudo apt-get install python3-pip;
sudo apt-get install python-pip; 
sudo apt-get install ruby;
sudo apt-get install screen;
sudo apt-get install git;
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
# >> /root/3klcon
#in directory --> word_lists , tools 

mkdir word_lists; 
mkdir tools; 
mv words.txt word_lists/; 
#install tools 

cd tools/; 

# /root/3klcon/tools

#install subfinder 
GO111MODULE=on go get -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder;
#3klcon/tools/

#install httpx 
GO111MODULE=on go get -v github.com/projectdiscovery/httpx/cmd/httpx#3klcon/tools/

#install nuclei 
GO111MODULE=on go get -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei;
#3klcon/tools/

#install nuclei-templets 
git clone https://github.com/projectdiscovery/nuclei-templates.git; 

#install naabu 
GO111MODULE=on go get -v github.com/projectdiscovery/naabu/v2/cmd/naabu;
#3klcon/tools/

#install assetfinder 
go get -u github.com/tomnomnom/assetfinder; 

#install waybackurls 
go get github.com/tomnomnom/waybackurls; 

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

#install gau 
GO111MODULE=on go get -u -v github.com/lc/gau;

#install amass 
go get -v github.com/OWASP/Amass/cmd/amass;

#install httprobe
go get -u github.com/tomnomnom/httprobe; 

#install dirsearch 
sudo apt-get install dirbuster; #to get its wordlist 
git clone https://github.com/maurosoria/dirsearch.git;

#install altdns 
pip install py-altdns; 

#install gf & gf-templete 
go get -u github.com/tomnomnom/gf;
git clone https://github.com/1ndianl33t/Gf-Patterns;
echo 'source /root/go/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc;
source ~/.bashrc;
mkdir ~/.gf;
cp -r /root/go/src/github.com/tomnomnom/gf/examples ~/.gf;
cp Gf-Patterns/*.json ~/.gf;

cp ~/go/bin/* /usr/local/bin; 
cd ../ ;

