WITH INPUT_TABLE_00 AS (
    -- get date part of created_at
    SELECT
        *,
        CAST(CREATED_AT AS DATE) AS CREATED_AT_DATEPART
    FROM INPUT_TABLE
),
INPUT_TABLE_01 AS (
    -- create a row_number grouping by created_at_datepart and brand_id (I ordered for created_at_datepart descending in order to select the record with rn=1)
    SELECT
        *,
        ROW_NUMBER() OVER (PARTITION BY CREATED_AT_DATEPART, BRAND_ID ORDER BY CREATED_AT_DATEPART DESC) AS RN
    FROM INPUT_TABLE_00
)
-- get the record with the most recent created_at_datepart for each brand
SELECT
    ID,
    TRANSACTION_VALUE,
    CREATED_AT
FROM INPUT_TABLE
WHERE RN = 1
GROUP BY BRAND_ID, CREATED_AT_DATEPART
ORDER Y CREATED_AT