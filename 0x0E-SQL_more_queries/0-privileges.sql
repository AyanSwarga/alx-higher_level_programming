----This script lists all privileges of the MySQL users user_0d_1 
----and user_0d_2 on my server in localhost. 

SELECT * FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2') AND host = 'localhost';
