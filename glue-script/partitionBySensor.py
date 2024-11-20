import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1732009999287 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://destination-bucket-mm/weather/38348 - Weg zonder naam, Amsterdam, Netherlands/"], "recurse": True}, transformation_ctx="AmazonS3_node1732009999287")

# Script generated for node Amazon S3
AmazonS3_node1732010093379 = glueContext.write_dynamic_frame.from_options(frame=AmazonS3_node1732009999287, connection_type="s3", format="csv", connection_options={"path": "s3://dest-sensor", "compression": "snappy", "partitionKeys": ["location_longitude"]}, transformation_ctx="AmazonS3_node1732010093379")

job.commit()