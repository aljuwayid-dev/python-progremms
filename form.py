#name: Abdulkarim Aljuwayid

#Program 1:

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os


class InternshipForm:
    def __init__(self, master):
        self.filename = None
        self.heading = None
        self.master = master
        self.master.title("Internship Form")
        self.master.geometry("900x600")
        self.master.configure(bg="lightblue")

        self.file_name = StringVar()
        self.full_name = StringVar()
        self.id = StringVar()
        self.phone_number = StringVar()
        self.gpa = StringVar()
        self.dept = StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.heading = Label(self.master, text="Internship Form", font=("arial", 30, "bold"), bg="lightblue")
        self.heading.grid(row=0, column=0, columnspan=2, pady=20)

        self.full_name_label = Label(self.master, text="Full Name:", font=("arial", 20, "bold"), bg="lightblue")
        self.full_name_label.grid(row=1, column=0, padx=20, pady=10)
        self.full_name_entry = Entry(self.master, textvariable=self.full_name, font=("arial", 20, "bold"), bg="lightblue")
        self.full_name_entry.grid(row=1, column=1, padx=20, pady=10)

        self.id_label = Label(self.master, text="ID:", font=("arial", 20, "bold"), bg="lightblue")
        self.id_label.grid(row=2, column=0, padx=20, pady=10)
        self.id_entry = Entry(self.master, textvariable=self.id, font=("arial", 20, "bold"), bg="lightblue")
        self.id_entry.grid(row=2, column=1, padx=20, pady=10)

        self.phone_number_label = Label(self.master, text="Phone Number:", font=("arial", 20, "bold"), bg="lightblue")
        self.phone_number_label.grid(row=3, column=0, padx=20, pady=10)
        self.phone_number_entry = Entry(self.master, textvariable=self.phone_number, font=("arial", 20, "bold"), bg="lightblue")
        self.phone_number_entry.grid(row=3, column=1, padx=20, pady=10)

        self.gpa_label = Label(self.master, text="GPA:", font=("arial", 20, "bold"), bg="lightblue")
        self.gpa_label.grid(row=4, column=0, padx=20, pady=10)
        self.gpa_entry = Entry(self.master, textvariable=self.gpa, font=("arial", 20, "bold"), bg="lightblue")
        self.gpa_entry.grid(row=4, column=1, padx=20, pady=10)

        self.dept_label = Label(self.master, text="Department:", font=("arial", 20, "bold"), bg="lightblue")
        self.dept_label.grid(row=5, column=0, padx=20, pady=10)
        self.dept_radio = Radiobutton(self.master, text="IS", variable=self.dept, value="IS", font=("arial", 16, "bold"), bg="lightblue")
        self.dept_radio.grid(row=5, column=1, padx=20, pady=10)
        self.dept_radio = Radiobutton(self.master, text="CS", variable=self.dept, value="CS", font=("arial", 16, "bold"), bg="lightblue")
        self.dept_radio.grid(row=5, column=2, padx=20, pady=10)
        self.dept_radio = Radiobutton(self.master, text="SE", variable=self.dept, value="SE", font=("arial", 16, "bold"), bg="lightblue")
        self.dept_radio.grid(row=5, column=3, padx=20, pady=10)

        self.filename_label = Label(self.master, text="File to be saved:", font=("arial", 20, "bold"), bg="lightblue")
        self.filename_label.grid(row=6, column=0, padx=20, pady=10)
        self.filename_entry = Entry(self.master, textvariable=self.file_name, font=("arial", 20, "bold"), bg="lightblue")
        self.filename_entry.grid(row=6, column=1, padx=20, pady=10)

        self.open_button = Button(self.master, text="Open", font=("arial", 20, "bold"), bg="lightblue", command=self.open_file)
        self.open_button.grid(row=6, column=2, padx=20, pady=10)

        self.submit_button = Button(self.master, text="Submit", font=("arial", 20, "bold"), bg="lightblue", command=self.submit_info)
        self.submit_button.grid(row=7, column=1, padx=20, pady=10)


        self.close_button = Button(self.master, text="Close", font=("arial", 20, "bold"), bg="lightblue", command=self.master.destroy)
        self.close_button.grid(row=7, column=2, padx=20, pady=10)

    def open_file(self):
        self.file = filedialog.askopenfile(parent=self.master, mode='rb', title='Choose a file')
        if self.file != None:
            contents = self.file.read()
            self.file.close()
            self.full_name.set(contents)
        self.file_name.set(self.file.name)

    def submit_info(self):

        if self.filename == "":
            messagebox.showerror("Error", "Please select a file")

        else:
            with open(self.filename, "a") as file:

                if self.full_name.get() == "":
                    messagebox.showinfo("Error", "Please enter your full name")
                    return
                elif type(self.full_name.get()) != str:
                    messagebox.showerror("Error", "Please enter your full name")
                    return
                else:
                    file.write("Full Name : " + self.full_name.get() + "")

                if self.id.get() == "":
                    messagebox.showinfo("Error", "Please enter your ID")
                    return
                elif len(self.id.get()) == 10:
                    file.write("ID : " + self.id.get() + "")
                else:
                    messagebox.showerror("Error", "Valid ID must be 10 digits")
                    return

                if self.phone_number.get() == "":
                    messagebox.showinfo("Error", "Please enter your phone number")
                    return
                if len(self.phone_number.get()) == 10:
                    file.write("Phone Number : " + self.phone_number.get() + "")
                else:
                    messagebox.showerror("Error", "Phone number must be 10 digits")
                    return

                if self.gpa.get() == "":
                    messagebox.showinfo("Error", "Please enter your GPA")
                    return
                elif 0 <= float(self.gpa.get()) <= 5:
                    file.write("GPA : " + self.gpa.get() + "")
                else:
                    messagebox.showerror("Error", "GPA must be between 0 and 5")
                    return

                if self.dept.get() == "":
                    messagebox.showinfo("Error", "Please select your department")
                    return
                else:
                    file.write("Department : "+self.dept.get() + "")

                messagebox.showinfo("Success", "Information saved successfully")
                self.clear_fields()

    def open_file(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
        print(self.filename)

    def clear_fields(self):
        self.full_name.set("")
        self.id.set("")
        self.phone_number.set("")
        self.gpa.set("")
        self.dept.set("")


def main():
     root = Tk()
     app = InternshipForm(root)
     root.mainloop()
     root.destroy()



if __name__ == '__main__':
    main()

# Program 2:
class myimges():
    def __init__(self, master):
        self.filename = None
        self.heading = None
        self.master = master
        self.master.title("myimges")
        self.master.geometry("900x600")
        self.master.configure(bg="lightblue")
        self.create_widgets2()
        self.root = tkinter.Tk()
        self.root.geometry("800x800")
        self.canvas = tkinter.Canvas(self.root, width=200, heigh=200, bg="white")
        self.img = tkinter.PhotoImage(file=self.imgFile)
        self.canvas.create_image(100, 100, anchor=tkinter.NW, image=self.img)
        self.canvas.pack(fill="both", expand="yes", pady="30", padx="30")
        self.button = tkinter.Button(self.root, text='Switch', command=self.action, foreground='Green', font=
        ('Arial', 20, 'bold', 'underline'))
        self.button.pack(pady="30")
        tkinter.mainloop()
        self.img = tkinter.PhotoImage(file=self.imgFile)
        self.canvas.create_image(512, 512, anchor=tkinter.NW, image=self.img)

def create_widgets2(self):
    self.heading = Label(self.master, text="Internship Form", font=("arial", 30, "bold"), bg="lightblue")
    self.heading.grid(row=0, column=0, columnspan=2, pady=20)
    self.filename_label = Label(self.master, text="File to be saved:", font=("arial", 20, "bold"), bg="lightblue")
    self.filename_label.grid(row=6, column=0, padx=20, pady=10)
    self.filename_entry = Entry(self.master, textvariable=self.file_name, font=("arial", 20, "bold"), bg="lightblue")
    self.filename_entry.grid(row=6, column=1, padx=20, pady=10)

def open_file2(self):
    self.file = filedialog.askopenfile(parent=self.master, mode='rb', title='Choose a file')
    if self.file != None:
        contents = self.file.read()
        self.file.close()
        self.full_name.set(contents)
        self.file_name.set(self.file.name)
def main():
    root = Tk()
    app = myimges(root)
    root.mainloop()
    root.destroy()
