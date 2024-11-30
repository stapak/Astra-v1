-- 1st Query: To select department name of all the department present.
select dept_name from departments;

create user 'stapak'@'localhost' identified by 'stapak';
grant IT to 'stapak'@'localhost';


grant all on trialsone.* to 'stapak'@'localhost';
grant all on testingdatabase.* to 'stapak'@'localhost';