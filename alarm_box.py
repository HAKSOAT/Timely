import tkinter as tki

class AlarmBox():

    def __init__(self, master):
        self.master = master
        self.alarm_frame = tki.Frame(self.master, padx = 7, pady = 5)
        self.alarm_frame.grid(row = 1, column = 0, columnspan = 8)

        self.alarm_canv = tki.Canvas(self.alarm_frame, height = 280, width = 570, bg = "#000fff000")
        self.alarm_canv.pack(side = tki.LEFT, fill = tki.BOTH)

        self.scrollbar = tki.Scrollbar(self.alarm_frame, command = self.alarm_canv.yview)
        self.scrollbar.pack(side = tki.RIGHT, fill = tki.Y)

        self.alarm_canv["yscrollcommand"] = self.scrollbar.set

        # self.but_ = tki.Button(self.alarm_canv)
        #
        # for each in range(0,250,5):
        #     self.alarm_canv.create_window((each,each), window = tki.Button(self.alarm_canv), anchor = "n")

        self.add_alarm(20, 10)
        self.add_alarm(20, 60)

    def add_alarm(self, x, y):
        self.alarm_display = tki.Button(self.alarm_canv, height = 2, width = 76, text = "Alarm One\t\t\t\t\tdfsh", bg = "#ffffff")
        self.checkbutton = tki.Checkbutton(self.alarm_canv, bg = "#000fff000")
        self.alarm_canv.create_window((x + 266,y), window = self.alarm_display, anchor = "n")
        self.alarm_canv.create_window((x,y + 10), window = self.checkbutton, anchor = "n")
