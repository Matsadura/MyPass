-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS mypass_dev_db;
CREATE USER IF NOT EXISTS 'mypass_dev'@'localhost' IDENTIFIED BY 'mypass_dev_pwd';
GRANT ALL PRIVILEGES ON `mypass_dev_db`.* TO 'mypass_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'mypass_dev'@'localhost';
FLUSH PRIVILEGES;
