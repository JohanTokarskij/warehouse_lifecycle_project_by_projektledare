USE ROLE ACCOUNTADMIN;

-- Grant roles to all users
grant role proj_leader_ads_dlt_role to role proj_leader_ads_dbt_role;
grant role proj_leader_ads_dbt_role to role proj_leader_ads_data_team_role;
grant role proj_leader_ads_reporter_role to role proj_leader_ads_data_team_role;
grant role proj_leader_ads_dbt_role to user dbt_user;
grant role proj_leader_ads_dlt_role to user dlt_user;
grant role proj_leader_ads_reporter_role to user reporter_user;
grant role proj_leader_ads_data_team_role to user emma_martini;
grant role proj_leader_ads_data_team_role to user johan_tokarskij;
grant role proj_leader_ads_data_team_role to user sermed_mohammad;
grant role proj_leader_ads_data_team_role to user anton_melin;
grant role proj_leader_ads_data_team_role to user niloofar_moosavi;