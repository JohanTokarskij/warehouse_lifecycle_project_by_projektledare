WITH stg_job_ads AS (
    SELECT * FROM {{ source('job_ads', 'stg_project_leader_job_ads') }}
)
SELECT
    id,
    NUMBER_OF_VACANCIES AS vacancies,
    relevance,
    publication_date,
    application_deadline,
    
FROM stg_job_ads