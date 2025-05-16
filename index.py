import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import time
from datetime import datetime
import openpyxl

recipients = []

def log_result(email, status, error=None):
    with open("email_log.txt", "a") as log_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if status == "Success":
            log_file.write(f"[{timestamp}] Sent to {email} - SUCCESS\n")
        else:
            log_file.write(f"[{timestamp}] Failed to send to {email} - ERROR: {error}\n")

def collect_recipients():
    global recipients
    recipients = []
    method = method_var.get()
    lines = email_text_area.get("1.0", tk.END).strip().splitlines()
    for email in lines:
        if email:
            recipients.append((None, email.strip()))
    return True

def preview_emails():
    if not collect_recipients():
        return

    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END).strip()

    if not subject or not body:
        messagebox.showerror("Missing Fields", "Subject and body are required.")
        return

    preview_window = tk.Toplevel(app)
    preview_window.title("Email Preview")

    for name, email in recipients:
        personalized_body = body.replace("{name}", name if name else "there")
        preview_text = f"From: {email_entry.get()}\nTo: {email}\nSubject: {subject}\n\n{personalized_body}\n{'-'*60}\n"
        label = tk.Label(preview_window, text=preview_text, justify="left", anchor="w", font=("Courier", 10))
        label.pack(anchor="w", padx=10)

def send_emails():
    try:
        sender_email = email_entry.get()
        sender_password = password_entry.get()
        subject = subject_entry.get()
        body_template = body_text.get("1.0", tk.END).strip()
        cv_path = cv_file_path.get()

        if not all([sender_email, sender_password, subject, body_template, cv_path]):
            messagebox.showerror("Missing Fields", "Please fill out all fields and upload the necessary files.")
            return

        if not collect_recipients():
            return

        send_button.config(state="disabled")
        preview_button.config(state="disabled")
        progress_bar["maximum"] = len(recipients)
        progress_bar["value"] = 0

        for idx, (name, recipient_email) in enumerate(recipients, start=1):
            try:
                body = body_template.replace("{name}", name if name else "there")

                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = sender_email
                msg['To'] = recipient_email
                msg.set_content(body)

                with open(cv_path, 'rb') as cv_file:
                    msg.add_attachment(cv_file.read(), maintype='application', subtype='pdf', filename=os.path.basename(cv_path))

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(sender_email, sender_password)
                    smtp.send_message(msg)

                log_result(recipient_email, "Success")
            except Exception as send_err:
                log_result(recipient_email, "Failed", str(send_err))

            progress_bar["value"] = idx
            progress_label.config(text=f"Sending {idx} of {len(recipients)}")
            app.update_idletasks()
            time.sleep(5)

        progress_label.config(text="All emails sent!")
        send_button.config(state="normal")
        preview_button.config(state="normal")
        messagebox.showinfo("Done", "All emails sent. Check 'email_log.txt'.")

    except Exception as e:
        send_button.config(state="normal")
        preview_button.config(state="normal")
        messagebox.showerror("Critical Error", str(e))



def browse_cv(entry_widget):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    entry_widget.delete(0, tk.END)
    entry_widget.insert(0, file_path)

def toggle_input_method():
    manual_frame.pack(pady=5)

# GUI Setup
app = tk.Tk()
app.title("CV Email Sender - By Murtaja")
app.geometry("550x760")

tk.Label(app, text="Your Email:").pack()
email_entry = tk.Entry(app, width=50)
email_entry.pack()

tk.Label(app, text="App Password:").pack()
password_entry = tk.Entry(app, show='*', width=50)
password_entry.pack()

tk.Label(app, text="Email Subject:").pack()
subject_entry = tk.Entry(app, width=50)
subject_entry.pack()

tk.Label(app, text="Email Body:").pack()
body_text = tk.Text(app, height=6, width=50)
body_text.pack()

tk.Label(app, text="Attach Your PDF CV:").pack()
cv_file_path = tk.Entry(app, width=40)
cv_file_path.pack(side=tk.LEFT, padx=5)
tk.Button(app, text="Browse for CV", command=lambda: browse_cv(cv_file_path)).pack(side=tk.LEFT)

# Input method selection
method_var = tk.StringVar(value="excel")




# Manual email input frame
manual_frame = tk.Frame(app)
tk.Label(manual_frame, text="Enter emails (one per line):").pack()
email_text_area = tk.Text(manual_frame, height=6, width=50)
email_text_area.pack()

# Progress bar and label
progress_label = tk.Label(app, text="")
progress_label.pack(pady=(15, 5))
progress_bar = ttk.Progressbar(app, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=5)

# Action Buttons
preview_button = tk.Button(app, text="Preview Emails", command=preview_emails, bg="orange")
preview_button.pack(pady=10)

send_button = tk.Button(app, text="Send Emails", command=send_emails, bg="green", fg="white")
send_button.pack(pady=10)

toggle_input_method()  # Set initial visibility

app.mainloop()
