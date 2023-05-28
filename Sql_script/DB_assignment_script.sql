CREATE DATABASE mydb;

SHOW DATABASES;
USE mydb;

CREATE TABLE COMPETITION (
ID int NOT NULL AUTO_INCREMENT,
CompName VARCHAR(255), 
StartDate DATE, 
EndDate DATE,
CompetitionVenue VARCHAR(100),
Organizer VARCHAR(100),
NumberOfLanes INT,
Length INT,
IndividualStartFee INT,
RelayStartFee INT,
Description VARCHAR(400),
primary key(ID)
);

CREATE TABLE STATUS (
ID int NOT NULL AUTO_INCREMENT,
StatusText varchar(50),
primary key (ID)
);

CREATE TABLE tblRankToLine (
	ID INT AUTO_INCREMENT,
	Size INT,
    MyRank INT,
	Line INT,
	primary key (ID)
);

CREATE TABLE REGISTRATIONS (
ID int NOT NULL AUTO_INCREMENT,
CompetitionID int,
EventNumber int, 
RegName VARCHAR(50), 
LastName VARCHAR(50), 
Team VARCHAR(50), 
Age int,
RegistrationTime time,
primary key (ID)
);

CREATE TABLE EVENT (
ID int NOT NULL auto_increment,
CompetitionID int,
EventNumber int, 
EventName VARCHAR(100), 
Distance int,
Gender VARCHAR(45),
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
AthleatName VARCHAR(50),
LastName VARCHAR(50), 
TeamName VARCHAR(50), 
Gender VARCHAR(50),
Age int,
Heat int,
Lane int,
RegistrationTime time,
ResultTime time,
primary key (ID),
foreign key (StatusID) references STATUS(ID),
foreign key (EventID) references EVENT(ID)
);

SELECT * FROM EVENT WHERE CompetitionID = 6;

SELECT * FROM Competition;
SELECT * FROM EVENT
WHERE CompetitionID = 3;

SET NAMES utf8mb4;

SET GLOBAL local_infile=1;

-- Work. Cant use åäö
LOAD DATA LOCAL INFILE 'E:/Uppgifter/Databas/Competitions.txt' INTO TABLE COMPETITION 
LINES TERMINATED BY '\r\n'
(Name, StartDate, EndDate, CompetitionVenue, Organizer, NumberOfLanes, Length, IndividualStartFee, RelayStartFee, Description);

DROP DATABASE mydb;




