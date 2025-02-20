# 🚦 Traffic Surveillance Logging (Washington D.C.)

## 📌 Project Overview
This project demonstrates the use of logging to track **traffic surveillance events** such as vehicle detection, speeding violations, and traffic jams in Washington D.C.

## 📊 Dataset
- `traffic_logs.json`: Contains logs of traffic surveillance events, such as vehicle detection, speeding, and traffic congestion. Each log entry includes:
  - **timestamp**: Time the event was logged.
  - **event_type**: Type of event (e.g., speeding, vehicle detection).
  - **vehicle_id**: ID of the vehicle involved.
  - **location**: GPS coordinates or street location of the event.
  - **speed**: Speed of the vehicle (in case of speeding event).

## 🛠️ Steps Implemented

1. **Extract**: Pulls traffic logs from the `traffic_logs.json` file.
2. **Filter**: Filters the logs to only keep speeding events.
3. **Save**: Saves the filtered speeding logs into an **SQLite database** for further analysis.

## 🚀 Technologies Used
- **JSON** for storing traffic logs.
- **SQLite** for storing and querying filtered logs.
- **Python's logging module** for capturing logs of the data extraction and filtering process.

## 🔧 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/data-engineering-portfolio.git
cd data-engineering-portfolio
```

### 2. Install dependencies
Make sure you have `pip` installed, then run the following command to install all the necessary dependencies:
```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain all the libraries needed to run the project, such as:
```txt
json
sqlite3
logging
```

### 3. Run the `system_logs.py` script
Now you’re ready to run the script that handles the logging of traffic surveillance data:

```bash
python use_cases/Logging-Traffic-Surveillance-DC/system_logs.py
```

This script will:
- Extract the traffic logs from `traffic_logs.json`.
- Filter out speeding events.
- Save the filtered logs to an SQLite database (`traffic_logs.db`).

### 4. View the results
- The filtered speeding events will be stored in the `speeding_logs` table within `traffic_logs.db`.
- Log events will also be captured in a log file called `traffic_surveillance.log`.

## 💻 Expected Output
- **SQLite Database**: The script creates a SQLite database `traffic_logs.db` with a table `speeding_logs` containing the filtered speeding logs.
- **Log File**: A log file `traffic_surveillance.log` will be created, containing the following information:
  - Extracted data.
  - The filtering process of speeding events.
  - Confirmation of successful database insertion.

---

### ✅ Next Steps
- **Test the script**:  
Run the `system_logs.py` script to make sure it works correctly and logs events to both the log file (`traffic_surveillance.log`) and the SQLite database.

- **Check the SQLite database**:  
Open the SQLite database (`traffic_logs.db`) and verify that the filtered speeding logs have been saved in the `speeding_logs` table.

- **Review the log file**:  
Open the `traffic_surveillance.log` file to ensure that logs are being captured during the extraction, filtering, and saving process.

- **Explore further improvements**:  
Consider adding additional features such as:
  - Tracking and logging more event types (e.g., vehicle detection, traffic congestion).
  - Analyzing the speeding data (e.g., identifying high-risk areas for enforcement).

- **Next use case**:  
Telemetry for Smart City (Baltimore Energy Usage) — Learn how to use telemetry data to monitor energy usage patterns in Baltimore's smart city infrastructure.

---

## 🚦 **Logging Module Configuration and Customization**

### 1. Set up Logging Configuration:
You can set up custom logging configurations in the `system_logs.py` file to capture various events at different log levels (e.g., info, warning, error). This is particularly useful for tracking different parts of the ETL process or for debugging.

Example:
```python
import logging

logging.basicConfig(filename="traffic_surveillance.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("This is an info log")
logging.error("This is an error log")
```

### 2. View Log Output:
When you run the ETL process, log messages will be stored in `traffic_surveillance.log`, which you can review for:
- Progress updates (e.g., "Data extraction successful").
- Errors or issues encountered during data filtering.
- Confirmation that the data has been loaded into the SQLite database.

### 3. Customizing Log Levels:
You can customize the logging level to capture different levels of detail. For example:
- `logging.DEBUG`: Captures detailed debug messages.
- `logging.INFO`: Captures general information about the process.
- `logging.WARNING`: Captures warnings related to potential issues.
- `logging.ERROR`: Captures errors in the process.
- `logging.CRITICAL`: Captures critical errors that may halt the process.

---

### ✅ **Additional Use Cases**

- **Chesapeake Bay Water Monitoring**:  
Track water quality in Chesapeake Bay by processing telemetry data. Learn how to use sensors to monitor water temperature, pH, and other critical parameters.

- **Smart City Energy Usage (Baltimore)**:  
Monitor energy consumption data from Baltimore’s smart city infrastructure, providing insights into energy optimization.

- **Maryland Public Transit Delay Monitoring**:  
Monitor and analyze bus delays in Maryland, helping to optimize routes and improve public transportation efficiency.

Let me know if you need any adjustments or help with the next project! 🚀
```

### Changes made:
- **Step 2**: "Install dependencies" has been added with proper code formatting and is now part of the step-by-step instructions in the README.
- The rest of the sections are formatted for clarity, and the entire process is now organized in a structured and easy-to-follow format. 

You can now copy this directly into your GitHub repository's README section, and it should render correctly with all the information you need.
