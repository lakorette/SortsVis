import numpy as np
import settings
import sets
import functions as f
import tkinter as tk

st = settings.Settings()


root = tk.Tk()
root.title("animation")
window = tk.Canvas(root, height = st.window_h, width = st.window_w, background = st.background_c)
window.pack()

array = sets.Set(window = window)
array.scramble()
array.bubble_sort()
array.scramble()
array.selection_sort()
array.scramble()
array.insertion_sort()
array.scramble()
array.shell_sort()


root.mainloop()

