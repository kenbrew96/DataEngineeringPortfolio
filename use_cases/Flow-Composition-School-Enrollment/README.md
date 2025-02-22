# 🔄 Data Pipeline Orchestration: Automating Maryland School Enrollment

## 📌 Project Overview
The Maryland Department of Education requires an **automated data pipeline** to process **new student enrollments** efficiently.

This project uses **Apache Airflow** to automate the extraction, transformation, and loading (ETL) of student records into a central database.

---

## 📊 Dataset
- **File:** `student_enrollment_data.json`
- **Contents:** Student names, grades, enrollment dates, and school assignments.
- **Sample Data (JSON format):**
  ```json
  [
      {
          "student_id": "MD-1001",
          "name": "John Doe",
          "grade": "10",
          "enrollment_date": "2024-08-20",
          "school": "Baltimore High"
      },
      {
          "student_id": "MD-1002",
          "name": "Jane Smith",
          "grade": "9",
          "enrollment_date": "2024-08-21",
          "school": "Annapolis Academy"
      }
  ]
  ```

---

## 🛠️ Steps Implemented
1. **Extract:** Reads student enrollment data from JSON.
2. **Transform:** Standardizes data fields and formats.
3. **Load:** Saves processed data into a **PostgreSQL database**.
4. **Orchestrate:** Automates daily pipeline execution using **Apache Airflow DAGs**.

---

## 🚀 Technologies Used
- 🌬 **Apache Airflow** – Task scheduling and orchestration.
- 🐍 **Python & Pandas** – Data extraction and transformation.
- 🛢 **PostgreSQL** – Database for storing processed enrollment records.

---

## 🔧 How to Run

### **1️⃣ Install Dependencies**
```sh
pip install apache-airflow pandas psycopg2
```

### **2️⃣ Start the Airflow Scheduler**
```sh
airflow scheduler &
```

### **3️⃣ Run the Airflow DAG**
```sh
airflow dags trigger student_enrollment_pipeline
```

### **4️⃣ Automate Pipeline Execution in `airflow_pipeline.py`**
Create an Apache Airflow DAG to automate the pipeline:
```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2

def extract():
    df = pd.read_json("student_enrollment_data.json")
    return df

def transform(df):
    df['enrollment_date'] = pd.to_datetime(df['enrollment_date'])
    return df

def load(df):
    conn = psycopg2.connect("dbname=school user=admin password=secret")
    df.to_sql("students", conn, if_exists='replace', index=False)
    conn.close()

def etl():
    df = extract()
    df = transform(df)
    load(df)

default_args = {"start_date": datetime(2024, 1, 1)}

dag = DAG("student_enrollment_pipeline", default_args=default_args, schedule_interval="@daily")

task = PythonOperator(task_id="etl_task", python_callable=etl, dag=dag)
```
Run the script:
```sh
python airflow_pipeline.py
```

After running the pipeline, **student data** will be stored in PostgreSQL and available for reporting.

---

## 📊 Expected Output in Database
| Student ID | Name       | Grade | Enrollment Date | School             |
|------------|-----------|-------|----------------|--------------------|
| MD-1001    | John Doe  | 10    | 2024-08-20     | Baltimore High    |
| MD-1002    | Jane Smith| 9     | 2024-08-21     | Annapolis Academy |

---

## 🏆 Key Skills Demonstrated
✅ **Building an automated ETL pipeline with Apache Airflow**  
✅ **Scheduling and monitoring workflows**  
✅ **Handling structured data for education systems**  

---

## 🔍 Next Steps
🔹 **Implement real-time monitoring with Airflow UI.**  
🔹 **Enhance data validation and error handling.**  
🔹 **Optimize pipeline for scalability with cloud databases.**  

---

## 🤝 Contributing
Contributions are welcome! Feel free to **add new features, improve data validation, or integrate with school APIs.**


