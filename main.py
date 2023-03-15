from tkinter import *
from tkinter import messagebox
import sys
import time

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

minute = 25
secunde = 59


def start_timer():
    window.after(1000, cronometru, secunde, minute)
    canvas.itemconfig(timer_start, text=f'{minute}, {secunde}', font=(FONT_NAME, 35, 'bold'), fill='blue')



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def cronometru(secunde_par, min_par):
    global secunde
    global minute
    print(secunde)
    secunde = secunde - 1
    if secunde == 0:
        minute = minute - 1
        secunde = 59
    # window.after(1000, cronometru, secunde, minute)
    start_timer()



# ---------------------------- UI SETUP ------------------------------- #
def exit_progr():
    question = messagebox.askquestion(message='Esti sigur ca vrei sa iesi?')
    if question == 'yes':
        sys.exit()
    else:
        pass


window = Tk()
window.title(string='Cronometru tip Pomodoro')
window.config(padx=25, pady=25, bg=RED)
canvas = Canvas(width=200, height=223, bg=RED, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato_img)

timer_start = canvas.create_text(100, 114, text=f'{minute}, {secunde}', font=(FONT_NAME, 35, 'bold'), fill='blue')
canvas.grid(column=1, row=1)

timer_panel = Label(text='Timer', font=('arial', 30), bg=RED, fg=GREEN)
timer_panel.grid(column=1, row=0)

but_start = Button(text='Start', bg=YELLOW, highlightthickness=0, command=start_timer)
but_start.grid(column=0, row=2)

but_reset = Button(text='Reset', bg=YELLOW, highlightthickness=0)
but_reset.grid(column=2, row=2)

but_exit = Button(text='Exit', command=exit_progr, fg=RED, highlightthickness=0)
but_exit.grid(column=3, row=2)

check_mark = Label(text='✅', font=('arial', 30), bg=RED, fg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
