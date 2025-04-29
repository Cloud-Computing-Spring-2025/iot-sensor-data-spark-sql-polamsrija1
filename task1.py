from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("IoT Sensor Data").getOrCreate()

# Load CSV with inferred schema
df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)

# Create Temp View
df.createOrReplaceTempView("sensor_readings")

# Show first 5 rows
df.show(5)

# Count total records
total_count = df.count()
print(f"Total Records: {total_count}")

# Distinct locations
distinct_locations = spark.sql("SELECT DISTINCT location FROM sensor_readings")
distinct_locations.show()

# Save DataFrame to CSV
df.write.csv("task1_output.csv", header=True, mode="overwrite")
