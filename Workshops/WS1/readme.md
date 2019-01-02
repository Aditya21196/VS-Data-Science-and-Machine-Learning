## Instructions for the workshop to build IMS notification system

### Requirements
What you need is an AWS account which is still free tier eligible and a SendGrid API. You will need to install putty for SSH and Filezilla for FTP to your server instance.

Putty: https://www.putty.org/
Filezilla Client: https://filezilla-project.org/download.php?type=client

The explanation for building the script is in the demo jupyter notebooks.

The task that remains is to schedule this script to run daily on your AWS server instance. Follow these steps systematically and contact me in case you have a doubt:

1) Log on to AWS. Go to Services -> EC2 console.

2) Click on create an instance. You will be provided with a list of Operating System Images to choose from. Choose Ubuntu LTS 16.04. It is the most stable linux machine you can get.

Literature on servers: Servers are machines that run 24 X 7 and by sending HTTP requests to servers, you can get HTML data. Basically that is how you "visit" a site. You just view this HTML on your browser. You can use a server for many other purposes. In this case, our server shall run a python script daily.

3) First click on "Review and Launch" straight away. You don't need to change anything default. Click on "Launch" again. You will now be given an option to choose access key for your instance.

4) Click on "create new key" and give it a random name. Save the key on to your PC.

Literature on access keys to AWS instances: AWS uses SSH keys which have the ".pem" extension. This key is used to access your server. You are supposed to keep this file secure so that random people can't access your server to configure it.

SSH: SSH stands for Secure SHell and it is a protocol using which you can control another machine remotely from your machine. It is activated by default on AWS instances. SSH onto an AWS instance requires security keys that were created while initializing that server instance.

Putty: Putty is a SSH client. We will be using it access our server. It uses files with ".ppk" for security and not ".pem" so we need to convert our ".pem" file to ".ppk" first.

Puttygen: Puttygen gets installed automatically when you install putty. You can use it convert ".pem" files to ".ppk" extension.

Filezilla: FTP client. We will use it transfer our files over to the server. We will then configure the server by tapping into in using SSH.

5) Let's first get our ".ppk" file handy. Open puttygen. Click on "Load". Browse to your ".pem" file. Now once it loads, click on "Save". Save your ".ppk" file somewhere.

6) Let's first transfer our files. Open Filezilla. Follow this video tutorial: https://www.youtube.com/watch?v=e9BDvg42-JI . Transfer the following files:

1 apikey.txt
2 script.py
3 database.csv
4 attenders.xlsx

That should be all files we need on the server.

7) Now SSH onto the server instance. Follow this short tutorial: https://www.youtube.com/watch?v=4WQe_-DAn1E

Alright now we are in boys and girls. Next step is scheduling. First, let's setup an acceptable python installation. By default, an AWS LTS 16.04 runs python 3 but does not have pip. We need pip to install packages. Execute the following series of commands to get pip:

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py --user

What the above command does is download the file that can be further used to install pip. Now run:

python get-pip.py --user

Congrats. You now have pip. Now install the modules:

pip install pandas numpy sendgrid bs4 lxml xlrd --user

pandas and numpy are modules to handle data, sendgrid is the emailing API, bs4 is to parse HTML, lxml is a HTML parser, xlrd is used to handle excel files ( The attenders list is an excel file.)

"--user" grants you the privilege to make permanent changes to your server.

Awesome. Now you even have the modules. Time to schedule the script.

Now see the time by hitting in this command:

date

Your sever sits somewhere in USA so choose a time which makes sense in this country. Suppose you choose 5 30. (Since there is an approximate lag of 9 hours, that should be about afternoon in India.) Now all you need to do is schedule the script to run at this time daily. For that we will use crontab.

Read up about it: https://www.tutorialspoint.com/unix_commands/crontab.htm

To edit crontab you type in the following command:

crontab -e

Since this is your first time using crontab, the system will ask you to choose a code editor. Choose nano by pressing 2 and then enter. Read the entire docstring of crontab. All necessary instructions on how to schedule a task is given in there.
 Append the following statement at the end of all the comments:

30 5 * * * python /home/ubuntu/script.py

This schedules your script to run at 5 30 as per server time daily. Press ctrl + X to exit and type in "Y" when asked whether if you want to save the changes and press enter.

This concludes the tutorial. Hope all the doubts were addressed. Thanks for attending guys!

Note: I have removed the names of attenders and left only mine. I don't want thee inbox of everyone to be flooded by people setting this up for themselves. Also: don't instantiate more than one AWS instance! That is beyond free tier. Also, terminate your instance before the end of one year from creating the account.
