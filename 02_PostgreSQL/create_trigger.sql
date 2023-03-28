create trigger test_trigger after insert on USERS for each row
begin
  insert into test_table values (new.id, new.name);
end




-- Path: docs/SQL/create_view.sql
-- Compare this snippet from docs/SQL/create_table.sql:

