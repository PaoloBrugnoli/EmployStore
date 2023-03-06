# Query
insert_to_emp = "insert into empdetails values ( {id} , {name} , {dept} )"
update_to_emp = "update empdetails set empName = {name} , empDept = {dept} where empID = {id}"
select_to_emp = "select * from empdetails where empID = {id}"
select_all_to_emp = "select * from empdetails"
delete_to_emp = "delete from empdetails where empID = {id}"
