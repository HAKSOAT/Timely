import tkinter as tki
from PIL import Image, ImageTk
from add import Add

class AlarmUI():

    def __init__(self, master):
        self.master = master

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

        self.alarm_box = tki.Canvas(self.master, bg = '#000fff000')
        self.alarm_box.grid(row = 1, column = 0, pady = 5, ipadx = 105, padx = 5, columnspan = 8)

        self.set_alarms_text = tki.Label(self.master, text = "Next 3 alarms")
        self.set_alarms_text.grid(row = 2, column = 0)

        self.set_alarms_box = tki.Entry(self.master)
        self.set_alarms_box.grid(row = 3, column = 0, ipady = 25, ipadx = 222, padx = 5, columnspan = 8)

        self.menu = tki.Menu(self.master)
        self.master.configure(menu = self.menu)
        self.menu.add_cascade(label = "Alarm")
        self.menu.add_cascade(label = "Pomodoro")
        self.menu.add_cascade(label = "Stop Watch")
        self.menu.add_cascade(label = "Settings")
        self.menu.add_cascade(label = "Help")

    def click_add(self):
        add_alarm = tki.Toplevel()

        add_alarm.minsize(385, 230)
        add_alarm.maxsize(385, 230)

        add_alarm.title("Add Alarm")

        Add(add_alarm)
