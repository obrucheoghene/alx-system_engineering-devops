-- Create user
CREATE USER "username"@"host" IDENTIFIED BY "password";

-- Grant privileges
-- All
GRANT ALL PRIVILEGES ON "database_name.*" TO "username"@"host";

-- Specific - permission to monitor replication status
GRANT REPLICATION CLIENT ON "*.*" TO "username"@"host";

-- Flust privileges
FLUSH PRIVILEGES;

-- create database
CREATE DATABASE database_name;

-- show database
SHOW DATABASES

-- Select database
USE database_name;

-- create table

CREATE TABLE nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

-- permission for user to replicate mysql server
GRANT REPLICATION SLAVE ON *.* TO "username"@"host"
