WITH stg_job_ads AS (
    SELECT * FROM {{ source('job_ads', 'stg_project_leader_job_ads') }}
)
SELECT
    id,
    headline,
    DESCRIPTION__TEXT AS "description",
    DESCRIPTION__TEXT_FORMATTED AS description_html_formatted,
    EMPLOYMENT_TYPE__LABEL AS employment_type,
    DURATION__LABEL AS duration,
    SALARY_TYPE__LABEL AS salary_type,
    SCOPE_OF_WORK__MAX AS scope_of_work_min,
    SCOPE_OF_WORK__MIN AS scope_of_work_max
FROM stg_job_ads