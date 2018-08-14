import tkinter as tki

class Add():

    def __init__(self, master):
        self.master = master

        self.units_hour = tki.Text(self.master, height = 5, width = 10, state = tki.DISABLED)
        self.units_hour.grid(row = 0, column = 0, padx = 10, pady = [20,0])

        self.tens_hour = tki.Text(self.master, height = 5, width = 10, state = tki.DISABLED)
        self.tens_hour.grid(row = 0, column = 1, padx = 10, pady = [20,0])

        self.units_minutes = tki.Text(self.master, height = 5, width = 10, state = tki.DISABLED)
        self.units_minutes.grid(row = 0, column = 2, padx = 10, pady = [20,0])

        self.tens_minutes = tki.Text(self.master, height = 5, width = 10, state = tki.DISABLED)
        self.tens_minutes.grid(row = 0, column = 3, padx = 10, pady = [20,0])

        self.add_button = tki.Button(self.master, text = "Add Alarm", padx = 35)
        self.add_button.grid(row = 3, column = 1, columnspan = 2, pady = 20)

        for each in range(0,4):
            up_arrow = tki.PhotoImage(file = "arrow-141-16.gif")

            self.increase = tki.Button(self.master, image = up_arrow)
            self.increase.image = up_arrow
            self.increase.grid(row = 1, column = each, pady = [20,0])

            down_arrow = tki.PhotoImage(file = "arrow-204-16.gif")

            self.decrease = tki.Button(self.master, image = down_arrow)
            self.decrease.image = down_arrow
            self.decrease.grid(row = 2, column = each)

        self.text_widgets = self.master.winfo_children()[:4]
        self.init_zero(self.text_widgets)

    def init_zero(self, text_widgets):
        for each in text_widgets:
            each["state"] = tki.NORMAL
            each.insert(tki.END, "\n\t0")
            each["state"] = tki.DISABLED
