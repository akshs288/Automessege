import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import pywhatkit as pyt

# Initialize the main window
root = tk.Tk()
root.title("Auto Messenger App")
root.geometry("500x724")
root.resizable(False, False)

# def motion(event):
#     print(f"Mouse at x={event.x}, y={event.y}")
# root.bind("<Motion>", motion)

'''Creating a title for Window'''

tit_= tk.Label(root, text = "Automated Message", font=("Comic Sans MS", 20), fg="black", bg="light blue")
tit_.pack(fill = "x", padx= 4)
tit_.config(justify="center", anchor="center")

# Load and set background image
img = Image.open("Mega projects/bg.png").resize((500, 867), Image.LANCZOS)
bg = ImageTk.PhotoImage(img)
l1 = tk.Label(root, image=bg)
l1.pack()

# Labels and Entry for sender's number

l1 = tk.Label(root, text="From: ", font=("Comic Sans MS", 10), fg="black", bg="light blue")
l1.place(x = 12, y = 82)
la = tk.Label(root, text="Enter your number: ", font=("Comic Sans MS", 10), fg="black", bg="light blue")
la.place(x = 70, y = 120)
entr = tk.Entry(root, font=("Comic Sans MS", 10), fg="black", bg="light blue")
entr.place(x=129, y=159)
# Labels and Entry for receiver's number
l2 = tk.Label(root, text="To: ", font=("Comic Sans MS", 10), fg="black", bg="light blue")
l2.place(x=12, y=209)
l3 = tk.Label(root, text="Enter Reciever's Number: ", font=("Comic Sans MS", 10), fg="black", bg="light blue")
l3.place(x = 60, y = 240)
entr2 = tk.Entry(root, font=("Comic Sans MS", 10), fg="black", bg="light blue")
entr2.place(x=129, y=284)
ask = tk.Label(root, text = "Enter platform:-", font=("Comic Sans MS", 16), bg = "light blue")

but = tk.Button(root, text="Done", font=("Comic Sans MS", 14), fg="black", bg="light blue", command=lambda: func2())
but.place(x=9, y=335, width=110, height=29)

def func():
    num = entr2.get().strip().replace(" ", "")
    if num.startswith("+") and len(num) == 13:
        messagebox.showinfo("Checking...", "Phone number format is correct.")
        mese.place(x=219, y=338)
        lab.place(x=9, y=374, width=397, height=106)
        scroll.place(x=405, y=374, height=106)
        d.place(x=9, y=485)
        dc.place(x=12, y=590)
        cal.place(x=76, y=592)
        time_label.place(x=220, y=555)
        hour_label.place(x=220, y=590)
        hour_entry.place(x=270, y=590, width=50)
        minute_label.place(x=330, y=590)
        minute_entry.place(x=400, y=590, width=50)
        end.place(x=12, y=639, width=190)
        alt.place(x = 226, y = 639, width= 190)
    else:
        messagebox.showerror("Error", "Please enter a valid international number (e.g., +919876543210).")

def func2():
    # aa = a2.get()
    but2 = tk.Button(root, text = "Done", font = ("Comic Sans MS", 14), fg = "black", bg ="light blue", command = lambda: func())
    but2.place(x=9, y=335, width=110, height=29)

# Message input section
mese = tk.Label(root, text="Enter your Message Here:", font=("Comic Sans MS", 10), fg="black")
lab = tk.Text(root, font=("Comic Sans MS", 10), fg="black", wrap="word")
scroll = tk.Scrollbar(root, command=lab.yview)
lab.config(yscrollcommand=scroll.set)
# Date and time selection for scheduled messages
d = tk.Label(root, text="Date & time on which\n you want to send Message", font=("Comic Sans MS",12),fg="black", bg="light blue")
dc = tk.Label(root, text="Date", font=("Comic Sans MS", 12),bg = "light blue", fg="black")
time_label = tk.Label(root, text="Time (24H Format)", font=("Comic Sans MS", 12),bg = "light blue", fg="black")
hour_label = tk.Label(root, text="Hour", font=("Comic Sans MS", 10),bg = "light blue", fg="black")
hour_entry = tk.Entry(root, width=5, font=("Comic Sans MS", 10))
cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
end = tk.Button(root, text="Send at time", font=("Comic Sans MS", 12),bg = "light blue",fg="black",command=lambda: send_messe())
alt = tk.Button(root, text = "Send Now", font=("Comic Sans MS", 12),fg="black", bg="light blue",command = lambda : now_())
minute_label = tk.Label(root, text="Minute", font=("Comic Sans MS", 10), fg="black", bg="light blue")
minute_entry = tk.Entry(root, width=5, font=("Comic Sans MS", 10))

# Hide elements initially
for i in [mese, lab, scroll, d, dc, cal,end, alt]:
    i.place_forget()

# Function to send message
def send_messe():
    receiver_num = entr2.get().strip().replace(" ", "")
    message = lab.get("1.0", "end-1c").strip()
    print(f"DEBUG: Sending message to {receiver_num} with content: '{message}'")
    
    if not receiver_num.startswith("+"):
        messagebox.showerror("Error", "Please enter the number in international format (e.g., +919876543210).")
        return
    
    if not message:
        messagebox.showerror("Error", "Message cannot be empty!")
        return

    try:
        hor = int(hour_entry.get())
        mina = int(minute_entry.get())
        pyt.sendwhatmsg(receiver_num, message, hor, mina)
        print(f"Message will be sent at {hour_entry.get()} : {minute_entry.get()}")
        messagebox.showinfo("Success", "Message sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send message:\n{str(e)}")

def now_():
    message = lab.get("1.0", "end-1c").strip()
    user_num = entr2.get().strip().replace(" ", "")
    
    if not user_num.startswith("+91"):
        messagebox.showinfo("Error", "Please put +91 at the starting of the number.")

    if not message:
        messagebox.showinfo("Error", "Please write something the text")
    
    else:
        vb = str(entr2.get())
        pyt.sendwhatmsg_instantly(vb, message)

# Start the GUI event loop
root.mainloop()