#!/bin/bash
yum update -y
yum install -y httpd
yum install git -y
systemctl start httpd
systemctl enable httpd
cd /var/www || exit
rm -rf html
git clone https://github.com/jupgomezme/cripto-app.git
mv cripto-app html
cd html/backend || exit
pip3 install -r requirements.txt
nohup uvicorn index:app  --reload --host 0.0.0.0 --port 8000 &