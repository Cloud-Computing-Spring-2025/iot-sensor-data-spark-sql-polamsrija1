from pyspark.sql.functions import round
from pyspark.sql import SparkSession
from pyspark.sql.functions import to_timestamp, hour


# Initialize Spark session
spark = SparkSession.builder.appName("IoT Sensor Data").getOrCreate()

# Load CSV with inferred schema
df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)
# Convert 'timestamp' string column to proper timestamp type (if not already)
df = df.withColumn("timestamp", to_timestamp("timestamp"))

# Extract the hour (0–23) from the timestamp
df = df.withColumn("hour_of_day", hour(df["timestamp"]))

# Confirm it worked
df.select("timestamp", "hour_of_day").show(5)

# Pivot table
pivot_df = df.groupBy("location") \
    .pivot("hour_of_day") \
    .avg("temperature") \
    .orderBy("location")

# Save pivot to CSV
pivot_df.write.csv("task5_output.csv", header=True, mode="overwrite")
