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

#install naabu 
git clone https://github.com/projectdiscovery/naabu.git; 
cd naabu/v2/cmd/naabu; 
go build; 
cp naabu /usr/local/bin/; 
cd ../../../../ ; 
#3klcon/tools/

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
sudo apt-get install dirbuster; #to get its wordlist 
git clone https://github.com/maurosoria/dirsearch.git;

#install altdns 
pip install py-altdns; 

#install gf & gf-templete 
go get -u github.com/tomnomnom/gf;
git clone https://github.com/1ndianl33t/Gf-Patterns;
echo 'source /root/go/src/github.com/tomnomnom/gf/gf-completion.bash' >> ~/.bashrc;
#source ~/.bashrc;
mkdir ~/.gf;
cp -r /root/go/src/github.com/tomnomnom/gf/examples ~/.gf;
cp Gf-Patterns/*.json ~/.gf;

cd ../ ;

