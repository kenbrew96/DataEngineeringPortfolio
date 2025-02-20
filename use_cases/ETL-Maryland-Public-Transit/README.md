# 🚌 Maryland Public Transit ETL Pipeline

## 📌 Project Overview
The Maryland Transit Administration (MTA) needs an **ETL pipeline** to track **bus delays** and optimize scheduling.

## 📊 Dataset
- `transit_data.csv`: Contains **bus stop times, GPS locations, and delays**.

## 🛠️ Steps Implemented
1. **Extract**: Pulls bus arrival data from `transit_data.csv`.
2. **Transform**: Filters **late arrivals** and calculates **average delays per route**.
3. **Load**: Saves **cleaned data** to a **PostgreSQL database** for analysis.

## 🚀 Technologies Used
- **Pandas** for data transformation.
- **PostgreSQL** for data storage.
- **SQLAlchemy** for database connections.

## 🔧 How to Run
```sh
python etl_pipeline.py

---

### **✅ Next Steps**
🔹 **Test the ETL script** to ensure it runs without errors.  
🔹 **Verify PostgreSQL database** to see if the table `bus_delays` is created.  
🔹 **Move to the next use case: Cloud Storage (Chesapeake Bay Water Monitoring).**  

Let me know if you need help setting up **PostgreSQL**, or if you'd like to move to the **next project!** 🚀

