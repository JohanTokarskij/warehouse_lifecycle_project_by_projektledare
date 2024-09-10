-- Test to see if warehouse, database and schemas exist
use role sysadmin;
show warehouses like 'proj_leader_ads_wh';
show databases like 'proj_leader_ads';
show schemas in database proj_leader_ads;


-- Test to see grants to roles
use role securityadmin;
show grants to ROLE proj_leader_ads_dlt_role;
show grants to ROLE proj_leader_ads_dbt_role;
show grants to ROLE proj_leader_ads_reporter_role;
show grants to ROLE proj_leader_ads_data_team_role;


-- Test to see grants to users
show grants to USER dlt_user;
show grants to USER dbt_user;
show grants to USER reporter_user;
show grants to USER emma_martini;
show grants to USER johan_tokarskij;
show grants to USER sermed_mohammad;
show grants to USER anton_melin;
show grants to USER niloofar_moosavi;


-- Test to see all users in the warehouse
use role accountadmin;
SELECT distinct(name)
FROM 
    SNOWFLAKE.ACCOUNT_USAGE.USERS
WHERE 
    DEFAULT_WAREHOUSE = 'PROJ_LEADER_ADS_WH';