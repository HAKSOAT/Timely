import tkinter as tki
from alarm_ui import AlarmUI
import threading

window = tki.Tk()

window.minsize(600, 430)
window.maxsize(600, 430)
window.title("Timely")

AlarmUI(window)

window.mainloop()
