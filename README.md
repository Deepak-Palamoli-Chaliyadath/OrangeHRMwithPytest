# OrangeHRM testing with Pytest

These are a few test cases executed using pytest on windows where the Login is validated for the OrangeHRM open Website [OrangeHRM](https://opensource-demo.orangehrmlive.com/).

**Prerequisites**

 - Machine running with a Windows OS
 - Python 3 installed on the machine
 - Chrome version is running with Version 91.0.4472.77 (Official Build) (64-bit)
 - FireFox version supported is when its run on 89.0 (64-bit)
 - [Allure](https://docs.qameta.io/allure/) is installed on the machine
 - Make sure the command ```allure --version``` returns a version number in command line

**Steps to run the test cases on your machine**
1) Create a virtual environment by using 

```
pip install virtualenv
```

2) Run the command
 
```
virtualenv mypython
```

3) Activate for windows using the below command
 
```
mypthon\Scripts\activate
``` 

4) All the libraries required for the test suite are run using the below command
```
pip install -r requirements.txt
```

5) The below command is used to Execute the test cases in command line 
```
pytest Tests --alluredir=Reports
```

6) The below command is used after the execution for displaying the allure report on your browser
```
allure serve Reports 
```

