import os
from dotenv import load_dotenv
from snowflake.connector import connect
import pandas as pd

def query_job_listings(query = 'select * from mart_job_listings'):
    load_dotenv()
    
    with connect(
        user = os.getenv("snowflake_user"), 
        password=os.getenv("snowflake_password"), 
        account=os.getenv("snowflake_account"),
        warehouse = os.getenv("snowflake_warehouse"),
        database = os.getenv("snowflake_database"),
        schema = os.getenv("snowflake_schema"),
        role = os.getenv("snowflake_role")
    ) as conn:
        
        df = pd.read_sql(query, conn)
        return df
    
print(query_job_listings())