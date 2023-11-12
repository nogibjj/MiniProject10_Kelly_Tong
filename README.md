# IDS 706 Mini Project 10

This repository is for IDS706 mini project week 10. 

## Purpose 
    This repository is for utilizing PySpark to perform data processing such as query with a dataset named women_stem.
    The main purpose is to look into women_stem and recategorize the dataset based on major_category. 
    
## Important Things included are:
- ``.devcontainer`` includes a Dockerfile and devcontainer.json.
                The 'Dockerfile' within this folder specifies how the container should be built

- ``workflows`` includes CI.yml, which contain configuration files for setting up automated build, test, and deployment pipelines

- ``.gitignore`` is used to specify which files or directories should be excluded from version control when using Git.

- ``Makefile`` is a configuration file used in Unix-based systems for automating tasks and building software. It contains instructions and dependencies for compiling code, running tests, and other development tasks.

- ``README.md`` is the instruction file for the readers.

- ``main.py`` is a Python file. This specific main.py gets the python versions and operation system names. 

- ``requirements.txt`` is to specify the dependencies (libraries and packages) required to run the project.

- ``test_main.py`` is a test file for main.py

- ``setup.py`` setup the local packages for python, specify the dependencies required in the package. This executes the ETL streamline commands which can be called by a Makefile commnd. 

- ``mylib`` includes ``lib.py`` which specifies all the function for utilizing PySpark. 

## Github actions
Status badges for CI.yml
`CI.yml`
[![CI](https://github.com/nogibjj/MiniProject10_Kelly_Tong/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/MiniProject10_Kelly_Tong/actions/workflows/CI.yml)

## Functions
1. Loading Data: data (women_stem.csv) is loaded into a PySpark dataframe
2. Describing Data: statistics are calculated
3. Transforming Data: Data is cleaned and prepared for query
4. Spark SQL Query: Spark SQL is used to perform structured query
5. Generating data summary report: a data summary report is generated in markdown

## Building Process

The building process starts with installing the packages. 


`make install`

**Make install** calls the command pip install --upgrade pip &&\pip install -r requirements.txt

<img width="820" alt="截屏2023-10-02 23 40 02" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/ba733b30-5da5-4f44-b2c1-237813b0597c">

`make setup_package`

**Make setup_package** calls the command python setup.py develop --user

<img width="604" alt="setup_package" src="https://github.com/nogibjj/Miniproject7_KellyTong/assets/142815940/85a0d2d7-36d5-4525-87f8-c9f72002a0eb">


`make lint`

**Make lint** calls the command pylint --disable=R,C --ignore-patterns=test_.*?py *.py
<img width="457" alt="make lint" src="https://github.com/Kelly0604/miniproject2/assets/142815940/39a19764-a6cc-4eaa-977f-7433b8915dad">

`make test`

**Make test** calls the command python -m pytest -vv --cov=main test_*.py

<img width="600" alt="截屏2023-10-02 23 35 30" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/44f27727-bcde-4e38-a6fb-df691f22033e">

`make format`

**Make format** calls the command black *.py

<img width="299" alt="make format" src="https://github.com/Kelly0604/miniproject2/assets/142815940/41df08ca-d8f7-4b62-b88b-1f39f1a7d858">



## Output
Output from the query is summarized in [analysis report](https://github.com/nogibjj/MiniProject10_Kelly_Tong/blob/ede0c256655402f842a464f79432dac66e934293/analysis_report.md)
