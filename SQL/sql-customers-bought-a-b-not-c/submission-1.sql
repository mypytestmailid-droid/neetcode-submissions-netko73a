-- Write your query below
-- Customers = A & B and != C 
-- 1.CTE --> Customers = A & B 2. Customers != C
-- JOIN 2 CTE's to remove customers in C 
WITH Customers_ab as (
    Select c.customer_id
        , c.customer_name
    from customers c
    join orders o
        on c.customer_id = o.customer_id
    where o.product_name IN('A','B')
    group by c.customer_id , c.customer_name
    having count(distinct o.product_name) = 2
),
Customers_c as(
    SELECT c1.customer_id
        ,c1.customer_name
    FROM customers c1
    JOIN orders o1
        on c1.customer_id = o1.customer_id
    WHERE o1.product_name = 'C'

) SELECT ab.customer_id
        , ab.customer_name
  FROM customers_ab ab
  WHERE ab.customer_id not in (SELECT DISTINCT CUSTOMER_ID
                                FROM customers_c)
 order by customer_name;
