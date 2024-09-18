import tkinter as tk
from tkinter import messagebox


'''Main window '''
window = tk.Tk()
window.title("ATM")
window.configure(bg='light grey')



'''------Label for instructions-------'''

label = tk.Label(window, text="Please Enter Your PIN", font=("Arial", 16))
label.grid(row=0, column=2, columnspan=4, pady=(40, 40))
label.configure(bg='Red',fg='White')


'''--------------- Entry field to input PIN or withdrawal amount-------'''


entry = tk.Entry(window, font=("Arial", 40), show="*", width=10, justify="center")  
entry.grid(row=1, column=2, columnspan=3, pady=(0, 60))
entry.configure(bg='lightblue',fg='green')

# State to keep track of PIN or withdrawal mode
Input_value = tk.StringVar(value='pin') 


def button_click(value):
    # Append digits based on the current state (PIN or withdrawal)
    if Input_value .get() == 'pin':
        current_text = entry.get()
        if len(current_text) < 4:  # Restrict PIN to 4 digits
            entry.insert(tk.END, value)
    elif Input_value.get() == 'withdraw':
        entry.insert(tk.END, value)



'''--- Numeric buttons---- '''

buttons = [
    ('1', 2, 2), ('2', 2, 3), ('3', 2, 4),
    ('4', 3, 2), ('5', 3, 3), ('6', 3, 4),
    ('7', 4, 2), ('8', 4, 3), ('9', 4, 4),
    ('0', 5, 3)
]


for (text, row, col) in buttons:
    button = tk.Button(window, text=text, font=("Arial", 14), width=5, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=30, pady=5,sticky='E')


''' --------Cancel, Clear, and Enter buttons------'''

def cancel():
    # Close the window
    window.destroy()

cancel_button = tk.Button(window, text="X", font=("Arial", 15), bg="red",fg='white', width=5, command=cancel)
cancel_button.grid(row=6, column=3, padx=5, pady=5)

def clear():
    # Clear the entry field
    entry.delete(0, tk.END)
clear_button = tk.Button(window, text="Clear", font=("Arial", 15), bg="orange",fg='white',width=5, command=clear)
clear_button.grid(row=5, column=2, padx=5, pady=10)

def Enter():
    # Handling PIN entry and withdrawal transaction
    if Input_value.get() == 'pin':
        entered_pin = entry.get()
        if entered_pin == "1234":
            messagebox.showinfo("ATM", "PIN Accepted!")
            Input_value.set('withdraw')
            label.config(text="Enter Amount to Withdraw")
            entry.config(show="")  # Remove masking 
            clear()
        else:
            messagebox.showwarning("ATM", "Invalid PIN!")
            clear()
    elif Input_value.get() == 'withdraw':
        amount = entry.get()
        messagebox.showinfo("ATM", f"₹{amount} Withdrawn Successfully!")
        clear()
        Input_value.set('pin')
        label.config(text="Please Enter Your PIN")
        entry.config(show="*")  # Reapply masking for PIN entry

enter_button = tk.Button(window, text="Enter", font=("Arial", 14), bg="green",fg='white', width=5, command=Enter)
enter_button.grid(row=5, column=4, pady=5)


'''----Run the application-----'''
window.mainloop()
