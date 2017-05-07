select D.Name Department, E.Name Employee, E.Salary Salary from Employee E join Department D on E.DepartmentId = D.Id where (select count(distinct(e1.Salary)) from Employee e1 where e1.Salary > E.Salary and e1.DepartmentId = E.DepartmentId) < 3; 
/*
SQL is implemented as if a query was executed in the following order:

FROM clause
WHERE clause
GROUP BY clause
HAVING clause
SELECT clause
ORDER BY clause
For most relational database systems, this order explains which names (columns or aliases) are valid because they must have been introduced in a previous step.

So in Oracle and SQL Server, you cannot use a term in the GROUP BY clause that you define in the SELECT clause because the GROUP BY is executed before the SELECT clause.

There are exceptions though: MySQL and Postgres seem to have additional smartness that allows it.
*/
