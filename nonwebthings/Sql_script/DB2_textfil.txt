CREATE DATABASE mydb;
SHOW DATABASES;
USE mydb;

-- ADD VALUES TO Competition
INSERT INTO Competition (Name, StartDate, EndDate, CompetitionVenue, Organizer, NumberOfLanes, Length, IndividualStartFee, RelayStartFee, Description)
VALUES ROW('Vårsimiaden','2023-05-19','2023-05-20','Staffanstorp','Triton',8,25,100,200,'Deltävling1'),
ROW('Vårsimiaden','2023-05-19','2023-05-20','Kristianstad','KSLS',8,25,100,200,'Deltävling2'),
ROW('Vårsimiaden','2023-05-19','2023-05-20','Malmö','MKK',8,25,100,200,'Deltävling3'),
ROW('Vårsimiaden','2023-05-19','2023-05-20','Helsingborg','HS',8,25,100,200,'Deltävling4'),
ROW('Vårsimiaden','2023-05-19','2023-05-20','Landskrona','LS',8,25,100,200,'Deltävling5');

-- ADD VALUES TO EVENT
INSERT INTO EVENT (CompetitionID,EventNumber, EventName, Distance,Gender,MaxAge,QualifyingTime,Relay)
VALUES
ROW(6,1,'4x50m Medley Flickor 11-12 år Final',200,'X',12,'',1),
ROW(6,2,'4x50m Medley Pojkar 11-12 år Final',200,'X',12,'',1),
ROW(6,3,'100m Frisim Mixed Final',100,'F',12,'',0),
ROW(6,4,'50m Fjärilsim Mixed Final',50,'M',12,'',0),
ROW(6,5,'100m Bröstsim Mixed Final',100,'F',12,'',0),
ROW(6,6,'50m Ryggsim Mixed Final',50,'M',12,'',0),
ROW(6,7,'100m Medley Mixed Final',100,'F',12,'',0),
ROW(6,8,'100m Medley Mixed Final',100,'M',12,'',0),
ROW(6,9,'4x100m Medley Mixed 11-12 år Final',400,'X',12,'',1),
ROW(7,1,'4x50m Medley Flickor 11-12 år Final',200,'X',12,'',1),
ROW(7,2,'4x50m Medley Pojkar 11-12 år Final',200,'X',12,'',1),
ROW(7,3,'100m Frisim Mixed Final',100,'F',12,'',0),
ROW(7,4,'50m Fjärilsim Mixed Final',50,'M',12,'',0),
ROW(7,5,'100m Bröstsim Mixed Final',100,'F',12,'',0),
ROW(7,6,'50m Ryggsim Mixed Final',50,'M',12,'',0),
ROW(7,7,'100m Medley Mixed Final',100,'F',12,'',0),
ROW(7,8,'100m Medley Mixed Final',100,'M',12,'',0),
ROW(7,9,'4x100m Medley Mixed 11-12 år Final',400,'X',12,'',1),
ROW(8,1,'4x50m Medley Flickor 11-12 år Final',200,'X',12,'',1),
ROW(8,2,'4x50m Medley Pojkar 11-12 år Final',200,'X',12,'',1),
ROW(8,3,'100m Frisim Mixed Final',100,'F',12,'',0),
ROW(8,4,'50m Fjärilsim Mixed Final',50,'M',12,'',0),
ROW(8,5,'100m Bröstsim Mixed Final',100,'F',12,'',0),
ROW(8,6,'50m Ryggsim Mixed Final',50,'M',12,'',0),
ROW(8,7,'100m Medley Mixed Final',100,'F',12,'',0),
ROW(8,8,'100m Medley Mixed Final',100,'M',12,'',0),
ROW(8,9,'4x100m Medley Mixed 11-12 år Final',400,'X',12,'',1),
ROW(9,1,'4x50m Medley Flickor 11-12 år Final',200,'X',12,'',1),
ROW(9,2,'4x50m Medley Pojkar 11-12 år Final',200,'X',12,'',1),
ROW(9,3,'100m Frisim Mixed Final',100,'F',12,'',0),
ROW(9,4,'50m Fjärilsim Mixed Final',50,'M',12,'',0),
ROW(9,5,'100m Bröstsim Mixed Final',100,'F',12,'',0),
ROW(9,6,'50m Ryggsim Mixed Final',50,'M',12,'',0),
ROW(9,7,'100m Medley Mixed Final',100,'F',12,'',0),
ROW(9,8,'100m Medley Mixed Final',100,'M',12,'',0),
ROW(9,9,'4x100m Medley Mixed 11-12 år Final',400,'X',12,'',1),
ROW(9,1,'4x50m Medley Flickor 11-12 år Final',200,'X',12,'',1),
ROW(9,2,'4x50m Medley Pojkar 11-12 år Final',200,'X',12,'',1),
ROW(10,3,'100m Frisim Mixed Final',100,'F',12,'',0),
ROW(10,4,'50m Fjärilsim Mixed Final',50,'M',12,'',0),
ROW(10,5,'100m Bröstsim Mixed Final',100,'F',12,'',0),
ROW(10,6,'50m Ryggsim Mixed Final',50,'M',12,'',0),
ROW(10,7,'100m Medley Mixed Final',100,'F',12,'',0),
ROW(10,8,'100m Medley Mixed Final',100,'M',12,'',0),
ROW(10,9,'4x100m Medley Mixed 11-12 år Final',400,'X',12,'',1);

