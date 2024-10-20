WITH stg_job_ads AS (
    SELECT * FROM {{ source('job_ads', 'stg_job_ads') }}
)
SELECT
    id,
    experience_required,
    driving_license_required AS driving_license,
    access_to_own_car,
    webpage_url
FROM stg_job_ads
