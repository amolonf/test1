# Credicard verification program 

How to run: ```python CreditCard.py``` 

This program is used to verify the numbers entered by the user

There are multiple criteria to check the numbers entered by the users

* The card number must start with 4 or 5 or 6 
* Other than '-' character is not allowed to enter
* Consecutive 4 same numbers are not allowed  

# Web-deploy 

Ansible repository to deploy the static web server on AWS

While designing the solution my first though was how can I divide the tasks into multiple subtask which can be written in roles

Therefore, I divided the static web-app deployment into two steps

1. Creation of instratrcture 

2. Deployment of web-app

In the creation of the infrastructire I need information about how to create VM on AWS cloud. Once you get that information then you can create the task to create the VM. For that purpose you need following information

* AWS account 
* Access and secret key to access that account
* Region and zone information where the VM will be created
* VPC information to get the local IP
* Security group in which you can access the VM through ssh, which can be acived with ingress rule 
* Also need to decide the type of the VM depeding on the users 


