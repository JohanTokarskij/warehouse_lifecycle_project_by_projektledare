use role sysadmin;

create warehouse if not exists proj_leader_ads_wh
with
warehouse_size = "XSMALL"
auto_suspend = 100
auto_resume = true
initially_suspended = true
comment = "Warehouse for Project Leader job ads";

use warehouse proj_leader_ads_wh;

create database if not exists proj_leader_ads;

create schema if not exists proj_leader_ads.staging;

create schema if not exists proj_leader_ads.warehouse;

create schema if not exists proj_leader_ads.marts;