-- =============================================================================
-- Employee Management Portal — Database Setup
-- Run this file once to create the database and all required tables.
-- Usage:  source database.sql   (in MySQL CLI)
-- =============================================================================

CREATE DATABASE IF NOT EXISTS muskanproject;
USE muskanproject;

-- Master employee table (used by both admin and employee views)
CREATE TABLE IF NOT EXISTS admin (
    EmpId   VARCHAR(10)   PRIMARY KEY,
    Name    VARCHAR(50)   NOT NULL,
    Post    VARCHAR(50)   NOT NULL,
    Salary  DECIMAL(10,2) NOT NULL
);

-- Individual health/wellness tables (one per employee)
CREATE TABLE IF NOT EXISTS emp1 (
    Date   VARCHAR(20),
    Status VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS emp2 (
    Date   VARCHAR(20),
    Status VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS emp3 (
    Date   VARCHAR(20),
    Status VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS emp4 (
    Date   VARCHAR(20),
    Status VARCHAR(10)
);

-- Sample employee data
INSERT IGNORE INTO admin VALUES
    ('Emp1', 'Employee One',   'Developer',  50000.00),
    ('Emp2', 'Employee Two',   'Designer',   45000.00),
    ('Emp3', 'Employee Three', 'Analyst',    48000.00),
    ('Emp4', 'Employee Four',  'HR Manager', 52000.00);
