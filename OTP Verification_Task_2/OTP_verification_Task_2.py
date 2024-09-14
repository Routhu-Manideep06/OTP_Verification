import random
import smtplib
from tkinter import *
from PIL import Image, ImageTk  # Importing PIL for image handling

# New Colors for better appearance
bg_color = '#f0f4c3'  # Light yellow-green
label_color = '#000000' #Black
button_color = '#388e3c'  # Green 
button_text_color = '#ffffff'  # White


# Function to generate OTP
def generateOTP():
    randomCode = ''.join(str(random.randint(0, 9)) for i in range(6)) 
    return randomCode

sender = 'routhudeepu6@gmail.com'
password = 'gcjl svux bxuo ussp' 
code = generateOTP()

def connectingSender():
    receiver = receiverMail.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    sendingMail(receiver, server)

def sendingMail(receiver, server):
    msg = f'subject: OTP Verification\nHello! \nThis is your OTP: {code}'
    server.sendmail(sender, receiver, msg)
    server.quit()

def checkOTP():
    if code == codeEntry.get():
        accept = Label(otp, text='Successful Verification!', fg='green', font=('Arial', 16), bg=bg_color)
        accept.place(x=150, y=350)
    else:
        refuse = Label(otp, text='Unsuccessful Verification!', fg='red', font=('Arial', 16), bg=bg_color)
        refuse.place(x=150, y=350)

otp = Tk()
otp.title('OTP Verification')
otp.geometry('500x400') 
otp.config(bg=bg_color)

img = Image.open('image_validation.png')
img = img.resize((150, 120), Image.ANTIALIAS) 
photo = ImageTk.PhotoImage(img)
image_label = Label(otp, image=photo, bg=bg_color)
image_label.place(x=180, y=10) 

mailMsg = Label(otp, text="E-Mail", justify=LEFT, bg=bg_color, fg=label_color, font=("Arial", 14))
mailMsg.place(x=15, y=150)

receiverMail = Entry(otp, width=30, font=("Arial", 16), fg=label_color, borderwidth=2)
receiverMail.place(x=120, y=150)

sendOTP = Button(otp, text="Send OTP", width=10, height=1, font=("Arial", 16), bg=button_color, fg=button_text_color, command=connectingSender)
sendOTP.place(x=180, y=200)

otpMsg = Label(otp, text="OTP", bg=bg_color, fg=label_color, font=('Arial', 14))
otpMsg.place(x=15, y=260)

codeEntry = Entry(otp, width=8, font=("Arial", 16), borderwidth=2)
codeEntry.place(x=120, y=260)

verify = Button(otp, text="Verify", width=10, height=1, font=("Arial", 16), bg=button_color, fg=button_text_color, command=checkOTP)
verify.place(x=180, y=300)

otp.mainloop()
