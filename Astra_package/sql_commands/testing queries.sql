insert into pharmacy_info
value
('testing1','Adhar card','234134213','stefe','werwer',8088123098,8088123098,"bhd",);


use  testingdatabase;

desc login_info;

alter table login_info
drop user_id;

alter table login_info
drop foreign key login_info_ibfk_3;

alter table login_info
add column user_id varchar(20) not null;