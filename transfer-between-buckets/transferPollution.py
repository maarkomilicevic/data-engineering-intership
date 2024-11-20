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
AmazonS3_node1732010602608 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://destination-bucket-mm/pollution/38348 - Weg zonder naam, Amsterdam, Netherlands/"], "recurse": True}, transformation_ctx="AmazonS3_node1732010602608")

# Script generated for node Amazon S3
AmazonS3_node1732010606162 = glueContext.write_dynamic_frame.from_options(frame=AmazonS3_node1732010602608, connection_type="s3", format="csv", connection_options={"path": "s3://dest-pollution", "partitionKeys": ["location_latitude"]}, transformation_ctx="AmazonS3_node1732010606162")

job.commit()