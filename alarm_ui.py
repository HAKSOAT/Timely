import tkinter as tki
from add import Add
from alarm_box import AlarmBox
from storage import AlarmStorage
from checked_buttons import CheckedButtons
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
        self.delete_bt = tki.Button(self.master, text = "Delete", image = photo, compound = "left", command = self.click_delete)
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

        self.alarm_box = AlarmBox(self.master, self.storage)
        self.alarm_box.show_alarm()

        self.button_state = []

        self.set_alarms_box = tki.LabelFrame(self.master, text = "Up Next", height = 68, width = 585, bg = "#ffffff")
        self.set_alarms_box.grid(row = 3, padx = [2,0], pady = [7, 0], column = 0, columnspan = 8)

        self.menu = tki.Menu(self.master)
        self.master.configure(menu = self.menu)
        self.menu.add_cascade(label = "Alarm")
        self.menu.add_cascade(label = "Pomodoro")
        self.menu.add_cascade(label = "Stop Watch")
        self.menu.add_cascade(label = "Settings")
        self.menu.add_cascade(label = "Help")

        self.delete_state = True

    def click_add(self):
        add_alarm = tki.Toplevel()

        add_alarm.transient(self.master)

        add_alarm.minsize(390, 350)
        add_alarm.maxsize(390, 350)

        add_alarm.title("Add Alarm")

        Add(add_alarm, self.storage, self.alarm_box)

    def click_delete(self):

        button_state = CheckedButtons(self.alarm_box.checkbutton_states).check_state()

        check_n_button_state = []

        for state in button_state:
            if state != "0":
                check_n_button_state += [state,state]
            else:
                check_n_button_state += ["0","0"]

        all_button_instances = self.alarm_box.alarm_canv.winfo_children()

        each_index = [index_ for index_, value in enumerate(check_n_button_state) if value != "0"]

        try:
            killed_buttons = [(all_button_instances[each], check_n_button_state[each]) for each in each_index]
        except IndexError:
            pass
        for each in killed_buttons:
            self.storage.connect()
            each[0].destroy()
            self.storage.delete(each[1])
            self.storage.commit()
            self.storage.close()
        self.alarm_box.show_alarm()
