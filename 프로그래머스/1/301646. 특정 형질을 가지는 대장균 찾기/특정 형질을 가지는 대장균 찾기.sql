-- 코드를 작성해주세요
select count(*) as COUNT
from ECOLI_DATA
where right(bin(GENOTYPE),3) in ('100', '001', '1', '101')