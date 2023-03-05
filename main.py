from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(string='Cronometru tip Pomodoro')
window.config(padx=100, pady=50, bg=RED)

canvas = Canvas(width=200, height=223, bg=RED, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato_img)
canvas.create_text(100, 114, text='00:00', font=(FONT_NAME, 35, 'bold'), fill='blue')

canvas.pack()




window.mainloop()