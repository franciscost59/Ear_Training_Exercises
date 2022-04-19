# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 12:04:14 2022

@author: francisco.barros
"""

from tkinter import *

from tkinter.ttk import *

window = Tk()

input_scales = Combobox(window)

window.title("Ear Training app")

window.geometry('450x300')

input_scales = Combobox(window)

input_scales['values']= ("Major_Scale", "Minor_Melodic", "Major_Harmonic", "Minor_Harmonic"
                  , "Chromatic_Scale")

input_scales.current(0) #set the selected item

input_scales.grid(column=2, row=0)

input_scales_txt = Label(window, text="Select Scale Input")

input_scales_txt.grid(column=0, row=0)

exercises = Spinbox(window, from_=0, to=10, width=5)

exercises.grid(column=2,row=2)

number_exercises = Label(window, text="Select Number of Exercises")

number_exercises.grid(column=0, row=2)

notes = Spinbox(window, from_=1, to=12, width=5)

notes.grid(column=2,row=4)

number_notes = Label(window, text="Select Number Notes of Per Exercise")

number_notes.grid(column=0, row=4)

octave = Spinbox(window, from_=0, to=10, width=5)

octave.grid(column=2,row=6)

number_octave = Label(window, text="Select Octave")

number_octave.grid(column=0, row=6)

window.mainloop()