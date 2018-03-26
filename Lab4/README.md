# Lab session #4: Creating a web application using cloud PaaS

Course link: [ccbda-upc.github.io](https://ccbda-upc.github.io/).

Group 1207

-   Quang Duy Tran - duy9968\@gmail.com

-   Marc Garnica Caparros - marcgarnicacaparros\@gmail.com

Assignment link: [Lab 4 Assignment](https://github.com/CCBDA-UPC/Assignments-2018/blob/master/Lab04.md)
Webapp repository: [Django express webapp](https://github.com/marcgarnica13/eb-django-express-singup-base)

## Objectives

The following README summarizes the tasks done during the fourth lab session
of the Cloud Computing for Big Data Analytics course in Universitat Politècnica
de Catalunya. For project delivery and recovery of information during the course evolution.
This session uses AWS Elastic Beanstalk to build a small webapp using Django and DynamoDB. This repository only includes the comments, answers and screenshots of the session but the implementation of the app can be found in the linked [repository](https://github.com/marcgarnica13/eb-django-express-singup-base). During the following session this repository will keep track of the modifications and updates of the webapp.

### Pre-lab homeworks

-   As prerequisites for this lab session it was only required to set up correctly AWS CLI and AWS EB CLI as was shown in the [first session of this course](https://github.com/CCBDA-UPC/Cloud-Computing-QuickStart/blob/master/Quick-Start-AWS.md).

### Lab tasks

-  [x] The initial template with a basic Django webapp can be found in this [link](https://github.com/CCBDA-UPC/eb-django-express-signup-base). And it has been downloaded and pushed to the webapp [repository] (https://github.com/marcgarnica13/eb-django-express-singup-base).

-  [x] Create an IAM Policy and Role to enable the webapp access the detailed resources of AWS.
-  [x] **DynamoDB Table** Create the *gsh_signup_table* in the [AWS DynamoDB console](https://console.aws.amazon.com/dynamodb/home).

![DynamoDB setup](img/setup_dynamo.png)

-  [x] At this point we were able to run the webapp locally. The **boto3** python package is in charge of connecting to the AWS CLI and targetting the *gsg-signup-table* created. In order to run the server properly, first we install **boto3** and **django** python packages and these commands were needed:

  ```
  (eb-virt)~$ python manage.py migrate
  (eb-virt)~$ python manage.py runserver
  ```

  But in order to execute correclty Django needs three OS variables. Those can be introduced by:

  ```
  _$ export DEBUG="True"
  _$ export STARTUP_SIGNUP_TABLE="gsg-signup-table"
  _$ export AWS_REGION="eu-west-1"
  ```

  Or:
  ```
  _$ source extra-files/environment.sh
  ```

  This variables are *terminall session dependent* which means that are only specific to the current bash session (console). By closing the bash session, the variables are lost.

  Finally, this image shows hows the app runs locally and we were able to add some new records to the DynamoDB table.

![Runnng webapp locally](img/app_local.png)

![Adding new records](img/records_local.png)

-  [x] **Deploy the webapp to the AWS Beanstalk environment:** Configure correctly the new EB and deploy the webapp using the AWS EB client. Finally the EB console looked like this:

![EB console](img/eb_console.png)

  The webapp can be accesed throug this [link](http://gsgsignup-j4mtn-env.eu-west-1.elasticbeanstalk.com/) and it is consequently adding new records to the DynamoDB table.

![App deployed](img/deploy_app.png)

  The configuration was saved for future deployments.

-  [x] **First check:** Terminating the EC2 instance that the AWS uses fot the Elastic Beanstalk environment.What has happened? Why do you think that has happened? 

 After terminating the EC2 instance in EC2 console, it had been removed from environment since Beanstalk treat the instane as being crashed, environment health went from OK to Severe because there were no instances running. After a few minutes, it has added a new instance automatically and health went back to OK, the website is up again. This happens because environment type (Auto Scaling) has set the minimum instance to 1, meaning it ensures there's always at least 1 instance running.

![Auto sclaing](img/term-ec2.png)

-  [x] **Second check:** Terminate the environment from the EBS console.What has happened? Why do you think that has happened? Check both EC2 and EBS consoles.

 When environment is starting to terminate, it removes the auto scaling group policy then terminates the running EC2 instance, and finally terminate the environment. The auto scaling policy was removed first in order to prevent it from adding new EC2 instance.
