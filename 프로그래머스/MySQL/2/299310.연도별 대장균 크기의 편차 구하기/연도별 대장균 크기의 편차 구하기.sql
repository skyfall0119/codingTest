-- 코드를 작성해주세요
select 
    year(a.Differentiation_date) as YEAR,
    b.mx - a.size_of_colony as YEAR_DEV,
    a.ID
from ecoli_data a
    join (
        select 
            year(differentiation_date) as year,
            max(size_of_colony) as mx
        from ecoli_data
        group by year(differentiation_date)
    ) b
    on year(a.differentiation_date) = b.year
order by 
    YEAR asc,
    YEAR_DEV asc
