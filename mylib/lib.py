from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.types import (
    StructType, 
    StructField, 
    FloatType, 
    IntegerType, 
    StringType)

REPORT_FILE = "analysis_report.md"

def append_to_report(description, content, sql_query=None):
    with open(REPORT_FILE, "a") as report:
        report.write(f"## {description}\n\n")
        if sql_query:
            report.write(f"**SQL Query:**\n```sql\n{sql_query}\n```\n\n")
        report.write("**Result Preview:**\n\n")
        report.write(f"```markdown\n{content}\n```\n\n")

def initiate_spark_session(app_title):
    session = SparkSession.builder.appName(app_title).getOrCreate()
    return session

def read_dataset(spark, dataset_path):
    women_schema = StructType([
        StructField("Rank", IntegerType(), True),  
        StructField("Major", StringType(), True),  
        StructField("Major_category", StringType(), True),  
        StructField("Total", IntegerType(), True),  
        StructField("Men", IntegerType(), True),  
        StructField("Women", IntegerType(), True), 
        StructField("ShareWomen", IntegerType(), True), 
        StructField("Median", IntegerType(), True),  
    ])
    dataset = spark.read.option("header", 
    "true").option("sep", ";").schema(women_schema).csv(dataset_path)
    append_to_report("Data Loading", dataset.limit(10).toPandas().to_markdown()) 
    return dataset

def describe(dataset):
    description = dataset.describe().toPandas().to_markdown()
    append_to_report("Data Description", description)
    return description

def transform_origin(dataset):
    major_conditions = [
        (col("Major_category") == "Engineering"),
        (col("Major_category") == "Physical Sciences"),
        (col("Major_category") == "Computers & Mathematics"),
        (col("Major_category") == "Health"),
        (col("Major_category") == "Biology & Life Science")
    ]
    major_categories = ["Engineering", "Physical Sciences", "Computers & Mathematics", 
                        "Health", "Biology & Life Science"]
    transformed_dataset = dataset.withColumn("RegionCategory", when(
        major_conditions[0], major_categories[0]
        ).when(major_conditions[1], major_categories[1]
        ).when(major_conditions[2], major_categories[2]
        ).when(major_conditions[3], major_categories[3]
        ).when(major_conditions[4], major_categories[4]
        ).otherwise("Other Majors"))
    append_to_report("Data Transformation", 
                     transformed_dataset.limit(10).toPandas().to_markdown())
    return transformed_dataset
