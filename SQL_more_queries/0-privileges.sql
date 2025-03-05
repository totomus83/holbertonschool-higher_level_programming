--  lists all privileges of the MySQL users 
SELECT user, host, privilege_type 
FROM information_schema.user_privileges 
WHERE user IN ('user_0d_1', 'user_0d_2');
