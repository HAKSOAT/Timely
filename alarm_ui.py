import os
import time
import tkinter as tki
from tkinter import messagebox
from alarm_config import Config
from alarm_box import AlarmBox
from storage import AlarmStorage
from ringer import Ringer
from checked_buttons import CheckedButtons


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

        self.button_images = ["icons/plus-16.gif", "icons/minus-16.gif",\
         "icons/edit-11-16.gif", "icons/copy-16.gif"]
        self.button_text = ["Add", "Delete", "Edit", "Clone"]
        self.button_actions = [self.click_add, self.click_delete, self.click_edit, self.click_clone]
        self.buttons = []

        for image, text, action in zip(self.button_images, self.button_text, self.button_actions):
            photo = tki.PhotoImage(file=image)
            button = tki.Button(self.master, text=text, image=photo,\
             compound="left", command=action)
            button.image = photo
            column_value = self.button_text.index(text)
            button.grid(row=0, column=column_value, sticky=tki.N + tki.E + tki.S + tki.W)
            self.buttons.append(button)

        self.alarm_box = AlarmBox(self.master, self.storage)
        self.ringer = Ringer(self.master, self.storage, self.alarm_box)
        self.ringer.get_ringtime()
        self.ringer.call_popup()
        self.alarm_box.get_alarm()

        self.button_state = []

    def click_add(self):
        add_alarm = tki.Toplevel()

        add_alarm.transient(self.master)

        add_alarm.minsize(493, 370)
        add_alarm.maxsize(493, 370)
        add_alarm.geometry('{}'.format(self.master.winfo_geometry()))

        add_alarm.title("Add Alarm")

        Config(add_alarm, self.storage, self.alarm_box, self.ringer)

    def click_delete(self):
        label_state = CheckedButtons(self.alarm_box.checklabel_states).check_label_n_state()
        ticked_boxes = [state for label, state in label_state if state == 1]
        no_ticked_boxes = len(ticked_boxes)
        if no_ticked_boxes >= 1:
            self.storage.connect()
            for label, state in label_state:
                if state == 1:
                    self.storage.delete(label["text"])
                    self.storage.commit()
            self.storage.close()
            self.alarm_box.delete()
            self.ringer.get_ringtime()
            self.ringer.call_popup()
            self.alarm_box.get_alarm()
        else:
            messagebox.showerror(title="Error!", message="Choose an alarm!")

    def click_clone(self):
        label_state = CheckedButtons(self.alarm_box.checklabel_states).check_label_n_state()
        ticked_boxes = [state for label, state in label_state if state == 1]
        no_ticked_boxes = len(ticked_boxes)
        if no_ticked_boxes >= 1:
            self.storage.connect()
            for label, state in label_state:
                if state == 1:
                    db_result = self.storage.query(label["text"])
                    time_index = time.time()
                    db_result = db_result[0]
                    self.storage.add(time_index, db_result[1], db_result[2],\
                     db_result[3], db_result[4], db_result[5], db_result[6])
                    self.storage.commit()

            self.storage.close()
            self.ringer.get_ringtime()
            self.ringer.call_popup()
            self.alarm_box.get_alarm()

        else:
            messagebox.showerror(title="Error!", message="Choose an alarm!")
    def click_edit(self):
        label_state = CheckedButtons(self.alarm_box.checklabel_states).check_label_n_state()
        ticked_boxes = [state for label, state in label_state if state == 1]
        no_ticked_boxes = len(ticked_boxes)
        if no_ticked_boxes == 1:
            self.storage.connect()
            for label, state in label_state:
                if state == 1:
                    edit_alarm = tki.Toplevel()
                    edit_alarm.transient(self.master)

                    edit_alarm.minsize(493, 370)
                    edit_alarm.maxsize(493, 370)
                    edit_alarm.geometry('{}'.format(self.master.winfo_geometry()))

                    edit_alarm.title("Edit Alarm")

                    db_result = self.storage.query(label["text"])
                    pretime_index = db_result[0][0]
                    pretime = db_result[0][4:6]
                    pretone = db_result[0][6]
                    predate = "{}/{}/{}".format(db_result[0][1], db_result[0][2], db_result[0][3])
                    Config(edit_alarm, self.storage, self.alarm_box, self.ringer,\
                    pretime, pretone, predate, pretime_index)

            self.storage.close()
            self.ringer.get_ringtime()
            self.ringer.call_popup()
            self.alarm_box.get_alarm()

        elif no_ticked_boxes > 1:
            messagebox.showerror(title="Error!", message="Edit one at a time!")
        else:
            messagebox.showerror(title="Error!", message="Choose an alarm!")
