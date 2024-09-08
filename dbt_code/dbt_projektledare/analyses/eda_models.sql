-- Check if ID column in dim_auxiliary_attributesis unique
WITH dim_auxiliary_attributes AS (
    SELECT * FROM {{ ref('dim_auxiliary_attributes') }}
)
SELECT
    id,
    COUNT(id) AS id_count
FROM dim_auxiliary_attributes
GROUP BY 1
ORDER BY 1 DESC;



-- Check if ID column in dim_job_details unique
WITH dim_job_details AS (
    SELECT * FROM {{ ref('dim_job_details') }}
)
SELECT
    job_details_id,
    COUNT(job_details_id) AS job_details_id_count
FROM dim_job_details
GROUP BY 1
ORDER BY 1 DESC;