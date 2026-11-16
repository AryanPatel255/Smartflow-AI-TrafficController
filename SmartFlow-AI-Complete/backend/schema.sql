CREATE DATABASE IF NOT EXISTS smartflow_ai;
USE smartflow_ai;
CREATE TABLE IF NOT EXISTS junctions(id VARCHAR(20) PRIMARY KEY,name VARCHAR(150) NOT NULL,vehicles INT DEFAULT 0,density VARCHAR(20) DEFAULT 'Low',signal VARCHAR(20) DEFAULT 'Red',duration INT DEFAULT 30);
INSERT INTO junctions(id,name,vehicles,density,signal,duration) VALUES
('J-04','Central Avenue',142,'High','Green',48),('J-02','Riverside Road',89,'Medium','Red',32),('J-01','Market Street',54,'Low','Green',24),('J-03','University Boulevard',117,'High','Yellow',41)
ON DUPLICATE KEY UPDATE name=VALUES(name);
