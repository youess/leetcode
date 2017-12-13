

Create table If Not Exists courses (student varchar(255), class varchar(255));
Truncate table courses;
insert into courses (student, class) values ('A', 'Math');
insert into courses (student, class) values ('B', 'English');
insert into courses (student, class) values ('C', 'Math');
insert into courses (student, class) values ('D', 'Biology');
insert into courses (student, class) values ('E', 'Math');
insert into courses (student, class) values ('F', 'Computer');
insert into courses (student, class) values ('G', 'Math');
insert into courses (student, class) values ('H', 'Math');
insert into courses (student, class) values ('I', 'Math');

/*
Please list out all classes which have more than or equal to 5 students.
 */

select class
from courses
group by class
having count(distinct student) >= 5;

-- more efficient way, dense_rank
select distinct class
from (
  select class
    , case when @ke != class then @dense_rank:= 1
      when @val = student then @dense_rank
      else @dense_rank:= @dense_rank + 1 end  as rnk
    , @ke := class  as ke
    , @val := student  as val
  from courses, (select @dense_rank := 0, @ke := '', @val := '') init_var
  order by class, student
) t
where rnk >= 5
;
