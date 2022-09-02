# temperature converter using tkinter. This programs converts from celcius to fahrenheit.
# by sandeep

# To do:
    # without button is giving some sort of error. dont' know wht
    # therefore try adding button tomorrow.


import tkinter as tk

def convert(event):
    # without button is giving some sort of error. dont' know wht
    # therefore try adding button tomorrow.

    if ent_c.get() != "":
        c = ent_c.get()
        c = float(c)
        f = (c * 9/5) + 32
        lbl_fhr["text"] = f"{f}"


window = tk.Tk()

window.rowconfigure(1, minsize=100)

# Creating placeholder(where user types and result will be shown.)
ent_c = tk.Entry(width=20)
ent_c.grid(row=1, column=0, sticky="nsew", padx=5)

lbl_sign = tk.Label(text="=")
lbl_sign.grid(row=1, column=1, sticky="nsew")

lbl_fhr = tk.Label(text="0", width=20)
lbl_fhr.grid(row=1, column=2, sticky="nsew")


#Creating labels
lbl_c = tk.Label(text="Celcius")
lbl_f = tk.Label(text="Fahrenheit")

lbl_c.grid(row=0, column=0)
lbl_f.grid(row=0, column=2)

# Create buttons
btn = tk.Button(text="Convert")
btn.grid(row=2, column=1, padx=5, pady=10)

btn.bind("<Button-1>", convert)

# You can also press enter to convert.
# this below is something like google converter where you type a...
# number and press enter on you keyboard and it will convert and ...
# show it in next bar.
ent_c.bind("<Return>", convert)

window.mainloop()
