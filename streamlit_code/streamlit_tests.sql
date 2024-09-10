use role proj_leader_ads_reporter_role;

USE WAREHOUSE proj_leader_ads_wh;

use database proj_leader_ads;

show schemas;

use schema marts;

show views in schema marts;

show grants to ROLE proj_leader_ads_reporter_role;

show future grants to role proj_leader_ads_reporter_role;

USE SCHEMA proj_leader_ads.marts;
CREATE TABLE test (id INTEGER);
SHOW TABLES;
DROP TABLE TEST;