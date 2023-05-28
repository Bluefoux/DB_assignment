-- Procedures and Triggers
-- StoreProcedure import registrations to Athleats
DROP PROCEDURE IF EXISTS SP_ImportRegistration;
DELIMITER ;;
CREATE PROCEDURE SP_ImportRegistration()
BEGIN
DECLARE done INT DEFAULT FALSE;
DECLARE compid, eventnum, aage, eventidto INT;
DECLARE aName, aLastName, aTeam VARCHAR(50);
DECLARE aRegistrationTime TIME;
DECLARE CurRegistration CURSOR FOR SELECT CompetitionID,EventNumber,Age,RegName,LastName,Team,RegistrationTime FROM Registrations;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

OPEN CurRegistration;
myloop: LOOP
	FETCH CurRegistration INTO compid, eventnum, aage, aName, aLastName, aTeam, aRegistrationTime;
    IF done THEN
		LEAVE myloop;
	END IF;
    
    SET eventidto = (select EVENT.ID FROM EVENT WHERE EVENT.CompetitionID = compid AND EVENT.EventNumber = eventnum LIMIT 1);
    INSERT INTO ATHLEATS (EventID, AthleatName, LastName, TeamName, Age, RegistrationTime)
    VALUES (eventidto, aName, aLastName, aTeam, aage, aRegistrationTime);
-- SELECT compid, eventnum, aage, aName, aLastName, aTeam, aRegistrationTime;
END LOOP;
CLOSE CurRegistration;
End;
;;

-- Store procedure get invoice (kinda work)
DROP PROCEDURE IF EXISTS SP_GetInvoice;
DELIMITER ;;
CREATE PROCEDURE SP_GetInvoice(compid INT)
BEGIN
DECLARE sum_invoice INT DEFAULT 0;
DECLARE invoiceperathleat INT DEFAULT 0;
SET invoiceperathleat = (SELECT IndividualStartFee FROM COMPETITION WHERE ID = compid);
SELECT ATHLEATS.TeamName, invoiceperathleat*COUNT(ATHLEATS.ID) AS InvoicePerEvent
	FROM ATHLEATS
	INNER JOIN EVENT
	ON ATHLEATS.EventID = EVENT.ID
	WHERE EVENT.CompetitionID = compid
	GROUP BY EVENT.CompetitionID, ATHLEATS.TeamName
	ORDER BY EVENT.CompetitionID, ATHLEATS.TeamName;
End;
;;

-- Generate Start List
DROP PROCEDURE IF EXISTS Generate_StartList;
DELIMITER ;;
CREATE PROCEDURE Generate_StartList(compid INT, eventid INT)
BEGIN
SELECT AthleatName, Lastname, TeamName, RegistrationTime
	FROM ATHLEATS
    INNER JOIN EVENT
	ON ATHLEATS.EventID = EVENT.ID AND EVENT.CompetitionID = compid AND ATHLEATS.EventID = eventid
	ORDER BY RegistrationTime ASC;
End;
;;

-- Get the contestents lane (based on ranking)
DROP FUNCTION IF EXISTS FN_RankToLine;
DELIMITER ;;
CREATE FUNCTION FN_RankToLine(Size INT, MyRank INT) 
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE LineVal INT;
    SELECT Line INTO LineVal
    FROM tblRankToLine
    WHERE tblRankToLine.Size = Size AND tblRankToLine.MyRank= MyRank;
    RETURN LineVal;
END;
;;

DROP PROCEDURE IF EXISTS Generate_Heatlist;
DELIMITER ;;
CREATE PROCEDURE Generate_Heatlist(compid INT, evid INT)
BEGIN
DECLARE num_of_athleats INT DEFAULT 0;
DECLARE num_of_lanes INT DEFAULT 0;
DECLARE num_of_heats INT DEFAULT 0;
DECLARE athleatID INT DEFAULT 0;
DECLARE current_heat INT DEFAULT 0;
DECLARE current_rank INT DEFAULT 0;
DECLARE current_lane INT DEFAULT 0;
DECLARE done INT DEFAULT FALSE;
DECLARE Cursorathleats CURSOR FOR SELECT ID FROM ATHLEATS WHERE EventID = evid ORDER BY RegistrationTime ASC;
DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

