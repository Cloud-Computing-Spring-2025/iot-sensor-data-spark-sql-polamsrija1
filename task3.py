from pyspark.sql.functions import hour, to_timestamp
from pyspark.sql import SparkSession
# Initialize Spark session
spark = SparkSession.builder.appName("IoT Sensor Data").getOrCreate()

# Load CSV with inferred schema
df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)

# Convert timestamp
df = df.withColumn("timestamp", to_timestamp("timestamp"))

# Extract hour
df = df.withColumn("hour_of_day", hour("timestamp"))

# Update temp view
df.createOrReplaceTempView("sensor_readings")

# Average temp per hour
hourly_avg = df.groupBy("hour_of_day").avg("temperature") \
    .withColumnRenamed("avg(temperature)", "avg_temp") \
    .orderBy("hour_of_day")

hourly_avg.show()

# Save to CSV
hourly_avg.write.csv("task3_output.csv", header=True, mode="overwrite")
