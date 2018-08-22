import sqlite3

class AlarmStorage():

    def __init__(self, location):
        self.connect_status = None
        self.cursor = None
        self.db_name = "alarm_storage.sqlite3"
        self.location = location + self.db_name

    def create(self):
        self.connect()
        self.cursor.execute("CREATE TABLE Alarms (Time INTEGER, Year TEXT, Month TEXT, Day TEXT, Hour TEXT, Minute TEXT, Tone TEXT)")

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
    def connect(self):
        self.connect_status = sqlite3.connect(self.location)
        self.cursor = self.connect_status.cursor()

    def commit(self):
        self.connect_status.commit()

    def close(self):
        self.connect_status.close()
