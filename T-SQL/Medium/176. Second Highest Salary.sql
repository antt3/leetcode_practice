/* Initial Solution */
IF EXISTS (
    SELECT DISTINCT
        salary AS 'SecondHighestSalary'
    FROM
        Employee
    ORDER BY
        salary DESC
    OFFSET 1 ROWS
    FETCH NEXT 1 ROWS ONLY
) BEGIN
    SELECT DISTINCT
        salary AS 'SecondHighestSalary'
    FROM
        Employee
    ORDER BY
        salary DESC
    OFFSET 1 ROWS
    FETCH NEXT 1 ROWS ONLY
END ELSE
    SELECT
        NULL AS 'SecondHighestSalary'