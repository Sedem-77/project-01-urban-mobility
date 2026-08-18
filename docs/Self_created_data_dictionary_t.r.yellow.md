| Variable              | Meaning | Type      | Role               | Concerns |
| --------------------- | ------- | --------- | ------------------ | -------- |
| VendorID              |         | integer   | identifier         |          |
| tpep_pickup_datetime  |         | date/time | temporal           |          |
| tpep_dropoff_datetime |         | date/time | temporal           |          |
| passenger_count       |         | float     | magnitude/weight   |          |
| trip_distance         |         | float     | predictor/outcome  |          |
| RatecodeID            |         | float     | identifier         |          |
| store_and_fwd_flag    |         | string    | data quality       |          |
| PULocationID          |         | integer   | spatial            |          |
| DOLocationID          |         | integer   | spatial            |          |
| payment_type          |         | integer   | monetary indicator |          |
| fare_amount           |         | float     | monetary           |          |
| extra                 |         | float     | monetary           |          |
| mta_tax               |         | float     | monetary           |          |
| tip_amount            |         | float     | monetary           |          |
| tolls_amount          |         | float     | monetary           |          |
| improvement_surcharge |         | float     | monetary           |          |
| total_amount          |         | float     | monetary           |          |
| congestion_surcharge  |         | float     | monetary           |          |
| Airport_fee           |         | float     | monetary           |          |
| cbd_congestion_fee    |         | float     | monetary           |          |