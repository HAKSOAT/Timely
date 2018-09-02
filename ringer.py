import tkinter as tki
from datetime import datetime as dt
from popup import AlarmPopUp
from pygame import mixer

class Ringer():
    def __init__(self, master, storage, alarm_box):
        self.master = master
        self.storage = storage
        self.alarm_box = alarm_box

    def get_ringtime(self):
        self.ascending_ringtime = []
        self.storage.connect()
        db_result = self.storage.query()

        ringtime = []

        for each in db_result:
            set_time = dt.now().replace(year = int(each[1]), month = int(each[2]), day = int(each[3]),
                        hour = int(each[4]), minute = int(each[5]), second = 0)
            time_left = set_time - dt.now()
            tone = each[6]
            time_index = each[0]
            hour = each[4]
            minute = each[5]
            ringtime.append((time_left.total_seconds(), tone, [time_index, hour, minute]))

        self.ascending_ringtime = sorted(ringtime, key = lambda x: x[0])

    def ring(self, tone):
        player = mixer
        player.init()
        player.music.load(tone)
        player.music.play()
        return player

    def call_popup(self):
        for each in self.ascending_ringtime:
            if int(each[0]) >= 0:
                pop_up = AlarmPopUp(self.master, self.alarm_box, self.storage, self.get_ringtime, self.call_popup, each[2][0])
                self.master.after(int(each[0]) * 1000, pop_up.display, self.ring, each[1])
            else:
                self.storage.connect()
                self.storage.delete(each[2][0])
                self.storage.commit()
                self.storage.close()
