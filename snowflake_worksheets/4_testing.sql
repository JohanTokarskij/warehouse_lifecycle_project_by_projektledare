-- Test to see if warehouse, database and schemas exist
use role sysadmin;
show warehouses like 'proj_leader_ads_wh';
show databases like 'proj_leader_ads';
show schemas in database proj_leader_ads;


-- Test to see grants to roles
use role securityadmin;
show grants to role proj_leader_ads_dlt_role;
show grants to role proj_leader_ads_dbt_role;
show grants to role proj_leader_ads_reporter_role;
show grants to role proj_leader_ads_data_team_role;


-- Test to see grants to users
show grants to user dlt_user;
show grants to user dbt_user;
show grants to user reporter_user;
show grants to user emma_martini;
show grants to user johan_tokarskij;
show grants to user sermed_mohammad;
show grants to user anton_melin;
show grants to user niloofar_moosavi;


-- Test to see all users in the warehouse
use role accountadmin;
select distinct(name)
from 
    snowflake.account_usage.users
where 
    default_warehouse = 'proj_leader_ads_wh';