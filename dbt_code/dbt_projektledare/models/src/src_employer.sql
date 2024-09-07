WITH stg_job_ads AS (
    SELECT * FROM {{ source('job_ads', 'stg_project_leader_job_ads') }}
)
SELECT
    id,
    EMPLOYER__NAME AS employer_name,
    EMPLOYER__WORKPLACE AS employer_workplace,
    EMPLOYER__ORGANIZATION_NUMBER AS employer_organization_number,
    WORKPLACE_ADDRESS__STREET_ADDRESS AS workplace_street_address,
    WORKPLACE_ADDRESS__REGION AS workplace_region,
    WORKPLACE_ADDRESS__POSTCODE AS workplace_postcode,
    WORKPLACE_ADDRESS__CITY AS workplace_city,
    WORKPLACE_ADDRESS__COUNTRY AS workplace_country
FROM stg_job_ads