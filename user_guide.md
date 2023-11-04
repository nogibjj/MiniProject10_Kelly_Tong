### User Guide for ETL Query Tool
#### Purpose
The purpose of this repository is to perform a streamline actions of extract, transform_load, and query through ETL pipeline tools. Setup tools are applied to setup the packages automatically. This is a user guide for how to perform these tasks step by step. 
A Cloud Database (MySQL) is hosted in Azure and connected to this Github repository 
through secret variables access_tokens, host_name and HTTP_path. 
Two csv files are extracted from two source url. 
Then they are cleaned, transformed and loaded into 2 .db files. 
Complex Query is performed to join the two datasets based on the desired order and
their common variables. Joined table will be generated automatically. 
In these case, the two datasets (csv files) are extracted into women_stem.db and 
all_ages.db which store the information about major and employment. 
This Github action allows extract, transform and load. and query to be performed 
seperately in codespace. It also enables flexibility in performing these in single command.

#### Preparation
`Github Repository`
* Fork MiniProject6_KellyTong repository
* Use the same dataset urls as the ones in Mini-Project 6. The datasets chose are women_stem.csv and all_ages.csv.

`Azure Database`
* Create a new data warehouse named mini-project 7
* Record Tokens, Host name, and HTTP path

`Environment`
* Save Tokens, Host name and HTTP path in secrets and variables for both actions and codespaces in order to connect the repository (as well as codespaces) with Azure Database

`Packaging in setup.py`
* Create a python file named setup.py
* Package all the python scripts into the package "ETLKellyTong"

#### Installation
* Clone repository using "git clone" in order to access the repository locally
* Requirements.txt contains all the packages required for the repository
* Install packages by pip install setup.py

#### Functions
`Extract`
* Extract data from url to csv files and pushed automatically to the repository

`Transform_load`
* Transform data and load it into database

`Query`
* Perform general and complex query

#### Data communication
The data is currently set up to communicate with Azure Databricks database.

#### Troubleshooting and Debuging
* Make sure all secrets are saved correctly in the settings
* Make sure all dependencies are installed (double check the requirement.txt file for this) 
* Make sure Azure Databricks Database has been started and is running
* Make sure to git pull before git push again

