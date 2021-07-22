import json
import os
import tkinter as tk
from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkinter.font import Font
import sys



class MyApp:
    def __init__(self):
        self.top = tk.Tk()
        self.top.geometry("600x300")
        self.top.configure(background='black')
        self.top.title("IBM Dumps Validation")
        self.canvas = tk.Canvas(self.top, height=300,
                                width=300, bg="black", highlightbackground="black")

        self.canvas.pack(expand=True)


app = MyApp()

style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="orange", background="white")

# Label for the Environment Name
txt_file = Label(app.canvas,
                 text="Environment Name", bg='black', fg='orange', font=Font(weight='bold', size=10)).place(x=40,
                                                                                                            y=30)
# JSON read data to Show in the combobox
file = open(os.path.join(os.sys.path[0], r"C:\Users\DELL\PycharmProjects\demo\server.json"), 'r')
json_data = file.read()

# parse
obj = json.loads(json_data)

server_list = obj['server']
details = []
for i in range(len(server_list)):
    output = server_list[i].get("server_name")
    details.append(output)
# print(details)

# Combobox creation
n = tk.StringVar()
server_taken = ttk.Combobox(
    app.canvas, width=3, textvariable=n, values=details, state='readonly')
server_taken.pack(pady=30, side=tk.TOP)
server_taken.current(0)

# Rows of the JobStream
file_type = Label(app.canvas,
                  text="Job Type", bg='black', fg='orange', font=Font(weight='bold', size=10))
file_type.place(x=40, y=100)

filetype_Options = ttk.Combobox(
    app.canvas, values=['Job', 'JobStream'], state='readonly', width=9)
filetype_Options.pack(padx=190, pady=20, side=tk.TOP)

# Upload The File Function

global lines
global filepath


def Upload_file():
    global filepath
    filepath = filedialog.askopenfile(initialdir="/",
                                      title="Select a File",
                                      filetypes=(("Text files",
                                                  "*.txt"),
                                                 ))
    global lines
    if filepath is not None:  # storing the content in filepath
        lines = [line.rstrip() for line in filepath]

    # print(lines)

    val = server_taken.get() + ".txt"
    filename = os.path.basename(filepath.name)
    # print(filename)

    if val == filename and len(lines) != 0:

        print("File Uploaded Successfully")
        valid_label = Label(app.canvas, text="File upload done", bg='black', fg='orange')
        # valid_label.place(x=30,y=50)
        valid_label.pack()
        # messagebox.showinfo(
        #     title="success", message="File uploaded successfully")
        valid_label.after(4000, valid_label.pack_forget)
    else:
        print("check the file")
        invalid_label = Label(
            app.canvas, text="Check The File", bg='black', fg='orange')

        invalid_label.pack()

        # messagebox.showinfo(
        #     title="Error", message="The File is empty or not correct")
        invalid_label.after(4000, invalid_label.pack_forget)

        # messagebox.showinfo(title="Error", message="The File is empty or not correct")


button_explore = Button(app.canvas,
                        text="Upload",
                        command=Upload_file, width=6,
                        height=0)
button_explore.place(x=150, y=250)
button_explore.pack(side=tk.LEFT, padx=40, pady=2)


# Method to check the file
# def check_file():
#     global lines
#     if 'Hello' in lines:
#         submit_label = Label(
#             app.canvas, text="File is Successfully Submitted", bg='black', fg='orange')
#         submit_label.place(x=40, y=200)
#         submit_label.pack(side=tk.LEFT)
#         submit_label.after(4000, submit_label.pack_forget)
#         messagebox.showinfo(title="Success", message="The file is good to go")
#
#     # elif len(lines) == 0:
#     else:
#         # save_path = "C:\Users\DELL\Desktop\work"
#         outFileName = r"C:\Users\DELL\Desktop\work\log.txt"
#         os.makedirs(os.path.dirname(outFileName), exist_ok=True)
#         now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#         outFile = open(outFileName, "w")
#         outFile.write("Error Logged On" + " " + now)
#         outFile.close()
#
#         is_submit_label = Label(
#             app.canvas, text="File can't be Submitted", bg='black', fg='orange')
#         is_submit_label.place(x=40, y=200)
#         is_submit_label.pack(side=tk.LEFT)
#         is_submit_label.after(4000, is_submit_label.pack_forget)
#         messagebox.showinfo(title="error",
#                             message="Error encountered! log file generated on given path")

# function for running the command
def run():
    global filepath
    # os.system('python sample.py')
    try:
        script_descriptor = open("sample.py")
        a_script = script_descriptor.read()
        sys.argv = [a_script, server_taken.get(), filetype_Options.get(), filepath.name]
        # exec(a_script)
        exec(sys.argv[0] + "" + sys.argv[1] + "" + sys.argv[2] + "" + sys.argv[3])
        messagebox.showinfo(title="sucess", message="executed properly")
        script_descriptor.close()
    except Exception as e:
        messagebox.showinfo(title="Error", message=e)




button_select = tk.Button(app.canvas, text="Submit",
                          width=10,
                          height=1,
                          # compound=tk.RIGHT,
                          command=run,
                          fg="black", bg="#ff1493", font=Font(weight='bold'))
button_select.pack(side=tk.RIGHT, padx=80, pady=30)

app.top.mainloop()
