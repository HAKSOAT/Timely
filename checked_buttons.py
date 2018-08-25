import tkinter as tki

class CheckedButtons():

    def __init__(self, checkbutton_states):
        self.checkbutton_states = checkbutton_states

    def check_state(self):
        states = []
        for button, variable in self.checkbutton_states:
            states.append(variable.get())
        return states
