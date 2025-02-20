# 📡 Telemetry for Smart City - Baltimore Energy Usage

## 📌 Project Overview
This project focuses on tracking **energy usage** in **Baltimore** using data from **smart meters** installed across various locations in the city. By processing this telemetry data, we aim to optimize energy usage patterns and improve city-wide energy distribution, helping to create a more sustainable urban environment.

## 📊 Dataset
The dataset, `baltimore_energy_usage.csv`, contains the following columns:
- `meter_id`: Unique identifier for each smart meter.
- `location`: Specific areas within Baltimore (e.g., Inner Harbor, Fells Point, etc.).
- `timestamp`: Date and time when the energy usage was recorded.
- `energy_usage`: Energy consumed (in kilowatt-hours, kWh).

### Example Data:
```csv
meter_id,location,timestamp,energy_usage
001,Inner Harbor,2025-02-01 08:00:00,150
002,Fells Point,2025-02-01 08:00:00,200
003,Mount Vernon,2025-02-01 08:00:00,180
004,Inner Harbor,2025-02-01 09:00:00,145
005,Fells Point,2025-02-01 09:00:00,190
