# gmi-test

This is example of UI Test Automation framework


How to run

# Create and activate virtual  environment 

$pip install virtualenv (skip next step If you already have env ) 

$virtualenv –p python3  env_name 

$source env_name/bin/activate  

# Clone a code

# Install dependencies  

$pip install -r requirements.txt 

# Download driver

Download and specify in /config/custom.py a path to Chromedriver or Geckodriver

Run a Code 
Open Terminal/Command Prompt

$ pytest -s -v /test --browser='Chrome'  -> run all existing tests in chrome browser (type Firefox if you need to run there)
$ pytest -s -v /test/<path_to_test_file> --browser='Chrome'  -> run specific tests
