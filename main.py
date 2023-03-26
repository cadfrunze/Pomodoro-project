from tkinter import *
from tkinter import messagebox
import sys
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
parcurgere = 0
timer = None
proba = True


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global proba
    global parcurgere
    question = messagebox.askquestion(message='Esti sigur ca doresti sa resetezi cronometrul??')
    if question == 'yes':
        window.after_cancel(timer)
        proba = True
        parcurgere = 0
        but_start = Button(text='Start', bg=YELLOW, highlightthickness=0, fg='black', command=click_cronometru)
        but_start.grid(column=0, row=2)
        timer_panel.config(text='Timer')
        canvas.itemconfig(timer_start, text=f'{WORK_MIN % 60}:0{math.floor(WORK_MIN / 60)}')
        check_mark.config(text='')
    else:
        pass


# ---------------------------- TIMER MECHANISM ------------------------------- #


def click_cronometru():
    global parcurgere
    global proba
    if proba:
        proba = False
        but_start = Label(text='Start', bg=YELLOW, highlightthickness=0, fg='gray')
        but_start.grid(column=0, row=2)
        start_cronometru()
    else:
        pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_cronometru():
    global parcurgere
    parcurgere += 1
    if parcurgere == 1 or parcurgere == 3 or parcurgere == 5:
        timer_panel.config(fg=YELLOW, text='Work')
        cronometru(count=WORK_MIN * 60)
    elif parcurgere == 2 or parcurgere == 4 or parcurgere == 6:
        timer_panel.config(fg=GREEN, text='Short Break')
        cronometru(count=SHORT_BREAK_MIN * 60)
    elif parcurgere == 8:
        timer_panel.config(fg=YELLOW, text='Long Break')
        cronometru(count=LONG_BREAK_MIN * 60)
        parcurgere = 0


def cronometru(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f'0{count_min}'
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_start, text=f'{count_min}:{count_sec}')
    count_min = int(count_min)
    count_sec = int(count_sec)

    if count_min == 0 and count_sec == 0:
        start_cronometru()
        marks = ''
        work_session = math.floor(parcurgere / 2)
        for _ in range(work_session):
            marks += '✅'
        check_mark.config(text=marks)

    else:
        global timer
        timer = window.after(1000, cronometru, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
def exit_progr():
    question = messagebox.askquestion(message='Esti sigur ca vrei sa iesi?')
    if question == 'yes':
        sys.exit()
    else:
        pass


window = Tk()
window.title(string='Timer de tip Pomodoro')
window.config(padx=25, pady=25, bg=RED)
canvas = Canvas(width=200, height=223, bg=RED, highlightthickness=0)

tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato_img)

timer_start = canvas.create_text(100, 114, text=f'{WORK_MIN % 60}:0{math.floor(WORK_MIN / 60)}',
                                 font=(FONT_NAME, 35, 'bold'), fill='blue')
canvas.grid(column=1, row=1)
timer_panel = Label(text='Timer', font=('arial', 30), bg=RED, fg=GREEN)
timer_panel.grid(column=1, row=0)

but_start = Button(text='Start', bg=YELLOW, highlightthickness=0, command=click_cronometru)
but_start.grid(column=0, row=2)

but_reset = Button(text='Reset', bg=YELLOW, highlightthickness=0, command=reset)
but_reset.grid(column=2, row=2)

but_exit = Button(text='Exit', command=exit_progr, fg=RED, highlightthickness=0)
but_exit.grid(column=3, row=2)

check_mark = Label(font=('arial', 20), bg=RED, fg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()
