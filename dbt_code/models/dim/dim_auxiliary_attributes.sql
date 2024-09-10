WITH src_auxiliary_attributes AS (
    SELECT * FROM {{ ref('src_auxiliary_attributes') }}
)
SELECT
    {{dbt_utils.generate_surrogate_key(['id', 'employer_name'])}} AS auxiliary_attributes_id,
    experience_required,
    driving_license,
    access_to_own_car
FROM src_auxiliary_attributes