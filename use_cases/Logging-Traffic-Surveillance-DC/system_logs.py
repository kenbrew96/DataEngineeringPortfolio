import json
import logging
import sqlite3
from datetime import datetime

# Configure logging
logging.basicConfig(filename="traffic_surveillance.log", level=logging.INFO)

def extract(log_file):
    """Extract traffic surveillance logs from a JSON file."""
    with open(log_file, 'r') as file:
        logs = json.load(file)
    logging.info("✅ Logs extracted successfully.")
    return logs

def filter_speeding(logs):
    """Filter logs to only include speeding events."""
    speeding_logs = [log for log in logs if log['event'] == 'Speeding']
    logging.info(f"✅ Found {len(speeding_logs)} speeding events.")
    return speeding_logs

def save_to_db(speeding_logs):
    """Save speeding logs into SQLite database."""
    conn = sqlite3.connect("traffic_logs.db")
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS speeding_logs (
                        timestamp TEXT,
                        camera_id TEXT,
                        location TEXT,
                        vehicle_id TEXT,
                        speed INTEGER)''')

    # Insert data
    for log in speeding_logs:
        cursor.execute('''INSERT INTO speeding_logs (timestamp, camera_id, location, vehicle_id, speed)
                          VALUES (?, ?, ?, ?, ?)''', 
                          (log['timestamp'], log['camera_id'], log['location'], log['vehicle_id'], log['speed']))
    conn.commit()
    conn.close()
    logging.info("✅ Speeding logs saved to database.")

def main():
    log_file = "traffic_logs.json"
    logs = extract(log_file)
    speeding_logs = filter_speeding(logs)
    save_to_db(speeding_logs)

if __name__ == "__main__":
    main()

