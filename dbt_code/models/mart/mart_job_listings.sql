WITH fct_job_ads AS (
    SELECT * FROM {{ ref('fct_job_ads') }}
),
job_details AS (
    SELECT * FROM {{ ref('dim_job_details') }}
),
employer AS (
    SELECT * FROM {{ ref('dim_employer')}}
)
SELECT
    jd.headline,
    f.number_vacancies,
    jd.salary_type,
    f.relevance,
    e.employer_name,
    e.workplace_city,
    jd."description",
    jd.description_html_formatted,
    jd.duration,
    jd.scope_of_work_min,
    jd.scope_of_work_max,
    f.publication_date_id,
    f.application_deadline_id
FROM fct_job_ads AS f
LEFT JOIN job_details AS jd
    ON f.job_details_id = jd.job_details_id
LEFT JOIN employer AS e
    ON f.employer_id = e.employer_id