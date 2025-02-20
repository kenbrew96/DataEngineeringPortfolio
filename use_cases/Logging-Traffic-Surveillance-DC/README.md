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
```sh
git clone https://github.com/your-username/data-engineering-portfolio.git
cd data-engineering-portfolio







