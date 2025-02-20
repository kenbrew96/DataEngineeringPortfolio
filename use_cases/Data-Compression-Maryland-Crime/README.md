# 🛡️ Data Compression for Maryland Crime Data

## 📌 Project Overview
This project demonstrates how to **compress** large crime datasets from Maryland for efficient storage. By compressing the data using formats like gzip, we reduce the file size without losing any data, making it easier to store and transfer large datasets.

## 📊 Dataset
The dataset, `maryland_crime_data.csv`, contains the following fields:
- `crime_id`: A unique identifier for each crime.
- `crime_type`: The type of crime (e.g., Assault, Theft, Burglary).
- `location`: The location where the crime took place (e.g., Baltimore, Annapolis).
- `timestamp`: The date and time when the crime occurred.

### Example Data:
```csv
crime_id,crime_type,location,timestamp
C1001,Assault,Annapolis,2025-02-01 08:00:00
C1002,Burglary,Baltimore,2025-02-01 08:15:00
C1003,Theft,Silver Spring,2025-02-01 08:30:00
C1004,Assault,Gaithersburg,2025-02-01 09:00:00
C1005,Robbery,Frederick,2025-02-01 09:30:00

