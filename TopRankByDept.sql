CREATE TABLE IF NOT EXISTS Employee (
  Id           INT,
  Name         VARCHAR(255),
  Salary       INT,
  DepartmentId INT
)
CREATE TABLE IF NOT EXISTS Department (
  Id   INT,
  Name VARCHAR(255)
)
TRUNCATE TABLE Employee
INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('1', 'Joe', '70000', '1')
INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('2', 'Henry', '80000', '2')
INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('3', 'Sam', '60000', '2')
INSERT INTO Employee (Id, Name, Salary, DepartmentId) VALUES ('4', 'Max', '90000', '1')
TRUNCATE TABLE Department
INSERT INTO Department (Id, Name) VALUES ('1', 'IT')
INSERT INTO Department (Id, Name) VALUES ('2', 'Sales')


SELECT
  d.Name AS "Department",
  a.Name AS "Employee",
  Salary AS "Salary"
FROM
  Department d

  JOIN

  (SELECT
     Name,
     Salary,
     DepartmentId,
     DENSE_RANK()
     OVER (PARTITION BY DepartmentId
       ORDER BY Salary DESC) AS ranks
   FROM Employee) a

    ON d.Id = a.DepartmentId
WHERE a.ranks <= 3
ORDER BY d.Name, Salary DESC, a.Name;
