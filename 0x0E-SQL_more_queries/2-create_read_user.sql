--  holberton task
CREATE DATABASE IF NOT EXISTS `hbtn_0d_2`;

--  holberton task
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
            IDENTIFIED BY 'user_0d_2_pwd';

--  holberton task
GRANT SELECT
          ON `hbtn_0d_2`.*
          TO 'user_0d_2'@'localhost';
