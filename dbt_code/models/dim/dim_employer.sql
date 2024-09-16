WITH src_employer AS (
    SELECT * FROM {{ ref('src_employer') }}
)

SELECT
    {{dbt_utils.generate_surrogate_key(['id', 'employer_name'])}} AS employer_id,
    COALESCE(employer_name, 'Ej specificerad') AS employer_name,
    COALESCE(employer_workplace, 'Ej specificerad') AS employer_workplace,
    COALESCE(employer_organization_number, 'Ej specificerad') AS employer_organization_number,
    COALESCE(workplace_street_address, 'Ej specificerad') AS workplace_street_address,
    COALESCE(workplace_region, 'Ej specificerad') AS workplace_region,
    COALESCE(workplace_postcode, 'Ej specificerad') AS workplace_postcode,
    COALESCE(workplace_city, 'Ej specificerad') AS workplace_city,
    COALESCE(workplace_country, 'Ej specificerad') AS workplace_country,
    COALESCE(employer_url, 'Ej specificerad') AS employer_url
FROM src_employer