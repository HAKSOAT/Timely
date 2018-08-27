import tkinter as tki

class CheckedButtons():

    def __init__(self, checkbutton_states):
        self.checkbutton_states = checkbutton_states

    def check_label_n_state(self):
        labels_n_states = []
        for button, variable, label in self.checkbutton_states:
            labels_n_states.append([label, variable.get()])
        return labels_n_states
