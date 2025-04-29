from pyspark.sql.window import Window
from pyspark.sql.functions import avg, dense_rank
from pyspark.sql import SparkSession
# Initialize Spark session
spark = SparkSession.builder.appName("IoT Sensor Data").getOrCreate()

# Load CSV with inferred schema
df = spark.read.csv("sensor_data.csv", header=True, inferSchema=True)

# Avg temp per sensor
avg_temp_per_sensor = df.groupBy("sensor_id") \
    .agg(avg("temperature").alias("avg_temp"))

# Ranking
windowSpec = Window.orderBy(avg_temp_per_sensor["avg_temp"].desc())
ranked_sensors = avg_temp_per_sensor.withColumn("rank_temp", dense_rank().over(windowSpec))

# Show top 5
ranked_sensors.show(5)

# Save top 5
ranked_sensors.limit(5).write.csv("task4_output.csv", header=True, mode="overwrite")
