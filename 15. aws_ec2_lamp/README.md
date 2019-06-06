# AWS EC2 LAMP

Go to EC2.

Choose to launch an instance with AWS Linux AMI.

Configure Security Group; Edit the SSH to use "My IP"; Add two rules: "HTTP and HTTPS".

Create a new key pair, name and download.

Open puttygen, load public key: "publickeyname.pem", save private key.

Open putty, go to connection/SSH/Auth; Add private key for authentication.

Go to session and add in the Host name "ec2-user@thepublicdnsname" for that instance and open.

Run "sudo yum update"

Run "sudo -i"

Run "cd /var/www/html"

Run "chown ec2-user ."

Its actually "sudo chown -R -v ec2-user /var/www/html"

sudo amazon-linux-extras install -y lamp-mariadb10.2-php7.2 php7.2

sudo yum install -y httpd mariadb-server

sudo systemctl start httpd

sudo systemctl enable httpd

sudo systemctl is-enabled httpd

Test the public dns to see if apache test page is there, if so the server is up.


