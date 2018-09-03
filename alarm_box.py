import tkinter as tki
import time
from pygame import mixer
from popup import AlarmPopUp

class AlarmBox():

    def __init__(self, master, storage):
        self.master = master
        self.storage = storage

        self.alarm_frame = tki.Frame(self.master, padx = 7, pady = 5)
        self.alarm_frame.grid(row = 1, column = 0, columnspan = 8)

        self.alarm_canv = tki.Canvas(self.alarm_frame, height = 350, width = 570, bg = "#000fff000")
        self.alarm_canv.pack(side = tki.LEFT, fill = tki.BOTH)

        self.scrollbar = tki.Scrollbar(self.alarm_frame, command = self.alarm_canv.yview)
        self.scrollbar.pack(side = tki.RIGHT, fill = tki.Y)

        self.alarm_canv["yscrollcommand"] = self.scrollbar.set
        self.checklabel_states = []

        self.ascending_ringtime = []

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


    def delete(self):
        self.alarm_canv.delete("all")
