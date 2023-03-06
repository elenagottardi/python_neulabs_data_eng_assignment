# Task 3

## Instructions

Use the `Solution` section below to add notes about your implementation.


### Question
Given a table of brand orders with columns id, brand_id, transaction_value, and created_at representing the date and time for each transaction, write a query to get the last order for each brand for each day.

The output should include the id of the transaction, datetime of the transaction, and the transaction amount. Order the transactions by datetime.

**Example**:

Input:

orders table

| Column            | Type     |
|:-------------------|----------|
| id                | INTEGER  |
| brand_id          | INTEGER  |
| transaction_value | FLOAT    |
| created_at        | DATETIME |


Output:

| Column            | Type     |
|:-------------------|----------|
| id                | INTEGER  |
| transaction_value | FLOAT    |
| created_at        | DATETIME |

### Solution

INPUT_TABLE: orders table


WITH INPUT_TABLE_00 AS (
    SELECT
        *,
        CAST(CREATED_AT AS DATE) AS CREATED_AT_DATEPART
    FROM INPUT_TABLE
),
INPUT_TABLE_01 AS (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY CREATED_AT_DATEPART ORDER BY CREATED_AT_DATEPART ASC) AS RN
    FROM INPUT_TABLE_00
)
SELECT 
    ID,
    TRANSACTION_VALUE,
    CREATED_AT
FROM INPUT_TABLE
WHERE RN = 1
GROUP BY BRAND_ID, CREATED_AT_DATEPART