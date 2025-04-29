from pyspark.sql import SparkSession
# Initialize Spark session
spark = SparkSession.builder.appName("IoT Sensor Data").getOrCreate()

# Load CSV with inferred schema
df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)

# Filter in-range and out-of-range
in_range = df.filter((df.temperature >= 18) & (df.temperature <= 30))
out_of_range = df.filter((df.temperature < 18) | (df.temperature > 30))

print(f"In-range count: {in_range.count()}")
print(f"Out-of-range count: {out_of_range.count()}")

# Aggregation by location
agg_df = df.groupBy("location").agg(
    {"temperature": "avg", "humidity": "avg"}
).withColumnRenamed("avg(temperature)", "avg_temperature") \
 .withColumnRenamed("avg(humidity)", "avg_humidity") \
 .orderBy("avg_temperature", ascending=False)

agg_df.show()

# Save to CSV
agg_df.write.csv("task2_output.csv", header=True, mode="overwrite")
