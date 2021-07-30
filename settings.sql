-- settings.sql
CREATE DATABASE miniproject;
CREATE USER miniprojectuser WITH PASSWORD 'miniproject';
GRANT ALL PRIVILEGES ON DATABASE miniproject TO miniprojectuser;