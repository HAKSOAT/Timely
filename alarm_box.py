"""
    This module deals is responsible for the box where alarms are displayed.
"""

import tkinter as tki

class AlarmBox():
    """
        This class is reponsible for creating the box where alarms are displayed.
        To instantiate, pass in the following:
            master widget where the box lives in
            storage object to access alarms
    """

    def __init__(self, master, storage):
        self.master = master
        self.storage = storage

        self.alarm_frame = tki.Frame(self.master, padx=7, pady=5)
        self.alarm_frame.grid(row=1, column=0, columnspan=8)

        self.alarm_canv = tki.Canvas(self.alarm_frame, height=350, width=570, bg="#00b300")
        self.alarm_canv.pack(side=tki.LEFT, fill=tki.BOTH)

        self.scrollbar = tki.Scrollbar(self.alarm_frame, command=self.alarm_canv.yview)
        self.scrollbar.pack(side=tki.RIGHT, fill=tki.Y)

        self.alarm_canv["yscrollcommand"] = self.scrollbar.set
        self.checklabel_states = []

        self.ascending_ringtime = []

    def get_alarm(self):
        """
            This module is responsible for getting alarms to be displayed in the alarmbox
            from the database.
        """
        self.checklabel_states = []
        self.storage.connect()
        db_result = self.storage.query()
        self.storage.close()
        point_y = 10
        for each in db_result:
            set_time = each[4:6]
            set_date = each[1:4]
            db_time = each[0]
            self.display_alarm(249, point_y, set_time, set_date, db_time)
            point_y += 50

    def display_alarm(self, point_x, point_y, time, date, db_time):
        """
            This module is responsible for displaying alarms in the alarmbox.
        """
        checkbox_x = 35
        checkbox_y = 7
        time_string = "{}:{}".format(time[0], time[1])
        date = "{}-{}-{}".format(date[2], date[1], date[0])

        alarm_label = tki.Label(self.alarm_canv, text="{}".format(db_time))

        alarm_display = tki.Button(self.alarm_canv, height=2, width=76,\
         text="{}\t\t\t\t{}".format(time_string, date), bg="#ffffff")

        state = tki.IntVar()
        checkbutton = tki.Checkbutton(self.alarm_canv, selectcolor="#00b300",\
         variable=state, indicatoron=0, width=1, height=0)

        self.checklabel_states.append([checkbutton, state, alarm_label])

        self.alarm_canv.create_window((checkbox_x + point_x, point_y),\
         window=alarm_display, anchor="n")
        self.alarm_canv.create_window((checkbox_x, checkbox_y + point_y),\
         window=checkbutton, anchor="n")


    def delete(self):
        """
            This module is responsible for deleting displayed alarms in the alarmbox.
        """
        self.alarm_canv.delete("all")
