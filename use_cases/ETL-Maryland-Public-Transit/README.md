# 🚌 Maryland Public Transit ETL Pipeline

## 📌 Project Overview
The Maryland Transit Administration (MTA) needs an **ETL pipeline** to track **bus delays** and optimize scheduling.

This project extracts bus transit data from a CSV file, transforms it to calculate **average delays per route**, and loads the cleaned data into a **PostgreSQL database** for further analysis.

---

## 📊 Dataset
- **File:** `transit_data.csv`
- **Contents:** Contains **bus stop times, GPS locations, and delays.**
- **Sample Data:**
  ```csv
  bus_id,route,stop_name,arrival_time,scheduled_time,delay_minutes
  101,Green Line,Lexington Market,08:05:00,08:00:00,5
  102,Red Line,Penn Station,09:15:00,09:10:00,5
  103,Blue Line,Inner Harbor,10:30:00,10:25:00,5
  104,Green Line,Lexington Market,12:45:00,12:40:00,5

