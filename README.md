# OrangeHRM testing with Pytest

We have provided a few test cases executed using pytest framework where the Login is validated for the OrangeHRM open source demo Website [OrangeHRM](https://opensource-demo.orangehrmlive.com/). The page object model design pattern is used while creating the scripts and Allure is chosen here for reporting the results.
The current code is capable of getting executed with two browsers Firefox and Chrome(provided as a part of the package). Instructions to run is provided below in usage.


**Prerequisites**

 - Machine running with a Windows OS
 - Python 3 installed on the machine
 - git is installed on the machine
 - Chrome version is running with Version 91.0.4472.77 (Official Build) (64-bit)
 - FireFox version supported is when its run on 89.0 (64-bit)
 - [Allure](https://docs.qameta.io/allure/) is installed on the machine
 - Make sure the command ```allure --version``` returns a version number in command line

## Steps to run the test cases on your machine

1) Open command prompt using cmd command
```
cmd
```
2) Create a new folder at a location you want the code to be present and run

```
mkdir Sample
```
3) Navigate into the Sample folder
```
cd Sample
```
3) Inside the Sample folder clone the repository of the code

```
git clone https://github.com/Deepak-Palamoli-Chaliyadath/OrangeHRMwithPytest.git
```

4) Create a virtual environment by using the below command at a folder where you want the test cases and code to be placed

```
pip install virtualenv
```

5) Run the command
 
```
virtualenv mypython
```

6) Activate the below command for windows 
```
mypython\Scripts\activate
``` 
7) Navigate into the Project folder OrangeHRMwithPytest
```
cd OrangeHRMwithPytest
``` 
8) All the libraries required for the test suite are run using the below command
```
pip install -r requirement.txt
```

9) The below command is used to Execute the test cases in command line 
```
pytest Tests --alluredir=Reports
```

10) The below command is used after the execution for displaying the allure report on your browser
```
allure serve Reports 
```

## Usage information

- The browser can be changed from the file CommonData under Pages folder.
- Changing the text of error messages column in the Excel file can provide an example for failed test cases
