use role sysadmin;


-- Give grants to the dlt role
grant usage on database proj_leader_ads to role proj_leader_ads_dlt_role;
grant usage on schema proj_leader_ads.staging to role proj_leader_ads_dlt_role;
grant usage on warehouse proj_leader_ads_wh to role proj_leader_ads_dlt_role;
grant create table on schema proj_leader_ads.staging to role proj_leader_ads_dlt_role;
grant select, insert, update, delete on all tables in schema proj_leader_ads.staging to role proj_leader_ads_dlt_role;
grant select, insert, update, delete on future tables in schema proj_leader_ads.staging to role proj_leader_ads_dlt_role;
grant insert on all tables in schema proj_leader_ads.public to role proj_leader_ads_dlt_role;
grant select on all tables in schema proj_leader_ads.public to role proj_leader_ads_dlt_role;
grant create schema on database proj_leader_ads to role proj_leader_ads_dlt_role;


--Give grants to the dbt role
use role securityadmin;
grant usage, create table, create view on schema proj_leader_ads.warehouse to role proj_leader_ads_dbt_role;
grant select, insert, update, delete on all tables in schema proj_leader_ads.warehouse to role proj_leader_ads_dbt_role;
grant select on all views in schema proj_leader_ads.warehouse to role proj_leader_ads_dbt_role;
grant select, insert, update, delete on future tables in schema proj_leader_ads.warehouse to role proj_leader_ads_dbt_role;
grant select on future views in schema proj_leader_ads.warehouse to role proj_leader_ads_dbt_role;

grant usage, create table, create view on schema proj_leader_ads.marts to role proj_leader_ads_dbt_role;
grant select, insert, update, delete on all tables in schema proj_leader_ads.marts to role proj_leader_ads_dbt_role;
grant select on all views in schema proj_leader_ads.marts to role proj_leader_ads_dbt_role;
grant select, insert, update, delete on future tables in schema proj_leader_ads.marts to role proj_leader_ads_dbt_role;
grant select on future views in schema proj_leader_ads.marts to role proj_leader_ads_dbt_role;


--Give grants to reporter
grant usage on warehouse proj_leader_ads_wh to role proj_leader_ads_reporter_role;
grant usage on database proj_leader_ads to role proj_leader_ads_reporter_role;
grant usage on schema proj_leader_ads.marts to role proj_leader_ads_reporter_role;
grant select on all tables in schema proj_leader_ads.marts to role proj_leader_ads_reporter_role;
grant select on all views in schema proj_leader_ads.marts to role proj_leader_ads_reporter_role;
grant select on future tables in schema proj_leader_ads.marts to role proj_leader_ads_reporter_role;
grant select on future views in schema proj_leader_ads.marts to role proj_leader_ads_reporter_role;