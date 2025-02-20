# 🚦 Logging Traffic Surveillance in DC

## 📌 Project Overview
This project is focused on logging **traffic surveillance** data collected from various sources in Washington, DC. The data consists of traffic incidents and other relevant traffic events that are logged and stored for analysis and record-keeping.

## 📊 Dataset
The dataset, `traffic_logs.json`, contains the following fields:
- `incident_id`: A unique identifier for each incident.
- `location`: The location where the incident occurred.
- `timestamp`: The date and time the incident occurred.
- `severity`: The severity of the incident (e.g., High, Medium, Low).
- `incident_type`: The type of traffic event (e.g., Accident, Traffic Jam, Broken Down Vehicle).

### Example Data:
```json
[
  {
    "incident_id": "T1001",
    "location": "14th Street NW & U Street NW",
    "timestamp": "2025-02-01 08:15:00",
    "severity": "High",
    "incident_type": "Accident"
  },
  {
    "incident_id": "T1002",
    "location": "Constitution Avenue NW & 17th Street NW",
    "timestamp": "2025-02-01 08:20:00",
    "severity": "Medium",
    "incident_type": "Traffic Jam"
  },
  {
    "incident_id": "T1003",
    "location": "K Street NW & 12th Street NW",
    "timestamp": "2025-02-01 08:30:00",
    "severity": "Low",
    "incident_type": "Broken Down Vehicle"
  }
]
```

## 🛠️ Steps Implemented
1. **Extract**: The traffic incident data is loaded from `traffic_logs.json`.
2. **Log**: The traffic incidents are logged into a log file (`traffic_incidents.log`) using Python's built-in logging library.

## 🚀 Technologies Used
- **JSON**: Format for traffic incident data.
- **Python**: Script for logging traffic data and incidents.
- **Logging**: Python logging library for storing logs.

## 🔧 How to Run
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/your-username/smart-city-traffic-logging.git
   cd smart-city-traffic-logging
   ```

2. **Install Dependencies**:
   Make sure to install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the Traffic Logging Script**:
   Execute the script to log the traffic incidents:
   ```sh
   python system_logs.py
   ```

   This will:
   - Extract data from `traffic_logs.json`.
   - Log traffic incidents into the `traffic_incidents.log` file.

## ✅ Next Steps
- **Verify Log Files**: Check that the `traffic_incidents.log` file has been populated correctly.
- **Next Use Case**: **Analyzing Traffic Incidents**: Use machine learning to predict high-risk traffic areas based on incident data.

Let me know if you need help setting up logging or have any questions. 🚀
```

---

With this setup, the **Logging Traffic Surveillance in DC** case is fully structured according to the given directory. Let me know if further adjustments are needed!
