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

