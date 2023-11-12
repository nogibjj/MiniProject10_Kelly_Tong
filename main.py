"""
Main application entry point for PySpark data processing
"""
from mylib.lib import (
    initiate_spark_session,
    read_dataset,
    describe,
    transform_origin,
    append_to_report,
)


def run_data_analysis():
    spark = initiate_spark_session("Women Data Analysis")

    data_file_path = "data/women_stem.csv"
    women_data = read_dataset(spark, data_file_path)
    description_data = describe(women_data)
    description_data.createOrReplaceTempView("description_view")
    transformed_data = transform_origin(women_data)
    transformed_data.createOrReplaceTempView("women_data_view")
    query_result = spark.sql(
        """
        SELECT Women, COUNT(*) AS TotalWomen
        FROM women_data_view
        GROUP BY Major_category
        ORDER BY TotalWomen DESC
    """
    )

    query_result.show()
    append_to_report(
        "Spark SQL Query Result", query_result.limit(10).toPandas().to_markdown()
    )

    # query_result.write.format("csv").save("output/query_result.csv")

    spark.stop()


if __name__ == "__main__":
    run_data_analysis()
