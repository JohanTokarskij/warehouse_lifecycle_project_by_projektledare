WITH recursive_date AS (
    SELECT '2024-01-01'::DATE AS date_value
    UNION ALL
    SELECT dateadd(day, 1, date_value)
    FROM recursive_date
    WHERE date_value < dateadd('month', 6, current_date()) -- adding 6 months ahead for column FCT_JOB_ADS.APPLICATION_DEADLINE_ID
)
SELECT
    date_value AS date_id,
    date_value AS date,
    year(date_value) AS year,
    month(date_value) AS month,
    day(date_value) AS day,
    quarter(date_value) AS quarter,
    weekofyear(date_value) AS week_of_year,
    dayofweek(date_value) AS day_of_week
FROM recursive_date