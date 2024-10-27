# End-to-end-Object-Detection-Project


## Workflows
 
- constants
- config_entity
- artifact_entity
- components
- pipeline
- app.py




## Project Configuration

```bash
#install aws cli from the following link

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
```

```bash
#Configure aws crediential (secret key & access key)

aws configure
```


```bash
#Create a s3 bucket for model pusher. name is mentioned in the consrtant

```



## How to run:

```bash
conda create -n signlang python=3.8 -y
```

```bash
conda activate signlang
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```




'''
deployment process using aws with jenkinsfile cicd pipelien.

.github\workflows\main.yaml-> in this path write a workflow

.jenkins\Jenkinsfile-> in this path write jenkinsfile code and update the dockercompose url with your own dockercompose url from github.

scripts\ec2_setup.sh-> write code for these path files
scripts\jenkins.sh-> write code for these path files

also write dockerfile and docker-compose file.

than go to aws and launch the ec2 machine all the process in present in other readme.md on github and go to the cli of ec2.

scripts\jenkins.sh-> in this path copy all the command and paste it in ec2 cli. go to the link that mention after 2nd command and paste it copy all the command and paste it in ec2 cli, make sure the last command is to install jenkins after install jenkins command neglect all the commands. than run rest of commnads present in this path -> scripts\jenkins.sh. when you run the aws cinfigure command you need to give secret, access key and regin.than restart the terminal. for restart the terminal follow these steps. cancle this terminal and go to ec2 machine and than instance and click on reboot instance and stop the instance. than connect to the machine.
than go ec2-> security option->  security groups -> edit inbound rules-> click add roles-> give port 8080 -> and this one 0.0.0.0/0 -> and save all things. go ec2 go to instance and copy the url its working fine.
#set elastic IP: go to instance-> left sidebar click on elastic IP -> allocate elastic ip-> click allocate-> Associate elastic IP-> slect the instace like jinkins machine-> click associate.
copy the ip address from instance and add port number 8080 and search i new tab you wil see the jinkens server.
than copy the url in this jinkens page. go to this path scripts\jenkins.sh and replace the url with new one in the last comand. than copy the last command and paste it in ec2 cli.ec2 cli give me a password copy the password and paste it in jinkens page and continue. than install suggested plugins. -> create First Admin User --> save and contineou.-> in nistance configuration you see the jinkens url and save and finsh and start using jinkens.
click on Manage jenkins->Plugins-> Avalaable Plugins->search ssh Agent -> install-> check mark on restrat button when installition is completed.

jinkens dashboard click on Manage jinkens->crediential-> system-> global credentials ->add credential.-> kind should secret text-> first of all give the ID ECR_REPOSITORY.-> go to aws and create ECR and copy the url-> go to jenkis page i am previously working and there paste the url in Secret input.->click create

add second secret-> kind is secret text-> give ID AWS_ACCOUNT_ID -> go to aws account and copy the account ID and paste in secret input

add secret-> kind is secret text -> ID is AWS_ACCESS_KEY_ID-> also paste AWS_ACCESS_KEY_ID secret input

add secret-> kind is secret text -> ID is AWS_SECRET_ACCESS_KEY -> also paste AWS_SECRET_ACCESS_KEY secret input

add secret-> kind is ssh user name with private key ->ID is ssh_key ->Enter key directly-> when you create ec2 machine where you download the file calledsomething like jenkins may be, so from there copy the url and paste in key-> create

*** now move for creating the pipeline ***
in jinkens dashboard -> click on new item-> give pipeline name -> and click on pipeline-> ok-> than select the pipeline defination ->source control managment-> select SCM is git.-> write you repo url-> change branch to main branch-> write the jenkinsfile path in source path like .jenkins/Jenkinsfile  -> save


*** now move for creating EC2 Instance ***
the process is already mention in previous readme.md and after that reach on ec2 cli.-> than run all the comand one by one that present in this path scripts/ec2_setup.sh



## Now setup elastic IP on AWS
go to instance and left sibe bar select elastic ip -> allocate elastic ip-> associate -> in instance select macine like sign machine or you created right now -> associate
go to instance you creat and copy the public ip and replace in jinkens file like line no 50


## now add github crediential. already mention step by step process in previous readme.md
go to github and add name is URL and secret section copy the url of jenkins dashboard and paste it.-> add secret

new secret-> USER-> your jenkins server user name-> add secret

new secret-> TOKEN-> go to jinkens and click on profile and there click on configure and in api token generate api token and copy the token and paste in github secret--> add secret

new secret-> JOBS-> go to jenkins Dashboard and copy the name of project like sign project-> add secret

