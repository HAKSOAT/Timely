import sqlite3

class Storage():

    def __init__(self, location):
        self.connect_status = None
        self.cursor = None
        self.location = location

    def create(self):
        self.connect_status = sqlite3.connect(self.location)
        self.cursor = self.connect_status.cursor()
        self.cursor.execute("CREATE TABLE Alarms (Time INTEGER, Year INTEGER, Month INTEGER, Day INTEGER, Hour INTEGER, Minute INTEGER, Tone TEXT)")

    def add(self, time, year, month, day, hour, minute, tone):
        self.cursor.execute("INSERT INTO Alarms (Time, Year, Month, Day, Hour, Minute, Tone) VALUES (?, ?, ?, ?, ?, ?, ?);", (time, year, month, day, hour, minute, tone))

    def delete(self, time):
        self.cursor.execute("DELETE FROM Alarms WHERE Time = ?;", (time))

    def query(self):
        try:
            self.cursor.execute("SELECT Year, Month, Day, Hour, Minute, Tone FROM Alarms ORDER BY Time ASC;")
            return self.cursor.fetchall()
        except IndexError:
        	return ""
