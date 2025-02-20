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
  ```

---

## 🛠️ Steps Implemented

1. **Extract:** Reads bus arrival data from `transit_data.csv`.
2. **Transform:**  
   - Converts arrival times to timestamps.  
   - Calculates **delay in minutes**.  
   - Aggregates data to find **average delays per route**.
3. **Load:** Saves **cleaned data** to a **PostgreSQL database** for further analysis.

---

## 🚀 Technologies Used
- 🐍 **Python** – Used for scripting ETL operations.
- 📊 **Pandas** – For data transformation.
- 🛢 **PostgreSQL** – For storing cleaned data.
- ⚙️ **SQLAlchemy** – For database connections.

---

## 🔧 How to Run

### **1️⃣ Set Up PostgreSQL Database**
If you haven't already, create a PostgreSQL database:
```sql
CREATE DATABASE maryland_transit;
```

Update the database connection in `etl_pipeline.py`:
```python
DB_CONNECTION = "postgresql://username:password@localhost:5432/maryland_transit"
```

### **2️⃣ Install Dependencies**
```sh
pip install pandas psycopg2 sqlalchemy
```

### **3️⃣ Run the ETL Pipeline**
```sh
python etl_pipeline.py
```

After running the script, you should see the `bus_delays` table created in PostgreSQL with average delays per route.

---

## 📊 Expected Output in Database
| route      | avg_delay_minutes |
|------------|------------------|
| Green Line | 5.0              |
| Red Line   | 5.0              |
| Blue Line  | 5.0              |

---

## 🏆 Key Skills Demonstrated
✅ **Extracting** structured data from CSV  
✅ **Transforming** timestamps & calculating delays  
✅ **Loading** into a relational database (PostgreSQL)  
✅ **SQL Querying** for analysis  

---

## 🔍 Next Steps
🔹 **Optimize for larger datasets** (handle millions of rows).  
🔹 **Enhance error handling** (handle missing or incorrect timestamps).  
🔹 **Automate ETL scheduling** with **Apache Airflow**.  

---

## 🤝 Contributing
Feel free to improve the pipeline by adding **error handling, scheduling, or performance optimizations**!
