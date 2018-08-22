import tkinter as tki
from tkinter import filedialog
from tkinter import messagebox
from calendar_picker.CalendarDialog import CalendarFrame

from storage import Storage
import time


class Add():

    def __init__(self, master):
        self.master = master

        self.time = None
        self.date = None
        self.tone = None

        self.time_index = None

        self.tens_hour = tki.Label(self.master, height = 2, width = 6, text = 0, font=("Helvetica", 16, "bold"))
        self.tens_hour.grid(row = 0, column = 0, padx = [2,10], pady = [20,0])

        self.units_hour = tki.Label(self.master, height = 2, width = 6, text = 0, font=("Helvetica", 16, "bold"))
        self.units_hour.grid(row = 0, column = 1, padx = 10, pady = [20,0])

        self.separator = tki.Label(self.master, height = 2, width = 1, text = ":", font=("Helvetica", 16, "bold"))
        self.separator.grid(row = 0, column = 2, padx = 5, pady = [20,0])

        self.tens_minutes = tki.Label(self.master, height = 2, width = 6, text = 0, font=("Helvetica", 16, "bold"))
        self.tens_minutes.grid(row = 0, column = 3, padx = 10, pady = [20,0])

        self.units_minutes = tki.Label(self.master, height = 2, width = 6, text = 0, font=("Helvetica", 16, "bold"))
        self.units_minutes.grid(row = 0, column = 4, padx = 10, pady = [20,0])

        self.add_button = tki.Button(self.master, text = "Add Alarm", padx = 35, command = self.get_date)
        self.add_button.grid(row = 3, column = 2, columnspan = 3, pady = [120,0])

        up_arrow = tki.PhotoImage(file = "arrow-141-16.gif")
        down_arrow = tki.PhotoImage(file = "arrow-204-16.gif")

        self.increase_one = tki.Button(self.master, image = up_arrow)
        self.increase_one.image = up_arrow
        self.increase_one.grid(row = 1, column = 0, pady = [20,0])

        self.increase_two = tki.Button(self.master, image = up_arrow)
        self.increase_two.image = up_arrow
        self.increase_two.grid(row = 1, column = 1, pady = [20,0])

        self.increase_three = tki.Button(self.master, image = up_arrow)
        self.increase_three.image = up_arrow
        self.increase_three.grid(row = 1, column = 3, pady = [20,0])

        self.increase_four = tki.Button(self.master, image = up_arrow)
        self.increase_four.image = up_arrow
        self.increase_four.grid(row = 1, column = 4, pady = [20,0])

        self.decrease_one = tki.Button(self.master, image = down_arrow)
        self.decrease_one.image = down_arrow
        self.decrease_one.grid(row = 2, column = 0)

        self.decrease_two = tki.Button(self.master, image = down_arrow)
        self.decrease_two.image = down_arrow
        self.decrease_two.grid(row = 2, column = 1)

        self.decrease_three = tki.Button(self.master, image = down_arrow)
        self.decrease_three.image = down_arrow
        self.decrease_three.grid(row = 2, column = 3)

        self.decrease_four = tki.Button(self.master, image = down_arrow)
        self.decrease_four.image = down_arrow
        self.decrease_four.grid(row = 2, column = 4)

        self.calendar_frame = CalendarFrame(master)
        self.calendar_frame.grid(row = 3, column = 0, columnspan = 2, pady = [50,10])

        self.tone_box = tki.LabelFrame(self.master)
        self.tone_box.grid(row = 4, column = 0, columnspan = 2)
        self.tone_name = tki.Entry(self.tone_box, state = tki.DISABLED)
        self.tone_name.grid(row = 0, column = 0)

        self.tone_click = tki.Button(self.tone_box, text = "Choose a tone")
        self.tone_click.grid(row = 1, column = 0)

        self.increase_one.bind("<ButtonRelease-1>", self.increase)
        self.increase_two.bind("<ButtonRelease-1>", self.increase)
        self.increase_three.bind("<ButtonRelease-1>", self.increase)
        self.increase_four.bind("<ButtonRelease-1>", self.increase)

        self.decrease_one.bind("<ButtonRelease-1>", self.decrease)
        self.decrease_two.bind("<ButtonRelease-1>", self.decrease)
        self.decrease_three.bind("<ButtonRelease-1>", self.decrease)
        self.decrease_four.bind("<ButtonRelease-1>", self.decrease)

        self.tone_click.bind("<ButtonRelease-1>", self.get_tone)
        self.add_button.bind("<ButtonRelease-1>", self.add_alarm)


    def increase(self, event):
        if self.increase_one.winfo_id == event.widget.winfo_id:
            self.tens_hour["text"] += 1

        elif self.increase_two.winfo_id == event.widget.winfo_id:
            self.units_hour["text"] += 1

        elif self.increase_three.winfo_id == event.widget.winfo_id:
            self.tens_minutes["text"] += 1

        elif self.increase_four.winfo_id == event.widget.winfo_id:
            self.units_minutes["text"] += 1

    def decrease(self, event):
        if self.decrease_one.winfo_id == event.widget.winfo_id and self.tens_hour["text"] >= 1:
            self.tens_hour["text"] -= 1

        elif self.decrease_two.winfo_id == event.widget.winfo_id and self.units_hour["text"] >= 1:
            self.units_hour["text"] -= 1

        elif self.decrease_three.winfo_id == event.widget.winfo_id and self.tens_minutes["text"] >= 1:
            self.tens_minutes["text"] -= 1

        elif self.decrease_four.winfo_id == event.widget.winfo_id and self.unit_minutes["text"] >= 1:
            self.units_minutes["text"] -= 1


    def get_tone(self, event):
        self.tone = filedialog.askopenfilename(initialdir = "/",title = "Select tone",filetypes = (("mp3 files","*.mp3"),))
        try:
            self.stripped_tone = self.tone.split("/")[-1]
            self.tone_name["state"] = tki.NORMAL
            self.tone_name.insert(tki.END, self.stripped_tone)
            self.tone_name["state"] = tki.DISABLED
        except AttributeError:
            self.tone = None


    def get_time(self):
        self.time = [int(str(tens_hour) + str(units_hour)), int(str(tens_minutes) + str(units_minutes))]
        self.time = {"hour": self.time[0], "minute": self.time[1]}
    def get_date(self):
        try:
            self.date = list(map(int, self.calendar_frame.date_box.get().split("/")))
            self.date = {"year":self.date[2], "month":self.date[1], "day":self.date[0]}

        except ValueError:
            self.date = None

    def to_db(self):
        storage = Storage()
        self.time_index = time.time()
        storage.add(self.time_index, self.date["year"], self.date["month"], self.date["day"],
                    self.time["hour"], self.time["minute"], self.tone)

    def add_alarm(self, event):
        self.get_date()
        if self.date is None:
            messagebox.showerror(title = "Error!", message = "Please choose a date!")

        elif self.tone is None:
            messagebox.showerror(title = "Error!", message = "Please choose a tone!")

        else:
            # self.to_db()
            self.close()


    def close(self):
        self.master.destroy()
