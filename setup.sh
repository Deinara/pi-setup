apt-get update
apt-get upgrade -y
apt-get install apache2 -y
apt-get install php5 libapache2-mod-php5 -y
apt-get install mysql-server php5-mysql -y
apt-get install vsftpd -y
cp motd $HOME/.bash_profile