-- ADD VALUES TO REGISTRATIONS
INSERT INTO REGISTRATIONS (CompetitionID,EventNumber,Name,LastName,Team,Age,RegistrationTime)
VALUES
ROW(6,3,'Isabelle ','Trajkovsk','Simklubben Ran',2011,'1:11.18'),
ROW(6,3,'Folke ','af Tramp','Simklubben Poseidon',2011,'1:12.74'),
ROW(6,3,'Ludvig ','Sjödah','Simklubben Ran',2011,'1:14.43'),
ROW(6,3,'Erik ','Giselsson Tholi','Simklubben Poseidon',2011,'1:14.86'),
ROW(6,3,'Oskar ','Zdolse','Simklubben Poseidon',2011,'1:14.86'),
ROW(6,3,'Liv ','Lundin Linné','Simklubben Poseidon',2011,'1:14.88'),
ROW(6,3,'Alice ','Hudso','Landskrona Simsällskap',2011,'1:15.69'),
ROW(6,3,'Theo ','Lin','Simklubben Poseidon',2011,'1:17.06'),
ROW(6,3,'Josephine ','Lindgre','Simklubben Lödde',2011,'1:17.53'),
ROW(6,3,'Anton ','Aldeniu','Simklubben Ran',2011,'1:18.27'),
ROW(6,3,'David ','Askari Louye','Malmö Kappsimningsklubb',2011,'1:18.49'),
ROW(6,3,'Linn ','Ekval','Landskrona Simsällskap',2011,'1:18.84'),
ROW(6,3,'Joa ','Brogår','Simklubben Lödde',2011,'1:19.13'),
ROW(6,3,'Ebbe ','Modi','Simklubben Hajen',2011,'1:19.33'),
ROW(6,3,'Freja ','Rosber','Vellinge-Näsets Simklubb',2011,'1:19.64'),
ROW(6,3,'Mason ','Custar','Malmö Kappsimningsklubb',2011,'1:19.71'),
ROW(6,3,'Elvira ','Holmgren Horrdi','Simklubben Ran',2011,'1:19.72'),
ROW(6,3,'Inez ','Rönno','Malmö Kappsimningsklubb',2011,'1:19.76'),
ROW(6,3,'Julia ','Lundah','Vellinge-Näsets Simklubb',2011,'1:20.03'),
ROW(6,3,'Sophia ','L','Malmö Kappsimningsklubb',2011,'1:20.48'),
ROW(6,3,'Ellen ','Kristoferso','Simklubben Lödde',2011,'1:20.88'),
ROW(6,3,'Ellen ','Sjöber','Vellinge-Näsets Simklubb',2011,'1:21.34'),
ROW(6,3,'Andrei ','Damian Pod','Simklubben Ran',2011,'1:21.36'),
ROW(6,3,'Anton ','Pogarci','Malmö Kappsimningsklubb',2011,'1:21.86'),
ROW(6,3,'Sarah-Li ','Appelblad Wend','Landskrona Simsällskap',2011,'1:22.34'),
ROW(6,3,'Lucas ','Wänber','Vellinge-Näsets Simklubb',2011,'1:23.37'),
ROW(6,3,'Ebba ','Lasso','Malmö Kappsimningsklubb',2011,'1:24.44'),
ROW(6,3,'Nora-My ','Häge','Simklubben Ran',2011,'1:24.75'),
ROW(6,3,'Jonathan ','Kastber','Simklubben Poseidon',2011,'1:24.78'),
ROW(6,3,'Lovisa ','Arfwidso','Malmö Kappsimningsklubb',2011,'1:25.19'),
ROW(6,3,'Ellie ','Hagströ','SK Triton',2011,'1:26.18'),
ROW(6,3,'Ebba ','Öhli','Simklubben Lödde',2011,'1:26.27'),
ROW(6,3,'Minea ','Tepi','Simklubben Ran',2011,'1:26.91'),
ROW(6,3,'Maja ','Slunsk','Malmö Kappsimningsklubb',2011,'1:26.96'),
ROW(6,3,'Love ','Lund','Vellinge-Näsets Simklubb',2011,'1:27.53'),
ROW(6,3,'Elias ','Öiner','Malmö Kappsimningsklubb',2011,'1:27.54'),
ROW(6,3,'Juni ','Rip','Landskrona Simsällskap',2011,'1:27.64'),
ROW(6,3,'Felix ','Dissieu','Landskrona Simsällskap',2011,'1:28.20'),
ROW(6,3,'Viktor ','Moli','Malmö Kappsimningsklubb',2011,'1:28.74'),
ROW(6,4,'Elsa ','Holmber','Vellinge-Näsets Simklubb',2012,'37.18'),
ROW(6,4,'Melissa ','Lundi','Simklubben Lödde',2012,'38.16'),
ROW(6,4,'Veronica ','Perlhede','Simklubben Lödde',2012,'40.08'),
ROW(6,4,'Joakim ','Sveberg Karlsso','Föreningen Trelleborg Sim',2012,'40.30'),
ROW(6,4,'Izabella ','Broel-Plate','Simklubben Poseidon',2012,'42.43'),
ROW(6,4,'Kenza ','Cherchm','Simklubben Sydsim',2012,'42.65'),
ROW(6,4,'Lova ','Nyhol','Simklubben Lödde',2012,'43.33'),
ROW(6,4,'Rufus ','D','Simklubben Ran',2012,'43.60'),
ROW(6,4,'Shasha ','E','Simsällskapet Iden',2012,'43.80'),
ROW(6,4,'Axel ','Hulteber','Vellinge-Näsets Simklubb',2012,'44.01'),
ROW(6,4,'Maja ','Maksimovi','Malmö Kappsimningsklubb',2012,'44.36'),
ROW(6,4,'Philip ','Rallin','Vellinge-Näsets Simklubb',2012,'44.87'),
ROW(6,4,'Harald ','Wendelru','Simklubben Lödde',2012,'45.84'),
ROW(6,4,'Teo ','Hanse','Vellinge-Näsets Simklubb',2012,'45.87'),
ROW(6,4,'Gustaf ','Erixo','Malmö Kappsimningsklubb',2012,'46.01'),
ROW(6,4,'Zoé ','Mae Raneli','Malmö Kappsimningsklubb',2012,'46.06'),
ROW(6,4,'Victor ','Antonio Begi','Simklubben Poseidon',2012,'46.88'),
ROW(6,4,'Alexandar-Borrís ','Stoiano','Simklubben Poseidon',2012,'47.35'),
ROW(6,4,'Astrid ','Simonsso','Vellinge-Näsets Simklubb',2012,'47.94'),
ROW(6,4,'Elianna ','Pallser Dragojevi','Malmö Kappsimningsklubb',2012,'48.02'),
ROW(6,4,'Julia ','Rothni','Simklubben Hajen',2012,'48.11'),
ROW(6,4,'Klara ','Malmgre','Malmö Kappsimningsklubb',2012,'48.81'),
ROW(6,4,'Neil ','OBrie','Simklubben Poseidon',2012,'49.21'),
ROW(6,4,'Morris ','Alsali','Simklubben Ran',2012,'50.16'),
ROW(6,4,'Selma ','Mölle','Vellinge-Näsets Simklubb',2012,'52.04'),
ROW(6,4,'Farah-Noush ','Thompso','Malmö Kappsimningsklubb',2012,'53.11'),
ROW(6,4,'Prisha ','Shrivastav','Simklubben Poseidon',2012,'53.43'),
ROW(6,4,'Karin ','Niklasso','Malmö Kappsimningsklubb',2012,'53.89'),
ROW(6,4,'Lill ','Bruh','Simklubben Sydsim',2012,'55.41'),
ROW(6,4,'Melker ','Borgströ','Malmö Kappsimningsklubb',2012,'55.75'),
ROW(6,4,'Luan ','Osman','Malmö Kappsimningsklubb',2012,'56.30'),
ROW(6,4,'Kevin ','Eriksso','Malmö Kappsimningsklubb',2012,'56.35'),
ROW(6,4,'Caspian ','Olsso','Simklubben Poseidon',2012,'56.49'),
ROW(6,4,'Märta ','Nilsso','Malmö Kappsimningsklubb',2012,'57.51'),
ROW(6,4,'Bella ','Borgströ','Malmö Kappsimningsklubb',2012,'57.55'),
ROW(6,4,'Ekaterina ','Rogovay','Malmö Kappsimningsklubb',2012,'57.85'),
ROW(6,4,'Vera ','Ahlgre','Malmö Kappsimningsklubb',2012,'58.08'),
ROW(6,4,'Vincent ','Gourdo','Malmö Kappsimningsklubb',2012,'58.20'),
ROW(6,4,'Alva ','Ehn Blomgre','Simklubben Poseidon',2012,'59.48'),
ROW(6,4,'Lovisa ','Gustafsson Manha','Malmö Kappsimningsklubb',2012,'59.94'),
ROW(6,4,'Kevin ','Alex','Malmö Kappsimningsklubb',2012,'1:00.02'),
ROW(6,4,'Alexander ','Lestande','Simsällskapet Iden',2012,'1:01.78'),
ROW(6,4,'Daniil ','Avoti','Landskrona Simsällskap',2012,'1:03.45'),
ROW(6,5,'Isabelle ','Trajkovsk','Simklubben Ran',2011,'1:29.96'),
ROW(6,5,'Linnéa ','Hansso','Landskrona Simsällskap',2011,'1:33.97'),
ROW(6,5,'Liv ','Lundin Linné','Simklubben Poseidon',2011,'1:35.71'),
ROW(6,5,'Julia ','Lundah','Vellinge-Näsets Simklubb',2011,'1:36.64'),
ROW(6,5,'Linn ','Ekval','Landskrona Simsällskap',2011,'1:37.51'),
ROW(6,5,'Folke ','af Tramp','Simklubben Poseidon',2011,'1:38.47'),
ROW(6,5,'David ','Askari Louye','Malmö Kappsimningsklubb',2011,'1:38.85'),
ROW(6,5,'Ellen ','Sjöber','Vellinge-Näsets Simklubb',2011,'1:39.48'),
ROW(6,5,'Freja ','Rosber','Vellinge-Näsets Simklubb',2011,'1:39.71'),
ROW(6,5,'Lykke ','Svah','Simklubben Lödde',2011,'1:40.42'),
ROW(6,5,'Anton ','Pogarci','Malmö Kappsimningsklubb',2011,'1:40.44'),
ROW(6,5,'Nora-My ','Häge','Simklubben Ran',2011,'1:41.78'),
ROW(6,5,'Sophia ','L','Malmö Kappsimningsklubb',2011,'1:42.01'),
ROW(6,5,'Ebba ','Lasso','Malmö Kappsimningsklubb',2011,'1:43.20'),
ROW(6,5,'Valencia ','Po','Simklubben Sydsim',2011,'1:43.90'),
ROW(6,5,'Lovisa ','Arfwidso','Malmö Kappsimningsklubb',2011,'1:44.00'),
ROW(6,5,'Ellen ','Johansso','Simklubben Hajen',2011,'1:44.25'),
ROW(6,5,'Joa ','Brogår','Simklubben Lödde',2011,'1:44.83'),
ROW(6,5,'Inez ','Rönno','Malmö Kappsimningsklubb',2011,'1:44.83'),
ROW(6,5,'Elias ','Öiner','Malmö Kappsimningsklubb',2011,'1:45.08'),
ROW(6,5,'Mason ','Custar','Malmö Kappsimningsklubb',2011,'1:45.42'),
ROW(6,5,'Felipe ','Ös','Föreningen Trelleborg Sim',2011,'1:45.69'),
ROW(6,5,'Juni ','Rip','Landskrona Simsällskap',2011,'1:46.47'),
ROW(6,5,'Anton ','Aldeniu','Simklubben Ran',2011,'1:46.59'),
ROW(6,5,'Theo ','Lin','Simklubben Poseidon',2011,'1:46.72'),
ROW(6,5,'Erik ','Giselsson Tholi','Simklubben Poseidon',2011,'1:47.09'),
ROW(6,5,'Kajsa ','Trönell Staglin','Simklubben Lödde',2011,'1:47.37'),
ROW(6,5,'Olivia ','Rab','Malmö Kappsimningsklubb',2011,'1:48.83'),
ROW(7,3,'Nefeli ','Blithikioti','Helsingborgs Simsällskap',2011,'1:05.53'),
ROW(7,3,'Noelle ','Roslin','Helsingborgs Simsällskap',2011,'1:13.79'),
ROW(7,3,'Felicia ','Hvistenda','Eslövs Simsällskap',2011,'1:15.29'),
ROW(7,3,'Aiyana ','Svensso','Kristianstads SLS',2011,'1:15.49'),
ROW(7,3,'Nellie ','Bertelsen Bor','Helsingborgs Simsällskap',2011,'1:16.00'),
ROW(7,3,'Maja ','Hansso','Helsingborgs Simsällskap',2011,'1:18.13'),
ROW(7,3,'Alice ','Levi','Helsingborgs Simsällskap',2011,'1:18.59'),
ROW(7,3,'Ella ','Stenmar','Ängelholms Simssällskap',2011,'1:18.80'),
ROW(7,3,'Marta ','Kalin','Ängelholms Simssällskap',2011,'1:19.75'),
ROW(7,3,'Thea ','Axelsson Orvegre','Kristianstads SLS',2011,'1:19.92'),
ROW(7,3,'Inez ','Pirvu Ottosso','Klippans Simsällskap',2011,'1:20.07'),
ROW(7,3,'Elvira ','Sandber','Helsingborgs Simsällskap',2011,'1:21.28'),
ROW(7,3,'Lykke ','Martinsso','Sjöbo Simsällskap',2011,'1:21.44'),
ROW(7,3,'Minuu ','Neuman','Helsingborgs Simsällskap',2011,'1:22.05'),
ROW(7,3,'Moa ','Thoré','Helsingborgs Simsällskap',2011,'1:22.21'),
ROW(7,3,'Olivia ','Eriksso','Helsingborgs Simsällskap',2011,'1:22.99'),
ROW(7,3,'Maria ','Komljenovi','Helsingborgs Simsällskap',2011,'1:24.21'),
ROW(7,3,'Olivia ','Pålsso','Karlshamns Simklubb',2011,'1:26.02'),
ROW(7,3,'Lovisa ','Ericso','Kristianstads SLS',2011,'1:27.47'),
ROW(7,3,'Stella ','Lundströ','Ängelholms Simsällskap',2011,'1:28.34'),
ROW(7,3,'Alice ','Al','Helsingborgs Simsällskap',2011,'1:28.92'),
ROW(7,3,'Meja ','Sandi','Helsingborgs Simsällskap',2011,'1:29.27'),
ROW(7,3,'Signe ','Kull','Höganäs Simsällskap',2011,'1:29.40'),
ROW(7,3,'Tyra ','Bengtsso','Ängelholms Simsällskap',2011,'1:31.16'),
ROW(7,4,'Andreas ','Jove','Helsingborgs Simsällskap',2011,'1:11.67'),
ROW(7,4,'Casper ','Huasso','Ringsjö Simklubb',2011,'1:12.85'),
ROW(7,4,'Albin ','Björ','Föreningen Österlen-Sim',2011,'1:14.89'),
ROW(7,4,'Oscar ','Thi','Kristianstads SLS',2011,'1:15.07'),
ROW(7,4,'Tim ','Banker','Helsingborgs Simsällskap',2011,'1:16.54'),
ROW(7,4,'Neo ','Dobra','Helsingborgs Simsällskap',2011,'1:17.66'),
ROW(7,4,'Alexander ','Nilry','Ystads Simsällskap',2011,'1:19.98'),
ROW(7,4,'Kaj ','Strun','Kristianstads SLS',2011,'1:20.91'),
ROW(7,4,'Neo ','Olofsso','Karlskrona Simsällskap',2011,'1:24.05'),
ROW(7,4,'Eren ','Bozkur','Karlshamns Simklubb',2011,'1:25.74'),
ROW(7,4,'Hassan ','Kabri','Helsingborgs Simsällskap',2011,'1:26.75'),
ROW(7,4,'Love ','Kronwal','Helsingborgs Simsällskap',2011,'1:27.43'),
ROW(7,4,'David ','Opariu','Osby Simsällskap',2011,'1:29.23'),
ROW(7,4,'Ludwig ','Ljungber','Kristianstads SLS',2011,'1:29.36'),
ROW(7,4,'Noel ','Cederhil','Karlshamns Simklubb',2011,'1:37.80'),
ROW(7,4,'Henry ','Pritchar','Höganäs Simsällskap',2011,'1:38.40'),
ROW(7,4,'Rayan ','Asaa','Karlshamns Simklubb',2011,'1:38.71'),
ROW(7,4,'Vincent ','Williamsso','Osby Simsällskap',2011,'1:57.22'),
ROW(7,4,'Alve ','Kalmarlin','Karlshamns Simklubb',2011,''),
ROW(7,4,'Jonathan ','Johansso','Höganäs Simsällskap',2011,''),
ROW(7,4,'Erik ','Korowajczy','Föreningen Österlen-Sim',2011,''),
ROW(7,4,'Felix ','Zande','Karlskrona Simsällskap',2011,''),
ROW(7,5,'Ellen ','Palmqvis','S 71',2012,'35.84'),
ROW(7,5,'Nellie ','Nilsso','Sjöbo Simsällskap',2012,'38.84'),
ROW(7,5,'Sofia ','Månsso','S 71',2012,'38.85'),
ROW(7,5,'Isa ','Ströby-Stepa','Klippans Simsällskap',2012,'40.64'),
ROW(7,5,'Martina ','Fernströ','Helsingborgs Simsällskap',2012,'47.50'),
ROW(7,5,'Patricija ','Meskyt','Bromöllaortens Simsällskap',2012,'48.42'),
ROW(7,5,'Tilda ','Olofsso','Osby Simsällskap',2012,'50.04'),
ROW(7,5,'Lova ','Bertelsen Bor','Helsingborgs Simsällskap',2012,'50.60'),
ROW(7,5,'Esther ','Eriksso','Höganäs Simsällskap',2012,'51.24'),
ROW(7,5,'Amelie ','Tho','Helsingborgs Simsällskap',2012,'52.01'),
ROW(7,5,'Elsa ','Börjesso','Helsingborgs Simsällskap',2012,'54.55'),
ROW(7,5,'Ebba ','Gustavsso','Eslövs Simsällskap',2012,'59.12'),
ROW(7,5,'Anna ','Johansso','Osby Simsällskap',2012,'1:17.34'),
ROW(7,5,'Ella ','Nilsso','Föreningen Österlen-Sim',2012,''),
ROW(7,5,'Gry ','Tuneki','S 71',2012,''),
ROW(7,5,'Isabel ','Poulse','Helsingborgs Simsällskap',2012,''),
ROW(7,5,'Lewisia ','Liena','Ystads Simsällskap',2012,''),
ROW(7,5,'Channelle ','Lundber','Simsällskapet Delfin',2012,''),
ROW(7,5,'Majken ','Brommesso','Kristianstads SLS',2012,'');

-- Insert values into status
INSERT INTO STATUS (StatusText)
VALUES 
('DNF'),
('OK'),
('DISKAD');

set @eventid = (select EVENT.ID
from EVENT
where EVENT.CompetitionID = 2 AND EVENT.EventNumber = 2
limit 1);
select @eventid;

set @statusid = (select STATUS.ID
from STATUS
where STATUS.ID = 2
);

-- Insert eventid into athleats once
insert into ATHLEATS (EventID)
values (@EventID);


-- Select satser för att checka tab
SELECT * FROM ATHLEATS;

SELECT * FROM STATUS;

select * from Competition;

select * from EVENT;

select * from REGISTRATIONS;

select * from Competition
inner join EVENT
on Competition.ID = EVENT.CompetitionID;

delete from Competition
where ID < 15;

drop table Competition;
