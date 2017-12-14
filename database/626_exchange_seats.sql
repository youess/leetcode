
-- insert data
Create table If Not Exists seat(id int, student varchar(255));
Truncate table seat;
insert into seat (id, student) values ('1', 'Abbot');
insert into seat (id, student) values ('2', 'Doris');
insert into seat (id, student) values ('3', 'Emerson');
insert into seat (id, student) values ('4', 'Green');
insert into seat (id, student) values ('5', 'Jeames');

/*
交换相邻的两行
 */

select a.id
  , case when a.id mod 2 then
      case when b.student is null then a.student else b.student end
      else c.student end as student
from seat a
  left join seat b on a.id + 1 = b.id and b.id mod 2 = 0
  left join seat c on a.id - 1 = c.id and c.id mod 2 != 0
order by a.id
;

-- official solution
SELECT
    s1.id, COALESCE(s2.student, s1.student) AS student
FROM
    seat s1
        LEFT JOIN
    seat s2 ON ((s1.id + 1) ^ 1) - 1 = s2.id
ORDER BY s1.id;

drop table seat;