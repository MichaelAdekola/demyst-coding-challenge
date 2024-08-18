import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.sql import SQLContext
from pyspark.sql.functions import md5, col

# Initialize the Glue context
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session

# Load the data from S3
input_data = "s3://bucket-name/large_data.csv"
df = spark.read.csv(input_data, header=True)

# Anonymize the data
df_anonymized = df.withColumn('first_name', md5(col('first_name'))) \
                  .withColumn('last_name', md5(col('last_name'))) \
                  .withColumn('address', md5(col('address')))

# Save the anonymized data back to S3
output_data = "s3://bucket-name/anonymized_data.csv"
df_anonymized.write.csv(output_data, header=True)

print(f"Anonymization complete. Output saved to {output_data}.")