-- snap table: author_name, book, date, sale, to print the top three for each month each author
select t1.author_name, t1.month, t1.total from (select author_name, month(date) month, sum(sale) total from snap group by author_name, month) t1 where (select count(distinct(total)) from (select author_name, month(date) month, sum(sale) total from snap group by author_name, month) t2 where t1.month = t2.month and t1.total > t2.total) < 3 order by t1.month, t1.total

