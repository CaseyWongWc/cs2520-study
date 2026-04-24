from tkinter import Tk, Label, Button, Entry, StringVar, messagebox

class ProjectWidget:
    def __init__(self, master):
        self.master = master
        master.title("Project Creator")

        self.label = Label(master, text="Enter Project Name:")
        self.label.pack()

        self.project_name = StringVar()
        self.entry = Entry(master, textvariable=self.project_name)
        self.entry.pack()

        self.create_button = Button(master, text="Create Project", command=self.create_project)
        self.create_button.pack()

        self.status_label = Label(master, text="")
        self.status_label.pack()

    def create_project(self):
        project_name = self.project_name.get()
        if project_name:
            # Here you would add the logic to create the project directory and files
            # For example, using the make_dir and make_file functions from your existing code
            self.status_label.config(text=f"Project '{project_name}' created successfully!")
            messagebox.showinfo("Success", f"Project '{project_name}' created successfully!")
        else:
            self.status_label.config(text="Please enter a project name.")
            messagebox.showwarning("Input Error", "Please enter a project name.")

def main():
    root = Tk()
    project_widget = ProjectWidget(root)
    root.mainloop()

if __name__ == "__main__":
    main()