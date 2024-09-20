WITH src_job_details AS (
    SELECT * FROM {{ ref('src_job_details') }}
)
SELECT
    {{ dbt_utils.generate_surrogate_key(['id','headline']) }} AS job_details_id, 
    COALESCE(headline, 'Ej specificerad') AS headline,
    COALESCE(job_description, 'Ej specificerad') AS job_description,
    COALESCE(description_html_formatted, 'Ej specificerad') AS description_html_formatted,
    COALESCE(employment_type, 'Ej specificerad') AS employment_type,
    COALESCE(duration, 'Ej specificerad') AS duration,
    COALESCE(salary_type, 'Ej specificerad') AS salary_type,
    scope_of_work_min,
    scope_of_work_max
FROM src_job_details