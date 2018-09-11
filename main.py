import tkinter as tki
from alarm_ui import AlarmUI


window = tki.Tk()

window.minsize(600, 395)
window.maxsize(600, 395)
window.title("Timely")

img = tki.PhotoImage(file='icons/timely-icon.gif')
window.tk.call('wm', 'iconphoto', window._w, img)

AlarmUI(window)

window.mainloop()
