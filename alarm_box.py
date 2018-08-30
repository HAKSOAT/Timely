import tkinter as tki
import threading
from datetime import datetime as dt
import time

from popup import AlarmPopUp

class AlarmBox():

    def __init__(self, master, storage):
        self.master = master
        self.storage = storage

        self.alarm_frame = tki.Frame(self.master, padx = 7, pady = 5)
        self.alarm_frame.grid(row = 1, column = 0, columnspan = 8)

        self.alarm_canv = tki.Canvas(self.alarm_frame, height = 280, width = 570, bg = "#000fff000")
        self.alarm_canv.pack(side = tki.LEFT, fill = tki.BOTH)

        self.scrollbar = tki.Scrollbar(self.alarm_frame, command = self.alarm_canv.yview)
        self.scrollbar.pack(side = tki.RIGHT, fill = tki.Y)

        self.alarm_canv["yscrollcommand"] = self.scrollbar.set
        self.checklabel_states = []

        self.trigger_thread = None

        self.create_thread()

    def show_alarm(self):
        self.checklabel_states = []
        self.storage.connect()
        self.db_result = self.storage.query()
        self.storage.close()
        self.point_y = 10
        for each in self.db_result:
            set_time = each[4:6]
            set_date = each[1:4]
            db_time = each[0]
            self.add_alarm(260, self.point_y, set_time, set_date, db_time)
            self.point_y += 50

    def add_alarm(self, x, y, time, date, db_time):
        checkbox_x = 26
        checkbox_y = 10
        time = "{}:{}".format(time[0], time[1])
        date = "{}-{}-{}".format(date[2], date[1], date[0])

        self.alarm_label = tki.Label(self.alarm_canv, text = "{}".format(db_time))

        self.alarm_display = tki.Button(self.alarm_canv, height = 2, width = 76,
                            text = "{}\t\t\t\t{}".format(time, date), bg = "#ffffff")

        state = tki.IntVar()
        self.checkbutton = tki.Checkbutton(self.alarm_canv, bg = "#000fff000", variable = state,
                            indicatoron = 1, width = 1)

        self.checklabel_states.append([self.checkbutton, state, self.alarm_label])

        self.alarm_canv.create_window((checkbox_x + x, y), window = self.alarm_display, anchor = "n")
        self.alarm_canv.create_window((checkbox_x,checkbox_y + y),
                                       window = self.checkbutton, anchor = "n")

    def create_thread(self):
        self.trigger_thread = threading.Timer(1, self.trigger)
        self.trigger_thread.start()

    def trigger(self):
        self.storage.connect()
        db_result = self.storage.query()

        ringtime = []

        for each in db_result:
            set_time = dt.now().replace(year = int(each[1]), month = int(each[2]), day = int(each[3]),
                        hour = int(each[4]), minute = int(each[5]), second = 0)
            time_left = set_time - dt.now()
            ringtime.append((time_left.total_seconds(), each[6], [each[0], each[4], each[5]]))

        ascending_ringtime = sorted(ringtime, key = lambda x: x[0])

        for each in ascending_ringtime:
            try:
                time.sleep(int(each[0]))
                self.popup = tki.Toplevel()
                self.popup.transient(self.master)

                self.popup.minsize(390, 350)
                self.popup.maxsize(390, 350)

                self.popup.title("Pop Up")
                print(each[0])
                AlarmPopUp(self.popup, self.storage, each[1], each[2][1], each[2][2])

            except ValueError:
                self.storage.connect()
                self.storage.delete(each[2][0])
                self.storage.commit()
                self.storage.close()


    def delete(self):
        self.alarm_canv.delete("all")
