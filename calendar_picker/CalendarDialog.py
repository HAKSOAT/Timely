import tkinter
from calendar_picker import ttkcalendar

from calendar_picker import tkSimpleDialog


class CalendarDialog(tkSimpleDialog.Dialog):
    """Dialog box that displays a calendar and returns the selected date"""

    def body(self, master):
        self.calendar = ttkcalendar.Calendar(master)
        self.calendar.pack()

    def apply(self):
        self.result = self.calendar.selection

# Demo code:


class CalendarFrame(tkinter.LabelFrame):
    def __init__(self, master):
        tkinter.LabelFrame.__init__(self, master)

        def getdate():
            cd = CalendarDialog(self)
            result = cd.result
            try:
                self.date_box["state"] = tkinter.NORMAL
                self.selected_date.set(result.strftime("%m/%d/%Y"))
                self.date_box["state"] = tkinter.DISABLED
            except AttributeError:
                pass

        self.selected_date = tkinter.StringVar()

        self.date_box = tkinter.Entry(self, textvariable=self.selected_date, state = tkinter.DISABLED)
        self.date_box.pack(side=tkinter.TOP)
        tkinter.Button(self, text="Choose a date", command=getdate).pack(side=tkinter.TOP)


# def main(master):
#     calendar_frame = CalendarFrame(master)
#     calendar_frame.grid(row = 3, column = 0, columnspan = 2, pady = [50,10])
# if __name__ == "__main__":
#     main(master)
