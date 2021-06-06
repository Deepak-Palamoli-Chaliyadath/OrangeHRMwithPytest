# OrangeHRMwithPytest

Steps to run the test case
1) Create a virtual environment by using 'pip install virtualenv'
2) virtualenv mypython
3) Activate 'mypthon\Scripts\activate' for windows and source mypython/bin/activate for Mac
4) pip install -r requirements.txt
5) pytest Tests --alluredir=Reports
6) allure serve Reports 
