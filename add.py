import tkinter as tki
from functools import partial

class Add():

    def __init__(self, master):
        self.master = master

        self.tens_hour = tki.Label(self.master, height = 2, width = 6, text = 0, font=("Helvetica", 16, "bold"))
        self.tens_hour.grid(row = 0, column = 0, padx = [2,10], pady = [20,0])

        self.units_hour = tki.Label(self.master, height = 2, width = 6, text = 0, font=("Helvetica", 16, "bold"))
        self.units_hour.grid(row = 0, column = 1, padx = 10, pady = [20,0])

        self.separator = tki.Label(self.master, height = 2, width = 1, text = ":", font=("Helvetica", 16, "bold"))
        self.separator.grid(row = 0, column = 2, padx = 5, pady = [20,0])

        self.tens_minutes = tki.Label(self.master, height = 2, width = 6, text = 0, font=("Helvetica", 16, "bold"))
        self.tens_minutes.grid(row = 0, column = 3, padx = 10, pady = [20,0])

        self.units_minutes = tki.Label(self.master, height = 2, width = 6, text = 0, font=("Helvetica", 16, "bold"))
        self.units_minutes.grid(row = 0, column = 4, padx = 10, pady = [20,0])

        self.add_button = tki.Button(self.master, text = "Add Alarm", padx = 35)
        self.add_button.grid(row = 3, column = 1, columnspan = 3, pady = 20)


        up_arrow = tki.PhotoImage(file = "arrow-141-16.gif")
        down_arrow = tki.PhotoImage(file = "arrow-204-16.gif")

        self.increase_one = tki.Button(self.master, image = up_arrow)
        self.increase_one.image = up_arrow
        self.increase_one.grid(row = 1, column = 0, pady = [20,0])

        self.increase_two = tki.Button(self.master, image = up_arrow)
        self.increase_two.image = up_arrow
        self.increase_two.grid(row = 1, column = 1, pady = [20,0])

        self.increase_three = tki.Button(self.master, image = up_arrow)
        self.increase_three.image = up_arrow
        self.increase_three.grid(row = 1, column = 3, pady = [20,0])

        self.increase_four = tki.Button(self.master, image = up_arrow)
        self.increase_four.image = up_arrow
        self.increase_four.grid(row = 1, column = 4, pady = [20,0])

        self.decrease_one = tki.Button(self.master, image = down_arrow)
        self.decrease_one.image = down_arrow
        self.decrease_one.grid(row = 2, column = 0)

        self.decrease_two = tki.Button(self.master, image = down_arrow)
        self.decrease_two.image = down_arrow
        self.decrease_two.grid(row = 2, column = 1)

        self.decrease_three = tki.Button(self.master, image = down_arrow)
        self.decrease_three.image = down_arrow
        self.decrease_three.grid(row = 2, column = 3)

        self.decrease_four = tki.Button(self.master, image = down_arrow)
        self.decrease_four.image = down_arrow
        self.decrease_four.grid(row = 2, column = 4)

        self.increase_one.bind("<Button-1>", self.increase)
        self.increase_two.bind("<Button-1>", self.increase)
        self.increase_three.bind("<Button-1>", self.increase)
        self.increase_four.bind("<Button-1>", self.increase)

        self.decrease_one.bind("<Button-1>", self.decrease)
        self.decrease_two.bind("<Button-1>", self.decrease)
        self.decrease_three.bind("<Button-1>", self.decrease)
        self.decrease_four.bind("<Button-1>", self.decrease)


    def increase(self, event):
        if self.increase_one.winfo_id == event.widget.winfo_id:
            self.tens_hour["text"] += 1

        elif self.increase_two.winfo_id == event.widget.winfo_id:
            self.units_hour["text"] += 1

        elif self.increase_three.winfo_id == event.widget.winfo_id:
            self.tens_minutes["text"] += 1
        else:
            self.units_minutes["text"] += 1

    def decrease(self, event):
        if self.decrease_one.winfo_id == event.widget.winfo_id:
            self.tens_hour["text"] -= 1

        elif self.decrease_two.winfo_id == event.widget.winfo_id:
            self.units_hour["text"] -= 1

        elif self.decrease_three.winfo_id == event.widget.winfo_id:
            self.tens_minutes["text"] -= 1
        else:
            self.units_minutes["text"] -= 1
