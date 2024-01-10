#create tests
import unittest
import mysql.connector
from athleat import athlete, status
from competition import competition
from event import event
from registration import registration

class TestCompetition(unittest.TestCase):
    def test1(self):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="fille2001",
            database="mydb"
        )
        mycursor = mydb.cursor(dictionary=True)
        comp = competition()
        comp.name = "Testcomp"
        comp.CompetitionVenue = "Testvenue"
        comp.Organizer = "Testorganizer"
        comp.NumberOfLanes = 10
        comp.save(mycursor, mydb)
        self.assertEqual(1, comp.id)
        mycursor.close()
        mydb.close()

if __name__ == '__main__':
    unittest.main()