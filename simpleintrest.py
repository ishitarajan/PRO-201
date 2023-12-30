from tkinter import *
window = Tk()
window.title('Simple Intrest Calculator')
window.geometry("380x400")
window.configure(bg='#DCC1AF')

def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)
    result_label.destroy()
    msg="Your Simple Intrest is "
    output_message=Label(result_frame, text = msg+str(interest), bg = "#DCC1AF", font=("Calibri", 12), width = 42)
    output_message.place(x = 20, y=40)
    output_message.pack()

app_label=Label(window, text="Simple Interest Calculator", fg = "black", bg = "#E8AE88", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

p_label=Label(window, text="Enter Principle", fg = "black", bg = "#DCC1AF", font=("Calibri", 12),bd=1)
p_label.place(x=20, y=90)
principle=Entry(window, text="", bd=2, width=15)
principle.place(x=170, y=92)

r_label=Label(window, text="Enter Rate of Interest", fg = "black", bg = "#DCC1AF", font=("Calibri", 12))
r_label.place(x=20, y=140)
rate =Entry(window, text="", bd=2, width=15)
rate.place(x=170, y=142)

t_label=Label(window, text="Enter Time", fg = "black", bg = "#DCC1AF", font=("Calibri", 12))
t_label.place(x=20, y=185)
time=Entry(window, text="", bd=2, width=15)
time.place(x=170, y=187)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "#617C58", bd=4,command=calculate_interest)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "#DCC1AF", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "#F7D0C0", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()