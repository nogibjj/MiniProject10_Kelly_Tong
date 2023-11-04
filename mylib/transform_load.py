"""
Transforms and Loads data into Azure Databricks
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


# load the csv file and insert into databricks
def load(dataset="data/women_stem.csv", dataset2="data/all_ages.csv"):
    """Transforms and Loads data into the local databricks database"""
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    server_h = server_h.strip('"')
    print(f"Server Hostname: {server_h}")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        # INSERT TAKES TOO LONG
        # c.execute("DROP TABLE IF EXISTS women_stemDB")
        c.execute("SHOW TABLES FROM default LIKE 'serve*'")
        result = c.fetchall()
        # takes too long so not dropping anymore
        # c.execute("DROP TABLE IF EXISTS all_agesDB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS women_stemDB (
                    Rank int, 
                    Major_code int,
                    Major string,
                    Major_category string,
                    Total int,
                    Men int, 
                    Women int, 
                    ShareWomen int, 
                    Median int
                )
            """
            )
            # insert
            for _, row in df.iterrows():
                convert = tuple(row)
                try:
                    c.execute(f"INSERT INTO women_stemDB VALUES {convert}")
                except Exception as e:
                    print(f"Problematic row: {convert}")
                    print(f"Exception: {e}")
                    break  # Stop after the first error for easier debugging
                #c.execute(f"INSERT INTO women_stemDB VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'event*'")
        result = c.fetchall()
        # c.execute("DROP TABLE IF EXISTS all_agesDB")
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS all_agesDB (
                    Major_code int,
                    Major string,
                    Major_category string,
                    Total int,
                    Employed int, 
                    Employed_full_time_year_round int, 
                    Unemployed int,
                    Unemployment_rate int, 
                    Median int, 
                    P25th int, 
                    P75th int
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                try:
                    c.execute(f"INSERT INTO all_agesDB VALUES {convert}")
                except Exception as e:
                    print(f"Problematic row: {convert}")
                    print(f"Exception: {e}")
                    break  # Stop after the first error for easier debugging
        c.close()

    return "success"
