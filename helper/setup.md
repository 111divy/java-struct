# Git and Github
- create your github account by signiing up on [github](github.com)
- install the git tool from [this](https://git-scm.com/) site

# Setup github repository on web
- go to this url [java-struct](https://github.com/kushtency/java-struct)
- find the button to fork it and click on it 
- proceed to next step without changing anything
- after forking it the repository is now owned by you
- go to the code button and click on the https tab
- on https tab select the whole url and copy it

# Setup github repository on your computer
- open up the terminal in your windows, download it from the store
- navigate to your desktop by ```cd Desktop```
- type the command ```git clone <copied url>```
- paste the url after clone
- it will create a new folder by the name of ```java-struct```
- go inside that folder ```cd java-struct```
- type the command to check wether it is successfully cloned or not ```git status```
- if the message says on main branch and working tree clean, you repository is successfully cloned on your computer

# Getting updated changes
- check the repository on your github account everyday
- click on the fetch upstream button and update it with my repository
- after the successfull update on the web
- go in your terminal and type ```git pull``` to get all the updated files from web repository

# Upload your solutions
- the code section will consist of the questions that are to be done by you
- create a folder of your name in the code section
- create a new file in the folder and name it in the format as ```Problem<number>Week<number>.java```
- for instance problem 5 of week 1 should be in a file named as ```Problem5Week1.java```
- configure your local github account as by opening up a terminal and type the commands:
- ```git config --global user.email <youremailfor@github.com>```
- ```git config --global user.name <yourgithubusername>```
- for instance my github user name is kushtency and account email by which i have logged in is kushagra.strive@gmail.com
- ```git config --global user.email kushagra.strive@gmail.com```
- ```git config --global user.name kushtency```
- after that in the terminal just add and commit your changes after you have completely run and submitted one problem as
- ```git add ./code/<yourfoldername>/<filename>```
- ```git commit -m "<yourname>-<problem name on site>```
- for instance i have solved a problem named watermelon and the solution is in the file Problem1Week1.java
- ```git add ./code/kushagra/Problem1Week1.java```
- ```git commit -m "kushagra-watermelon```
- after that just type ```git push```
- it will redirect you to the web browser
- fill your credentials and authenticate
- now you are good to go and just push up the code on web.
