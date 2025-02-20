# 🌊 Chesapeake Bay Water Quality Monitoring (Cloud Storage)

## 📌 Project Overview
Environmental scientists need a **cloud-based system** to store and analyze **real-time water quality sensor data** from Chesapeake Bay.

This project **reads water quality data** from sensors and uploads it to **AWS S3** for secure cloud storage.

---

## 📊 Dataset
- **File:** `sample_water_quality.json`
- **Contents:** Water quality measurements (pH, oxygen, turbidity) recorded from multiple sensors.
- **Sample Data:**
  ```json
  [
      {
          "sensor_id": "MD-001",
          "location": "Annapolis Dock",
          "timestamp": "2024-02-20T12:00:00Z",
          "pH": 7.2,
          "oxygen_concentration": 8.5,
          "turbidity": 4.1
      }
  ]
  ```

---

## 🛠️ Steps Implemented
1. **Extract:** Reads real-time water quality data from `sample_water_quality.json`.
2. **Transform:** No major transformations needed for raw sensor data.
3. **Load:** Uploads **JSON data** to an **AWS S3 bucket** for cloud storage.

---

## 🚀 Technologies Used
- ☁️ **AWS S3** – Cloud storage solution.
- 🐍 **Python** – Used for scripting cloud uploads.
- 🛠 **Boto3** – AWS SDK for Python to interact with S3.

---

## 🔧 How to Run

### **1️⃣ Set Up AWS Credentials**
Replace `AWS_ACCESS_KEY` and `AWS_SECRET_KEY` with your AWS credentials in `s3_upload.py`.

### **2️⃣ Install Dependencies**
```sh
pip install boto3
```

### **3️⃣ Run the Upload Script**
```sh
python s3_upload.py
```

After running the script, you should see `water_quality_data.json` stored in your **AWS S3 bucket**.

---

## 📊 Expected Output in S3
| File Name                | Storage Path                                   | Size |
|--------------------------|-----------------------------------------------|------|
| water_quality_data.json  | `s3://chesapeake-water-quality/water_quality_data.json` | ~2KB |

---

## 🏆 Key Skills Demonstrated
✅ **Uploading JSON data to AWS S3**  
✅ **Using Boto3 for cloud interactions**  
✅ **Secure storage for environmental monitoring**  

---

## 🔍 Next Steps
🔹 **Automate daily uploads** using a **Lambda function**.  
🔹 **Implement data validation** before uploading.  
🔹 **Use AWS Athena** to query stored sensor data.  

---

## 🤝 Contributing
Feel free to **add error handling, logging, or automation scripts** to enhance this project!



