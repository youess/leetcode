
--  Rank Scores, when got tie set the same and count next
SELECT os.Score, count(us.Score) Rank FROM Scores os,
(
  SELECT DISTINCT Score FROM Scores
) us WHERE us.Score >= os.Score
GROUP BY os.id
ORDER BY os.Score DESC;

SELECT Score, Rank FROM (
  SELECT @rank := IF(@prevScore > Score, @rank + 1, @rank) Rank,
    @prevScore := Score AS prevScore
  FROM Scores, (SELECT @rank := 1, @prevScore := -1) init
  ORDER BY Score DESC
) t;

--  Consecutive Nums, three
SELECT DISTINCT Num as ConsecutiveNums FROM (
  SELECT Num, @count := IF(@pre = Num, @count + 1, 1) AS n, @pre := Num
  FROM Logs, (SELECT @count := 0, @pre := -1) AS init
) AS t WHERE t.n >= 3;

--  Employees Earning More than Their managers
SELECT e1.Name AS Employee FROM Employee e1 LEFT JOIN Employee e2
ON (e1.ManagerId = e2.Id)
WHERE e1.Salary > e2.Salary;

-- Duplicate Email
SELECT Email FROM (
  SELECT Email, count(1) AS num FROM Person
  GROUP BY Email
) e WHERE e.num > 1;

--  Customers Who Never Order
SELECT c.Name as Customers FROM Customers c
  LEFT JOIN Orders o ON (c.Id = o.CustomerId)
  WHERE o.Id is null;

--  Department Highest Salary
SELECT D.Name AS Department, E.Name AS Employee, E.Salary FROM Employee AS E, Department AS D
WHERE E.DepartmentId = D.Id AND Salary >= ALL(
  SELECT Salary FROM Employee E_TMP
  WHERE E_TMP.DepartmentId = E.DepartmentId
);

SELECT D.Name Department, E1.Name Employee, E1.Salary FROM Employee E1
RIGHT JOIN (
  SELECT MAX(E.Salary) M_Salary, E.DepartmentId FROM Employee E
  GROUP BY E.DepartmentId
) EM ON (E1.Salary = EM.M_Salary AND E1.DepartmentId = EM.DepartmentId)
INNER JOIN Department D ON (D.Id = E1.DepartmentId);

--  Department Top Three Salaries
SELECT D.Name Department, t.Name Employee, t.Salary FROM (
  SELECT DepartmentId,
    Name,
    Salary,
    @rank := IF(@preDeptId != DepartmentId, 1,
      IF(@preSal = Salary, @rank, @rank + 1)) AS Rank,
    @preDeptId := DepartmentId AS preDeptId,
    @preSal := Salary AS preSal
  FROM Employee E, (SELECT @rank := 0, @preDeptId := NULL, @preSal := NULL) Init
  ORDER BY DepartmentId ASC, Salary DESC
) t INNER JOIN Department D
ON (t.DepartmentId = D.Id)
Where t.Rank <= 3;

--  Delete Duplicate Emails
--  DELETE p1 FROM Person p1 INNER JOIN Person p2
--  WHERE p1.Email = p2.Email AND p1.Id > p2.Id;
DELETE FROM p1 USING Person p1 INNER JOIN Person p2
WHERE p1.Email = p2.Email AND p1.Id > p2.Id;

--  Rising Temperature
SELECT Id FROM (
  SELECT CASE
    WHEN Temperature > @pretemp AND DATEDIFF(Date, @predate) = 1
      THEN Id
    ELSE NULL END AS Id,
      @pretemp := Temperature,
      @predate := Date
    FROM Weather, (SELECT @pretemp := NULL, @predate := NULL) Init
    ORDER BY Date ASC
) AS D WHERE Id is NOT NULL;

--  Trips and Users
SELECT request_at Day, ROUND(
  SUM(IF(Status = 'completed', 0, 1)) / COUNT(1), 2
) AS `Cancellation Rate` FROM Trips t
LEFT JOIN Users u ON (u.Users_Id = t.Client_Id)
WHERE u.Banned <> "Yes" AND
  t.Request_at >= "2013-10-01" AND t.Request_at <= "2013-10-03"
GROUP BY request_at;

SELECT request_at Day, ROUND(
  SUM(IF(Status = 'completed', 0, 1)) / COUNT(1), 2
) AS `Cancellation Rate` FROM Trips t
WHERE Exists(
  Select Users_Id FROM Users u
  WHERE u.Users_Id = t.Client_Id
    AND u.Banned <> "Yes"
) AND t.Request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY request_at;
