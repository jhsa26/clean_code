select max(Salary) from Employee where Salary < (select max(Salary) from Employee);
select t1.Salary from (select Salary from Employee order by Salary desc limit 2) t1 order by t1.Salary limit 1
-- pay attention to renmae the table
