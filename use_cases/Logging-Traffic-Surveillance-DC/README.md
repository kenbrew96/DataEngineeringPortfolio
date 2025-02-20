# Logging: Traffic Surveillance in DC

## Overview
This use case demonstrates how logging is essential in monitoring traffic surveillance systems in Washington, DC. The traffic monitoring system generates logs which need to be stored, tracked, and analyzed to identify traffic patterns, unusual behaviors, system performance, and security issues.

### Components
- **Logging**: The primary focus is on setting up logging to monitor events, system activities, and performance.
- **Traffic Data**: The sample dataset (`traffic_logs.json`) contains logs from traffic cameras in DC, including timestamps, traffic volume, and anomaly detection logs.

### Tools Used
- Python
- Logging module in Python
- JSON format for storing logs

### Instructions
1. **system_logs.py**:
   This script reads traffic data from `traffic_logs.json` and processes it to track important events, such as traffic jams, accidents, or system errors. It uses Python’s built-in `logging` module to store log messages.
   
2. **traffic_logs.json**:
   A sample dataset containing records of traffic surveillance cameras. Each entry includes:
   - Camera ID
   - Timestamp
   - Traffic volume
   - Event type (e.g., "Accident", "Traffic Jam")
   
### Example Usage
```bash
python system_logs.py

