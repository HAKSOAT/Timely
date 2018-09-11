import tkinter as tki
from alarm_ui import AlarmUI


window = tki.Tk()

window.minsize(600, 395)
window.maxsize(600, 395)
window.title("Timely")

AlarmUI(window)

window.mainloop()
