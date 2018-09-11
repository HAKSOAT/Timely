import time as t
import tkinter as tki
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime as dt
from calendar_picker.CalendarDialog import CalendarFrame



class Config():

    def __init__(self, master, storage, alarm_box, ringer, pretime=None,\
     pretone=None, predate=None, pretime_index=None):
        self.master = master
        self.storage = storage
        self.alarm_box = alarm_box
        self.ringer = ringer

        self.time = None
        self.date = predate
        self.tone = pretone

        self.time_index = pretime_index

        if pretime is None:
            pretime = ["00", "00"]

        self.indicator_labels = [int(pretime[0][0]), int(pretime[0][1]),\
         ":", int(pretime[1][0]), int(pretime[1][1])]

        self.indicators = []

        column = 0
        for label in self.indicator_labels:
            if column == 0:
                padx = [2, 10]
            elif column == 2:
                padx = 5
            else:
                padx = 10
            temp_indicator = tki.Label(self.master, height=2,\
             width=6, text=label, font=("Helvetica", 16, "bold"))
            temp_indicator.grid(row=0, column=column, padx=padx, pady=[20, 0])
            self.indicators.append(temp_indicator)
            column += 1

        up_arrow = tki.PhotoImage(file="icons/arrow-141-16.gif")
        down_arrow = tki.PhotoImage(file="icons/arrow-204-16.gif")
        self.navigate_buttons = []

        for column in range(5):
            if column == 2:
                continue
            temp_increase = tki.Button(self.master, image=up_arrow)
            temp_increase.image = up_arrow
            temp_increase.grid(row=1, column=column, pady=[20, 0])
            self.navigate_buttons.append(temp_increase)

            temp_decrease = tki.Button(self.master, image=down_arrow)
            temp_decrease.image = down_arrow
            temp_decrease.grid(row=2, column=column)
            self.navigate_buttons.append(temp_decrease)

        if self.time_index is None:
            self.add_button = tki.Button(self.master, text="Add Alarm",\
             padx=35, command=self.add_alarm)
            self.add_button.grid(row=3, column=2, columnspan=3, pady=[120, 0])

        else:
            self.update_button = tki.Button(self.master, text="Update Alarm",\
             padx=35, command=self.update_alarm)
            self.update_button.grid(row=3, column=2, columnspan=3, pady=[120, 0])

        self.calendar_frame = CalendarFrame(master, self.date)
        self.calendar_frame.grid(row=3, column=0, columnspan=2, pady=[50, 10])

        self.tone_box = tki.LabelFrame(self.master)
        self.tone_box.grid(row=4, column=0, columnspan=2)
        self.tone_name = tki.Entry(self.tone_box, state=tki.DISABLED)
        self.tone_name.grid(row=0, column=0)

        self.tone_click = tki.Button(self.tone_box, text="Choose a tone", command=self.get_tone)
        self.tone_click.grid(row=1, column=0)

        self.bind_widgets()

        if self.tone != None:
            self.display_tone_name()

    def bind_widgets(self):
        self.navigate_buttons[0].bind("<ButtonRelease-1>", self.increase)
        self.navigate_buttons[2].bind("<ButtonRelease-1>", self.increase)
        self.navigate_buttons[4].bind("<ButtonRelease-1>", self.increase)
        self.navigate_buttons[6].bind("<ButtonRelease-1>", self.increase)

        self.navigate_buttons[1].bind("<ButtonRelease-1>", self.decrease)
        self.navigate_buttons[3].bind("<ButtonRelease-1>", self.decrease)
        self.navigate_buttons[5].bind("<ButtonRelease-1>", self.decrease)
        self.navigate_buttons[7].bind("<ButtonRelease-1>", self.decrease)


    def increase(self, event):
        if self.navigate_buttons[0].winfo_id == event.widget.winfo_id\
         and self.indicators[0]["text"] <= 1:
            if self.indicators[0]["text"] == 1 and self.indicators[1]["text"] > 3:
                pass
            else:
                self.indicators[0]["text"] += 1

        elif self.navigate_buttons[2].winfo_id == event.widget.winfo_id\
         and self.indicators[1]["text"] <= 8:
            if self.indicators[0]["text"] == 2 and self.indicators[1]["text"] == 3:
                pass
            else:
                self.indicators[1]["text"] += 1

        elif self.navigate_buttons[4].winfo_id == event.widget.winfo_id\
         and self.indicators[3]["text"] <= 4:
            self.indicators[3]["text"] += 1

        elif self.navigate_buttons[6].winfo_id == event.widget.winfo_id\
         and self.indicators[4]["text"] <= 8:
            self.indicators[4]["text"] += 1

    def decrease(self, event):
        if self.navigate_buttons[1].winfo_id == event.widget.winfo_id\
         and self.indicators[0]["text"] >= 1:
            self.indicators[0]["text"] -= 1

        elif self.navigate_buttons[3].winfo_id == event.widget.winfo_id\
         and self.indicators[1]["text"] >= 1:
            self.indicators[1]["text"] -= 1

        elif self.navigate_buttons[5].winfo_id == event.widget.winfo_id\
         and self.indicators[3]["text"] >= 1:
            self.indicators[3]["text"] -= 1

        elif self.navigate_buttons[7].winfo_id == event.widget.winfo_id\
         and self.indicators[4]["text"] >= 1:
            self.indicators[4]["text"] -= 1


    def get_tone(self):
        self.display_tone_name()
        try:
            self.tone = filedialog.askopenfilename(initialdir="/", initialfile="", title="Select tone",\
            filetypes=(("mp3 files", "*.mp3"),), parent=self.master)
        except tki._tkinter.TclError:
            pass
        self.display_tone_name()


    def display_tone_name(self):
        try:
            self.stripped_tone = self.tone.split("/")[-1]
            self.tone_name["state"] = tki.NORMAL
            self.tone_name.insert(tki.END, self.stripped_tone)
            self.tone_name["state"] = tki.DISABLED
        except AttributeError:
            self.tone = None

    def get_time(self):
        unparsed_time = [str(self.indicators[0]["text"]) + str(self.indicators[1]["text"]),\
         str(self.indicators[3]["text"]) + str(self.indicators[4]["text"])]
        self.time = {"hour": unparsed_time[0], "minute": unparsed_time[1]}
        return self.time
    def get_date(self):
        try:
            self.date = self.calendar_frame.date_box.get().split("/")
            self.date = {"year":self.date[2], "month":self.date[1], "day":self.date[0]}
            return self.date
        except IndexError:
            self.date = None

    def to_db(self):
        if self.time_index is None:
            self.time_index = t.time()
            self.storage.connect()
            self.storage.add(self.time_index, self.date["year"], self.date["month"],\
             self.date["day"], self.time["hour"], self.time["minute"], self.tone)
            self.storage.commit()
            self.storage.close()
        else:
            self.storage.connect()
            self.storage.update(self.time_index, self.date["year"], self.date["month"],\
             self.date["day"], self.time["hour"], self.time["minute"], self.tone)
            self.storage.commit()
            self.storage.close()

    def add_alarm(self):
        date = self.get_date()
        time = self.get_time()

        if self.date is None:
            messagebox.showerror(title="Error!", message="Please choose a date!")

        elif self.tone is None:
            messagebox.showerror(title="Error!", message="Please choose a tone!")

        else:
            time_difference = dt.now().replace(year=int(date["year"]), month=int(date["month"]),\
            day=int(date["day"]), hour=int(time["hour"]),\
            minute=int(time["minute"]), second=0) - dt.now()
            seconds_difference = time_difference.total_seconds()
            if seconds_difference <= 0:
                messagebox.showerror(title="Error!", message="The chosen time is in the past!")
            else:
                self.to_db()
                self.ringer.get_ringtime()
                self.ringer.call_popup()
                self.alarm_box.get_alarm()
                self.close()

    def update_alarm(self):
        self.get_date()
        self.get_time()
        if self.date is None:
            messagebox.showerror(title="Error!", message="Please choose a date!")

        elif self.tone is None:
            messagebox.showerror(title="Error!", message="Please choose a tone!")

        else:
            self.to_db()
            self.ringer.get_ringtime()
            self.ringer.call_popup()
            self.alarm_box.get_alarm()
            self.close()

    def close(self):
        self.master.destroy()
