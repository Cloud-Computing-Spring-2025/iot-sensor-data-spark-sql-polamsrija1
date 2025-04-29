# iot-sensor-data-spark-sql
# IoT Sensor Data Analysis using Spark SQL

## 📌 Overview

This project analyzes IoT sensor data using Apache Spark SQL. The data includes temperature and humidity readings from various sensors placed across multiple building floors. The analysis covers exploratory queries, filtering, aggregations, time-based insights, ranking with window functions, and pivoting for comparative analysis.

## 📁 Dataset

### `sensor_data.csv`

**Schema:**

- `sensor_id`: Unique identifier for the sensor
- `timestamp`: Date and time when the reading was recorded
- `temperature`: Temperature in Celsius
- `humidity`: Relative humidity percentage
- `location`: Physical location (e.g., BuildingA_Floor1)
- `sensor_type`: Type of sensor (e.g., TypeA, TypeB)

### 📊 Tasks Completed

#### ✅ Task 1: Load & Basic Exploration

- Loaded `sensor_data.csv` into Spark with inferred schema
- Created a temporary view `sensor_readings`
- Ran basic queries:
  - Show first 5 rows
  - Count total records
  - Get distinct locations/sensor types
- ✅ Output saved to: `task1_output.csv`

#### ✅ Task 2: Filtering & Aggregations

- Filtered data where temperature is outside 18–30°C
- Counted in-range vs. out-of-range records
- Aggregated average temperature and humidity by location
- ✅ Output saved to: `task2_output.csv`

#### ✅ Task 3: Time-Based Analysis

- Converted `timestamp` column to Spark `timestamp` type
- Extracted `hour_of_day`
- Grouped by hour to compute average temperature
- ✅ Output saved to: `task3_output.csv`

#### ✅ Task 4: Window Functions

- Computed average temperature per `sensor_id`
- Used `RANK()` to order sensors by avg temp (descending)
- Extracted top 5 hottest sensors
- ✅ Output saved to: `task4_output.csv`

#### ✅ Task 5: Pivot & Pattern Interpretation

- Created pivot table:
  - Rows = `location`
  - Columns = `hour_of_day` (0–23)
  - Values = average temperature
- Identified `(location, hour)` with highest temperature
- ✅ Output saved to: `task5_output.csv`

## 🏁 File Structure

```
.
├── sensor_data.csv
├── data_generator.py
├── task1_output.csv
├── task2_output.csv
├── task3_output.csv
├── task4_output.csv
├── task5_output.csv
├── task1.py
├── task2.py
├── task3.py
├── task4.py
├── task5.py
└── README.md
```

## 🧠 Key Learnings

- Spark SQL temp views and SQL-style queries
- Data filtering and aggregation
- Time-based analysis with timestamp parsing
- Advanced SQL functions like `RANK() OVER(...)`
- Pivoting for multi-dimensional comparisons

## ⚙️ Execution

To run any task locally:

```bash
spark-submit task1.py
spark-submit task2.py
spark-submit task3.py
spark-submit task4.py
spark-submit task5.py
```
