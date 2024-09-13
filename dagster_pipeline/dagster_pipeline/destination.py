from dlt.destinations import snowflake
import os
from dotenv import load_dotenv

load_dotenv()

snowflake_credentials = {
    'database': os.getenv("SNOWFLAKE_DATABASE"),
    'password': os.getenv("SNOWFLAKE_PASSWORD"),
    'username': os.getenv("SNOWFLAKE_USER"),
    'host': os.getenv("SNOWFLAKE_ACCOUNT"),
    'warehouse': os.getenv("SNOWFLAKE_WAREHOUSE"),
    'role': os.getenv("SNOWFLAKE_ROLE")
    }

aw_snowflake = snowflake(credentials=snowflake_credentials)