SET num_of_athleats = (SELECT COUNT(ATHLEATS.ID) 
FROM EVENT 
INNER JOIN ATHLEATS
ON EVENT.ID = ATHLEATS.EventID AND EVENT.CompetitionID = compid AND EVENT.ID = evid);
SET num_of_lanes = (SELECT NumberOfLanes FROM COMPETITION WHERE ID = compid);
SET num_of_heats = (SELECT CEILING(num_of_athleats / num_of_lanes));

-- SELECT num_of_athleats, num_of_lanes, num_of_heats;

OPEN Cursorathleats;
heatloop: LOOP    
    SET current_heat = (num_of_heats - (current_rank DIV num_of_lanes));
    SET current_lane = 1 + MOD(current_rank, num_of_lanes);
    SET current_lane = FN_RankToLine(num_of_lanes, current_lane);
	FETCH Cursorathleats INTO athleatID;
    IF done THEN
		LEAVE heatloop;
	END IF;
    
    UPDATE ATHLEATS
    SET Heat = current_heat, Lane = current_lane 
    WHERE ID = athleatID;
    SET current_rank = current_rank+1;
END LOOP;
CLOSE Cursorathleats;
End;
;;

-- delete event trigger (delete all athleats with eventid)
DELIMITER ;;
CREATE TRIGGER del_event BEFORE DELETE ON EVENT
FOR EACH ROW
BEGIN
	DELETE FROM ATHLEATS
    WHERE ATHLEATS.EventID = OLD.ID;
END;
;;

-- delete competition trigger (delete all events with competitionid)
DELIMITER ;;
CREATE TRIGGER del_comp BEFORE DELETE ON COMPETITION
FOR EACH ROW
BEGIN
	DELETE FROM EVENT
    WHERE EVENT.CompetitionID = OLD.ID;
END;
;;


-- call procedure
CALL SP_ImportRegistration();
CALL SP_GetInvoice(6);
CALL Generate_StartList(6, 3);
CALL Generate_Heatlist(6, 3);


SELECT * FROM ATHLEATS;
SELECT * FROM REGISTRATIONS;
SELECT * FROM EVENT;
SELECT * FROM ATHLEATS WHERE EventID = 48 ORDER BY Heat, Lane;

-- Test delete competition trigger
DELETE FROM COMPETITION
WHERE ID < 6;

-- Select to check competition
SELECT * FROM COMPETITION;

SELECT COMPETITION.*, COUNT(EVENT.ID ) FROM COMPETITION
INNER JOIN EVENT
ON COMPETITION.ID = EVENT.CompetitionID
GROUP BY EVENT.CompetitionID;

-- Select to check deleted from event and amount of athleats in each event
SELECT EVENT.*, COUNT(ATHLEATS.ID ) FROM EVENT
INNER JOIN ATHLEATS
ON EVENT.ID = ATHLEATS.EventID
GROUP BY ATHLEATS.EventID;

SELECT * FROM ATHLEATS;

DELETE FROM EVENT
WHERE ID = 4;

-- Select to check table
SELECT * FROM ATHLEATS;
SELECT * FROM COMPETITION;
SELECT * FROM EVENT;

SELECT EVENT.CompetitionID, COUNT(ATHLEATS.ID), ATHLEATS.TeamName, 100*COUNT(ATHLEATS.ID) AS Invoice
FROM ATHLEATS
INNER JOIN EVENT
ON ATHLEATS.EventID = EVENT.ID
GROUP BY EVENT.CompetitionID, ATHLEATS.TeamName
ORDER BY EVENT.CompetitionID, ATHLEATS.TeamName;

SELECT * FROM ATHLEATS
ORDER BY EventID;