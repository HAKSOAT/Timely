import tkinter as tki
from add import Add
from alarm_box import AlarmBox
from storage import AlarmStorage
import os

class AlarmUI():

    def __init__(self, master):
        self.master = master
        self.location = "./"
        self.db_name = "alarm_storage.sqlite3"

        if self.db_name in os.listdir("."):
            self.storage = AlarmStorage("./")
            self.storage.connect()
        else:
            self.storage = AlarmStorage("./")
            self.storage.create()

        photo = tki.PhotoImage(file = "plus-16.gif")
        self.add_bt = tki.Button(self.master, text = "Add", image = photo, compound = "left", command = self.click_add)
        self.add_bt.image = photo
        self.add_bt.grid(row = 0, column = 0, sticky = tki.N + tki.E + tki.S + tki.W)

        photo = tki.PhotoImage(file = "minus-16.gif")
        self.delete_bt = tki.Button(self.master, text = "Delete", image = photo, compound = "left")
        self.delete_bt.image = photo
        self.delete_bt.grid(row = 0, column = 1, sticky = tki.N + tki.E + tki.S + tki.W)

        photo = tki.PhotoImage(file = "edit-11-16.gif")
        self.edit_bt = tki.Button(self.master, text = "Edit", image = photo, compound = "left")
        self.edit_bt.image = photo
        self.edit_bt.grid(row = 0, column = 2, sticky = tki.N + tki.E + tki.S + tki.W)

        photo = tki.PhotoImage(file = "copy-16.gif")
        self.clone_bt = tki.Button(self.master, text = "Clone", image = photo, compound = "left")
        self.clone_bt.image = photo
        self.clone_bt.grid(row = 0, column = 3, sticky = tki.N + tki.E + tki.S + tki.W)

        AlarmBox(self.master, self.storage)

        # self.set_alarms_text = tki.Label(self.master, text = "Next 3 alarms")
        # self.set_alarms_text.grid(row = 2, column = 0)

        self.set_alarms_box = tki.LabelFrame(self.master, text = "Up Next", height = 68, width = 585, bg = "#ffffff")
        self.set_alarms_box.grid(row = 3, padx = [2,0], pady = [7, 0], column = 0, columnspan = 8)

        self.menu = tki.Menu(self.master)
        self.master.configure(menu = self.menu)
        self.menu.add_cascade(label = "Alarm")
        self.menu.add_cascade(label = "Pomodoro")
        self.menu.add_cascade(label = "Stop Watch")
        self.menu.add_cascade(label = "Settings")
        self.menu.add_cascade(label = "Help")

    def click_add(self):
        add_alarm = tki.Toplevel()

        add_alarm.transient(self.master)

        add_alarm.minsize(390, 350)
        add_alarm.maxsize(390, 350)

        add_alarm.title("Add Alarm")

        Add(add_alarm, self.storage)
