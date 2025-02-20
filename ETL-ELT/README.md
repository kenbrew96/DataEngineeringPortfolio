# ETL-ELT Pipeline

This directory contains examples of ETL (Extract, Transform, Load) and ELT (Extract, Load, Transform) pipelines.

## Files:
- `etl_pipeline.py`: A simple ETL pipeline that extracts data from a CSV, transforms it, and loads it into an SQLite database.
- `elt_pipeline.py`: An ELT pipeline where the data is loaded into a database first and transformed later.

### Usage:
1. Install dependencies: 
    ```bash
    pip install pandas sqlalchemy
    ```
2. Run the ETL pipeline: 
    ```bash
    python etl_pipeline.py
    ```
3. For the ELT pipeline, run:
    ```bash
    python elt_pipeline.py
    ```

### Overview:
- **ETL**: Data is extracted, transformed, and then loaded into the database.
- **ELT**: Data is loaded first into the database, and transformation happens afterward.

