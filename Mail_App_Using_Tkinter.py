import smtplib
import tkinter as tk
from tkinter.filedialog import askopenfilename

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_mail():
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.starttls()

    mail.login("smtptestmail6969@gmail.com", "smtpsmtpsmtp")

    msg['Subject'] = subject.get()
    msg['To'] = to_field.get()
    msg['From'] = from_field.get()
    text = content.get("1.0", "end")

    text = MIMEText(text, 'html')
    msg.attach(text)

    try:
        mail.sendmail(from_field.get(), to_field.get(), msg.as_string())
        mail.close()
        print("Mail sent succesfully!")
    except:
        print("Failed!")


def attach_file():
    
    attachment = askopenfilename(filetypes=[("All files", "*.*")], initialdir="~/Desktop")
    filename = str(attachment).split('/')[-1]

    the_file = open(attachment, "rb")

    mb = MIMEBase('application', 'octet-stream')
    mb.set_payload((the_file).read())
    encoders.encode_base64(mb)
    mb.add_header('Content-Disposition', "attachment; filename = %s" %filename)

    msg.attach(mb)

    attached.config(text="%s attached" %filename)
    attachment_button.config(text="File attached")


root = tk.Tk()
root.title("SMTP_Mail APP")
root.geometry("550x300")

to_label = tk.Label(root, text="To:")
to_label.grid(column=0, row=0, padx=5)

to_field = tk.Entry(root, width=40)
to_field.grid(column=1, row=0, padx=5)

from_label = tk.Label(root, text="From:")
from_label.grid(column=0, row=1, padx=5)

from_field = tk.Entry(root, width=40)
from_field.grid(column=1, row=1, padx=5)

subject_label = tk.Label(root, text="Subject:")
subject_label.grid(column=0, row=2, padx=5)

subject = tk.Entry(root, width=40)
subject.grid(column=1, row=2, padx=5)

content_label = tk.Label(root, text="Body:")
content_label.grid(column=0, row=3, padx=5)

content = tk.Text(root, width=50, height=10, borderwidth=2)
content.grid(column=1, row=3, pady=10)

send = tk.Button(root, text="Send", command=send_mail)
send.grid(row=10, column=5)

attachment_button = tk.Button(root, text="Attach", command=attach_file)
attachment_button.grid(row=10, column=0)

attached = tk.Label(root, text="")
attached.grid(row=10, column=1)

msg = MIMEMultipart('alternative')

root.mainloop()
