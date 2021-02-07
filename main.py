import tkinter
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
WORK_BREAK_SEQUENCE = (WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, SHORT_BREAK_MIN,
                       WORK_MIN, SHORT_BREAK_MIN, WORK_MIN, LONG_BREAK_MIN)

UI_SET = {SHORT_BREAK_MIN: [PINK, "Short Break"], WORK_MIN: [RED, "Work"], LONG_BREAK_MIN: [GREEN, "Long Break"]}
STAGE = 0
Check = "✓"
LICZNIK = None
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def initiate_count():
    """Initiate the count by pressing start button"""
    global STAGE
    global UI_SET

    timer_label.config(text=UI_SET[WORK_BREAK_SEQUENCE[STAGE]][1],
                       fg=UI_SET[WORK_BREAK_SEQUENCE[STAGE]][0])

    count_down(WORK_BREAK_SEQUENCE[STAGE] * 60)
    STAGE +=1
    if  STAGE > len(WORK_BREAK_SEQUENCE)-1:
        STAGE = 0


def reset_count():
    global LICZNIK
    global STAGE
    window.after_cancel(LICZNIK)
    canvas.itemconfig(zegar, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    tic_label.config(text="")
    STAGE = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(seconds):
    """Decrement every ct>0, -1 every 1 second until reaches 0"""
    global STAGE
    global Check
    min = math.floor(seconds / 60)
    sec = seconds % 60
    canvas.itemconfig(zegar, text="{}:{}".format(str(min).rjust(2, "0"), str(sec).rjust(2, "0")))
    if seconds != 0:
        global LICZNIK
        LICZNIK = window.after(1000, count_down,  seconds - 1)
    elif seconds == 0:
        tic_label["text"] += Check
        window.after(1000, initiate_count)

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.config(padx=40, pady=40, bg=YELLOW)
window.title("Pomodoro App")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomidor = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomidor)

zegar = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row=2, column=2)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=1, column=2)

button_start = tkinter.Button(text="START", font=(FONT_NAME, 14), command=initiate_count)
button_start.grid(row=3, column=1)

button_reset = tkinter.Button(text="RESET", font=(FONT_NAME, 14), command=reset_count)
button_reset.grid(row=3, column=3)

tic_label = tkinter.Label(text="", fg=GREEN, font=(14), bg=YELLOW)
tic_label.grid(row=4, column=2)

window.mainloop()