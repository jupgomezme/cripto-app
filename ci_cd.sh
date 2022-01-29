cd /var/www/html || exit
sudo git pull origin master
cd backend || exit
pip3 install --user -r requirements.txt
