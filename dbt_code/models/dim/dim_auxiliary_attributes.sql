WITH src_auxiliary_attributes AS (
    SELECT * FROM {{ ref('src_auxiliary_attributes') }}
)
SELECT
    {{dbt_utils.generate_surrogate_key(['id', 'employer_name'])}} AS auxiliary_attributes_id,
    COALESCE(experience_required, 'Ej specificerad') AS experience_required,
    COALESCE(driving_license, 'Ej specificerad') AS driving_license,
    COALESCE(access_to_own_car, 'Ej specificerad') AS access_to_own_car,
    COALESCE(webpage_url, 'Ej specificerad') AS webpage_url,
FROM src_auxiliary_attributes