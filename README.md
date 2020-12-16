# feedbalancer_testing
## Python Setup
- Requires Python 3.8 or higher
- Requires pip 20.1 or higher
- Requires [pipenv](https://docs.pipenv.org/).
To install pipenv, run `pip install pipenv` (`sudo -H pip install -U pipenv` if doesnt work) from the command line.

## WebDriver Setup
- Require web driver
    - [Chromedriver]( https://sites.google.com/a/chromium.org/chromedriver/)

- Setpath for web driver
    - Windows: Create a folder named `C:\Selenium`.>> Move the executables into this folder.>>
    Add this folder to the *Path* environment variable.
    - Linux: mv /path/to/ChromeDriver /usr/local/bin

## Project Setup
- Run `pipenv install` to install the dependencies. (`pipenv update` for updated dependency)
- Run `pipenv run python -m pytest` to verify that the framework can run tests.


## pages package
- consists of locators and function to access it

## tests
- consists of different test cases to be executed
