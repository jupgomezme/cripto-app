cd /var/www/html || exit
git pull origin master
cd backend || exit
pip3 install -r requirements.txt
