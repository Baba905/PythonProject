from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_count = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_count)
    timer.config(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text=f"00:00")
    global reps
    reps =0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN *60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps% 2 == 1 :
        print("Work")
        timer.config(text="Work",font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
        count_down(work_sec)

    elif reps == 8 :
        print("Long")
        timer.config(text="Break", font=(FONT_NAME, 35), fg=RED, bg=YELLOW)
        count_down(long_break_sec)

    else:
        print("Short")
        timer.config(text="Break", font=(FONT_NAME, 35), fg=PINK, bg=YELLOW)
        count_down(short_break_sec)

    print(f"Reps : {reps}")

    #count_down(long_break_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0"+str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global  timer_count
        timer_count =window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps%2==0:
            tmp = check["text"]+ "✔ "
            check.config(text=tmp)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=7)

# Timer label
timer = Label(text="Timer", font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button
start = Button(text="Start")
start["command"] = start_timer
start.grid(column=0, row=2)

# Reset button
reset = Button(text="Reset", command= reset_timer)
reset.grid(column=2, row=2)

# Check mark label
check = Label(text="", font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)
window.mainloop()
