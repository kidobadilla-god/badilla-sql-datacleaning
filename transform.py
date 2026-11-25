import duckdb

output = duckdb.sql("""
COPY(   
        SELECT 
        DISTINCT * ,

        SPLIT_PART(browser_os, '|', 1) AS browser,
        SPLIT_PART(browser_os, '|', 2) AS os,
        
        TRIM(device_type) AS device_clean,
   
        CONCAT(browser_os, ' ', device_type) AS device_os,
        
        store_id,
        COALESCE(session_purchase_made, '0') AS purchase,
        FROM 'bronze.parquet',
    )
TO 'silver.parquet'(FORMAT PARQUET);
""")
   