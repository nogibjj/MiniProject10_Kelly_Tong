from setuptools import setup, find_packages

# make sure the etl script outputs properly

setup(
    name="ETLKellyTong",
    version="0.1.0",
    description="ETLpipline",
    author="Kelly Tong",
    author_email="ht117@duke.edu",
    packages=find_packages(),
    install_requires=[
        "black==22.3.0",
        "click==8.1.3",
        "pytest==7.1.3",
        "pytest-cov==4.0.0",
        "requests==2.26.0",
        "ruff==0.0.284",
        "pandas",
        "python-dotenv",
        "databricks-sql-connector",
        "setuptools",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)
