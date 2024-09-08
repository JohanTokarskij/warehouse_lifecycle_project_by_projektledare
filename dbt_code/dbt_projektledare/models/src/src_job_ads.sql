WITH stg_job_ads AS (
    SELECT * FROM {{ source('job_ads', 'stg_project_leader_job_ads') }}
)
SELECT
    id,
    NUMBER_OF_VACANCIES AS number_vacancies,
    relevance,
    CAST(publication_date AS DATE) AS publication_date,
    CAST(application_deadline AS DATE) AS application_deadline
FROM stg_job_ads