import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, from_unixtime


os.environ['HADOOP_HOME'] = r'C:\\hadoop-2.8.1'
os.environ['HADOOP_CONF_DIR'] = r'C:\\hadoop-2.8.1\\bin'
os.environ['PATH'] += r';C:\\hadoop-2.8.1\\bin'

def process_weather_data(input_dir, output_file):
    spark = SparkSession.builder \
        .appName("WeatherDataProcessing") \
        .getOrCreate()

    weather_data = spark.read.csv(
        os.path.join(input_dir, "*"),
        header=True,
        inferSchema=True
    )

    processed_data = weather_data.select(
        col("name").alias("LocationName"),
        from_unixtime(col("time_nano") / 1e9).alias("Timestamp"),
        col("weather_temperature").alias("Temperature_C"),
        (col("weather_windSpeed") * 3.6).alias("WindSpeed_kmh")
    )

    processed_data.coalesce(1).write.csv(output_file, sep=";", header=True, mode="overwrite")

if __name__ == "__main__":

    LOCAL_PATH = "downloaded_files"
    OUTPUT_PATH = "processed_weather_data"
    process_weather_data(LOCAL_PATH, OUTPUT_PATH)
