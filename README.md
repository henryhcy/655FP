# 655FP
# CS655 Geni Project
Chengyang He 
Qingyang Xu


1.
Reserve geni resource by creating one client and one server with VM machines, and enable public ip for them. Using our Rspec is also applicable, but sometimes will get errors with environment setup in next step.

2.
On client side, run client.sh to setup environment and get python and html files. Then, to enable CGI use, go to /etc/apache2/conf-available/cgi-enabled.conf and add lines below into the file:
<Directory “/var/www/html/cgi-enabled/”>
Options +ExecCGI
AddHandler cgi-script. py
</Directory>
After this step, restart apache2 by command: sudo systemctl restart apache2

3. 
Log in to server node and run server.sh to set up server ends. Run server.py to start server, and go to http://192.86.139.73/ to upload images for classification.
