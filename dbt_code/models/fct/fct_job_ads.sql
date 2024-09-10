WITH src_job_ads AS (
    SELECT * FROM {{ ref('src_job_ads') }}
),
src_job_details AS (
    SELECT * FROM {{ ref('src_job_details') }}
),
src_employer AS (
    SELECT * FROM {{ ref('src_employer') }}
),
src_auxiliary_attributes AS (
    SELECT * FROM {{ ref('src_auxiliary_attributes') }}
),
dim_date_publication AS (
    SELECT 
        date_id AS publication_date_id, 
        date AS publication_date
    FROM {{ ref('dim_date') }}
),
dim_date_deadline AS (
    SELECT 
        date_id AS application_deadline_id, 
        date AS application_deadline
    FROM {{ ref('dim_date') }}
)

SELECT
    src_job_ads.id AS job_id,
    {{dbt_utils.generate_surrogate_key(['src_job_details.id', 'src_job_details.headline'])}} AS job_details_id,
    {{dbt_utils.generate_surrogate_key(['src_employer.id', 'src_employer.employer_name'])}} AS employer_id,
    {{dbt_utils.generate_surrogate_key(['src_auxiliary_attributes.id', 'src_auxiliary_attributes.employer_name'])}} AS auxiliary_attributes_id,
    COALESCE(number_vacancies, 1) AS number_vacancies,
    COALESCE(relevance, 0) AS relevance,
    dp.publication_date_id,
    dd.application_deadline_id
FROM 
    src_job_ads 
LEFT JOIN 
    src_job_details ON src_job_ads.id = src_job_details.id
LEFT JOIN 
    src_employer ON src_job_ads.id = src_employer.id
LEFT JOIN
    src_auxiliary_attributes ON src_job_ads.id = src_auxiliary_attributes.id
LEFT JOIN
    dim_date_publication dp ON src_job_ads.publication_date = dp.publication_date
LEFT JOIN
    dim_date_deadline dd ON src_job_ads.application_deadline = dd.application_deadline
