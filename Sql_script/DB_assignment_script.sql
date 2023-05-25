CREATE DATABASE mydb;

SHOW DATABASES;
USE mydb;

CREATE TABLE COMPETITION (
ID int NOT NULL auto_increment,
Name varchar(50), 
StartDate date, 
EndDate date,
CompetitionVenue varchar(100),
Organizer varchar(100),
NumberOfLanes bit(8),
Length tinyint(50),
IndividualStartFee int,
RelayStartFee int,
Description varchar(400),
primary key(ID)
);

CREATE TABLE STATUS (
ID int NOT NULL auto_increment,
primary key (ID),
StatusText varchar(50)
);

CREATE TABLE REGISTRATIONS (
ID int NOT NULL auto_increment,
CompetitionID int,
EventNumber int, 
Name varchar(50), 
LastName varchar(50), 
Team varchar(50), 
Age int,
RegistrationTime time,
primary key (ID)
);

CREATE TABLE EVENT (
ID int NOT NULL auto_increment,
CompetitionID int,
EventNumber int, 
EventName varchar(100), 
Distance int,
Gender varchar(45),
MaxAge INT,
QualifyingTime time,
Relay bit(3),
primary key (ID),
foreign key (CompetitionID) references COMPETITION(ID)
);

CREATE TABLE ATHLEATS (
ID int NOT NULL auto_increment,
StatusID int,
EventID int,
Name VARCHAR(50),
LastName varchar(50), 
TeamName varchar(50), 
Age int,
Heat int,
Lane int,
RegistrationTime time,
ResultTime time,
primary key (ID),
foreign key (StatusID) references STATUS(ID),
foreign key (EventID) references EVENT(ID)
);

SELECT * FROM Competition;
SELECT * FROM EVENT
WHERE CompetitionID = 3;

SET GLOBAL local_infile=1;

-- Work. Cant use åäö
LOAD DATA LOCAL INFILE 'E:/Uppgifter/Databas/Competitions.txt' INTO TABLE COMPETITION 
LINES TERMINATED BY '\r\n'
(Name, StartDate, EndDate, CompetitionVenue, Organizer, NumberOfLanes, Length, IndividualStartFee, RelayStartFee, Description);

DROP DATABASE mydb;




