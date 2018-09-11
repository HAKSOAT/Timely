import tkinter as tki

class AlarmPopUp():
    def __init__(self, master, alarm_box, storage, get_ringtime, call_popup, time_index):
        self.master = master
        self.storage = storage
        self.alarm_box = alarm_box
        self.get_ringtime = get_ringtime
        self.call_popup = call_popup

        self.storage.connect()
        self.db_result = self.storage.query(time_index)[0]
        self.year = self.db_result[1]
        self.month = self.db_result[2]
        self.day = self.db_result[3]
        self.hour = int(self.db_result[4])
        self.minute = int(self.db_result[5])
        self.tone = self.db_result[6]
        self.time_index = time_index


    def display(self, ring, tone):
        self.pop_up = tki.Toplevel()

        self.pop_up.transient(self.master)

        self.pop_up.minsize(390, 350)
        self.pop_up.maxsize(390, 350)

        self.pop_up.title("Arise And Shine!!!")

        self.player = ring(tone)

        self.spacing = tki.Label(self.pop_up, text = "", pady = 3)
        self.spacing.pack()

        self.image = "icons/alarm-clock.gif"
        self.tk_photo = tki.PhotoImage(file = self.image)
        self.image_label = tki.Label(self.pop_up, image = self.tk_photo)
        self.image_label.image = self.tk_photo
        self.image_label.pack()

        self.spacing.pack()

        close = tki.Button(self.pop_up, text = "Dismiss", pady = 10, command = self.click_dismiss)
        close.pack(fill = tki.X, side = tki.LEFT, expand = True)

        snooze = tki.Button(self.pop_up, text = "Snooze", pady = 10, command = self.click_snooze)
        snooze.pack(fill = tki.X, side = tki.LEFT, expand = True)

    def click_dismiss(self):
        self.player.music.stop()
        self.alarm_box.delete()
        self.get_ringtime()
        self.call_popup()
        self.alarm_box.get_alarm()
        self.pop_up.destroy()

    def click_snooze(self):

        if self.minute <= 54:
            self.minute += 5
        elif self.minute == 55:
            self.minute = 0
            self.hour += 1
            self.apply_snooze_increments()
        elif self.minute == 56:
            self.minute = 1
            self.hour += 1
            self.apply_snooze_increments()
        elif self.minute == 57:
            self.minute = 2
            self.hour += 1
            self.apply_snooze_increments()
        elif self.minute == 58:
            self.minute = 3
            self.hour += 1
            self.apply_snooze_increments()
        elif self.minute == 59:
            self.minute = 4
            self.hour += 1
            self.apply_snooze_increments()

        self.hour = "{:02d}".format(self.hour)
        self.minute = "{:02d}".format(self.minute)

        self.storage.connect()
        self.storage.update(self.time_index, self.year, self.month, self.day,
                            self.hour, self.minute, self.tone)
        self.storage.commit()
        self.storage.close()

        self.click_dismiss()

    def apply_snooze_increments(self):
        if self.hour == 24:
            self.hour = 0
            self.day += 1
            if self.day == 31 and self.month in [4, 6, 9, 11]:
                self.month += 1
                if self.month == 13:
                    self.month = 1
                    self.year += 1
            elif self.day == 32 and self.month not in [4, 6, 9, 11]:
                self.month += 1
                if self.month == 13:
                    self.month = 1
                    self.year += 1
