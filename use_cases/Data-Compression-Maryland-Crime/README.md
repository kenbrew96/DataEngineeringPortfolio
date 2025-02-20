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
```

## 🛠️ Steps Implemented
1. **Extract**: The Maryland crime data is loaded from `maryland_crime_data.csv`.
2. **Compress**: The data is compressed using the `gzip` format for efficient storage.
3. **Store**: The compressed data is saved into a `.gz` file.

## 🚀 Technologies Used
- **Pandas**: For reading and handling the crime data.
- **gzip**: For compressing the crime data file.
- **shutil**: For efficiently copying and compressing data.

## 🔧 How to Run
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/data-compression-maryland-crime.git
   cd data-compression-maryland-crime
   ```

2. **Install Dependencies**:
   Make sure to install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Compression Script**:
   Execute the script to compress the crime data:
   ```sh
   python compress_crime_reports.py
   ```

   This will:
   - Compress the `maryland_crime_data.csv` into `maryland_crime_data_compressed.csv.gz`.
   - Load the data from the original CSV file and print the first few rows.

## ✅ Next Steps
- **Verify Compression**: Check that the compressed file (`maryland_crime_data_compressed.csv.gz`) exists and is smaller than the original CSV.
- **Next Use Case**: **Data Storage Optimization**: Explore storing the compressed data on cloud storage (e.g., AWS S3 or Azure Blob Storage).

Let me know if you need any help with compression or have any questions. 🚀
```

---

With this setup, the **Data Compression for Maryland Crime Data** case is fully structured according to the given directory. Let me know if you'd like any further adjustments or clarifications!
