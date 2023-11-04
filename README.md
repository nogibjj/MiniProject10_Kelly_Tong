# IDS 706 Mini Project 7

This repository is for IDS706 mini project week 7. 

## Purpose 
    This repository is for building an ETL-Query pipeline. 
    Github actions such as extract, transform and load, and query are included. 
    A local csv file is extracted from a url and then cleaned and loaded into a .db file.
    In this case, the two datasets (csv files) are extracted into women_stem.db and 
    all_ages.db which store the information about major and employment. 
    A Cloud Database (MySQL) is hosted in Azure and connected to this Github repository 
    through secret variables access_tokens, host_name and HTTP_path. 
    Setup tools are used to package the Python script. 
    
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

- ``mylib`` includes ``extract.py`` ``transform_load.py`` and ``query.py`` which are used to extract
  a csv from an url, clean it and return a db file.

## Github actions
Status badges for CI.yml
`CI.yml`
[![CI](https://github.com/nogibjj/Miniproject7_KellyTong/actions/workflows/CI.yml/badge.svg)](https://github.com/nogibjj/Miniproject7_KellyTong/actions/workflows/CI.yml)

## Results
By running command: python main.py

`extract`

<img width="466" alt="截屏2023-10-02 23 32 09" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/ff1ce85c-030f-4762-85d2-408fba3d9a37">

`transform_load`
`query`
<img width="775" alt="截屏2023-10-02 23 27 28" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/14e70102-7963-40e4-883d-d3c697ef6984">


## Building Process

The building process starts with installing the packages. 


`make install`

**Make install** calls the command pip install --upgrade pip &&\pip install -r requirements.txt

<img width="820" alt="截屏2023-10-02 23 40 02" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/ba733b30-5da5-4f44-b2c1-237813b0597c">

`make setup_package`

**Make setup_package** calls the command python setup.py develop --user

<img width="604" alt="setup_package" src="https://github.com/nogibjj/Miniproject7_KellyTong/assets/142815940/85a0d2d7-36d5-4525-87f8-c9f72002a0eb">

`make extract`

**make extract**

<img width="600" alt="截屏2023-10-02 23 35 30" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/3c644d65-ea4a-4e7a-ae3e-fcc405432b60">

`make transform_load`

**make transform_load**

<img width="257" alt="截屏2023-10-02 23 34 17" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/12959752-a54c-41cd-ae19-4c701eec414a">

`make query`

**make query**

<img width="206" alt="截屏2023-10-02 23 34 21" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/9bd70437-5329-47bb-9614-431981068365">

`make lint`

**Make lint** calls the command pylint --disable=R,C --ignore-patterns=test_.*?py *.py
<img width="457" alt="make lint" src="https://github.com/Kelly0604/miniproject2/assets/142815940/39a19764-a6cc-4eaa-977f-7433b8915dad">

`make test`

**Make test** calls the command python -m pytest -vv --cov=main test_*.py

<img width="600" alt="截屏2023-10-02 23 35 30" src="https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/44f27727-bcde-4e38-a6fb-df691f22033e">

`make format`

**Make format** calls the command black *.py

<img width="299" alt="make format" src="https://github.com/Kelly0604/miniproject2/assets/142815940/41df08ca-d8f7-4b62-b88b-1f39f1a7d858">

## Visualization for how the process work

![1_xHSzARQPes6JhHe_jNGRdg](https://github.com/nogibjj/MiniProject5_KellyTong/assets/142815940/57a7ce64-dab8-40c3-a066-87fe9862dd41)
