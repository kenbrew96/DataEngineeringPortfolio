# Data Engineering Learning Guide

This guide provides a structured approach to learning data engineering, covering fundamental and advanced concepts. The directory is organized by topic, each containing scripts and explanations.

## Directory Structure
```
│── ETL-ELT/
│   ├── etl_pipeline.py
│   ├── elt_pipeline.py
│   ├── README.md
├── Cloud-Storage/
│   ├── s3_setup.py
│   ├── file_storage_setup.py
│   └── README.md
├── Logging/
│   ├── system_logs.py
│   ├── app_logs.py
│   └── README.md
├── Telemetry/
│   ├── data_collection.py
│   ├── data_transmission.py
│   └── README.md
├── Data-Formats/
│   ├── csv_example.py
│   ├── json_example.py
│   ├── parquet_example.py
│   ├── avro_example.py
│   └── README.md
├── Data-Compression/
│   ├── lossless_compression.py
│   ├── lossy_compression.py
│   └── README.md
├── Flow-Composition/
│   ├── data_pipeline.py
│   ├── airflow_example.py
│   └── README.md
├── Firewalls/
│   ├── network_firewall_setup.py
│   ├── host_firewall_setup.py
│   └── README.md
├── Whitelisting/
│   ├── ip_whitelisting.py
│   ├── software_whitelisting.py
│   └── README.md
├── ACLs/
│   ├── acl_permissions.py
│   ├── acl_configuration.py
│   └── README.md
├── ATOs/
│   ├── risk_assessment.py
│   ├── system_configuration.py
│   └── README.md
├── PPSM/
│   ├── ph_protection.py
│   ├── data_classification.py
│   └── README.md
├──│   ├── ETL-Maryland-Public-Transit/
│   │   ├── etl_pipeline.py
│   │   ├── transit_data.csv  # Sample dataset
│   │   ├── README.md
│   ├── Cloud-Storage-Chesapeake-Bay/
│   │   ├── s3_upload.py
│   │   ├── sample_water_quality.json  # Sample dataset
│   │   ├── README.md
│   ├── Smart-City-Telemetry-Baltimore/
│   │   ├── telemetry_data_collection.py
│   │   ├── baltimore_energy_usage.csv  # Sample dataset
│   │   ├── README.md
│   ├── Logging-Traffic-Surveillance-DC/
│   │   ├── system_logs.py
│   │   ├── traffic_logs.json  # Sample dataset
│   │   ├── README.md
│   ├── Data-Compression-Maryland-Crime/
│   │   ├── compress_crime_reports.py
│   │   ├── maryland_crime_data.csv  # Sample dataset
│   │   ├── README.md
│   ├── Flow-Composition-School-Enrollment/
│   │   ├── airflow_pipeline.py
│   │   ├── student_enrollment_data.json  # Sample dataset
│   │   ├── README.md
│   ├── Firewalls-Hospital-Security/
│   │   ├── configure_firewall.sh
│   │   ├── README.md
│   ├── Whitelisting-State-Gov-Access/
│   │   ├── ip_whitelisting.py
│   │   ├── README.md
│   ├── ACLs-University-Library-System/
│   │   ├── acl_permissions.py
│   │   ├── README.md
│   ├── ATOs-DMV-Digital-Transformation/
│   │   ├── risk_assessment.py
│   │   ├── README.md
│   ├── PPSM-Securing-Gov-Networks/
│   │   ├── configure_ports.py
│   │   ├── README.md
├── requirements.txt
└── README.md
```

## Topics Covered
### 1. ETL & ELT
- **ETL (Extract, Transform, Load)**: Traditional data processing where data is transformed before loading into a database.
- **ELT (Extract, Load, Transform)**: Modern approach where data is loaded first and then transformed within the data warehouse.

### 2. Cloud Storage
- **Amazon S3 Setup**: Configuring and using AWS S3 for data storage.
- **File Storage Setup**: Working with cloud-based and local file storage solutions.

### 3. Logging
- **System Logs**: Collecting and analyzing system-level logs.
- **Application Logs**: Tracking and managing logs from applications.

### 4. Telemetry
- **Data Collection**: Gathering telemetry data for monitoring.
- **Data Transmission**: Sending data to storage or analytics platforms.

### 5. Data Formats
- **CSV, JSON, Parquet, Avro**: Understanding various data formats and their use cases.

### 6. Data Compression
- **Lossless Compression**: Techniques for compressing data without loss.
- **Lossy Compression**: When to use lossy methods for efficiency.

### 7. Flow Composition
- **Data Pipeline Design**: Structuring efficient data workflows.
- **Apache Airflow Example**: Implementing automated pipelines with Airflow.

### 8. Security & Access Control
- **Firewalls**: Setting up network and host-level firewalls.
- **Whitelisting**: Configuring IP and software whitelisting.
- **ACLs (Access Control Lists)**: Managing permissions for data access.
- **ATOs (Authorization to Operate)**: Ensuring compliance and security approval.
- **PPSM (Port, Protocol, and Service Management)**: Protecting data through proper classification and network security.

## Getting Started
1. **Install Requirements:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Explore the topics by reading the README files** within each folder.
3. **Run the example scripts** to gain hands-on experience.

This guide aims to provide both theoretical and practical insights into data engineering. Expand your knowledge by implementing additional use cases and exploring advanced topics.
