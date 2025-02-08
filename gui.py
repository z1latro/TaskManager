import tkinter as tk
from tkinter import messagebox, simpledialog

class Task:
    def __init__(self,name,priority,status=False):
        self.name = name
        self.priority = priority
        self.status = status
    def __str__(self):
        return f"{self.name} | {self.priority} | {'Completed' if self.status else 'Not Completed'}"
class taskManagerGUI:
    def __init__(self, root):
        self.task_list = []
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x400")  # Fixed size for the main window
        self.root.resizable(False, False)  # Prevent resizing

        # Widgets
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.priority_var = tk.StringVar(value="Select Priority")
        self.priority_menu = tk.OptionMenu(root, self.priority_var, "          High      ", "        Medium    ", "         Low      ")
        self.priority_menu.grid(row=0, column=1, padx=10, pady=10)
        
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

        self.edit_button = tk.Button(root, text="Edit Task", command=self.edit_task)
        self.edit_button.grid(row=2, column=1, padx=10, pady=10)

        self.view_button = tk.Button(root, text="Flip Task Status", command=self.flip_tasks)
        self.view_button.grid(row=2, column=2, padx=10, pady=10)

    def add_task(self):
        name = self.task_entry.get().strip()
        priority = self.priority_var.get()

        if not name or priority == 'Select Priority':
            messagebox.showerror("Error", "Please enter a task name and select a priority")
            return
        task = Task(name,priority)
        self.task_list.append(task)
        self.task_listbox.insert(tk.END,str(task))
        self.task_entry.delete(0, tk.END)
        self.priority_var.set("Select Priority")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error","Please select a task to delete.")
            return
        self.task_list.pop(selected_index[0])
        self.task_listbox.delete(selected_index)
    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error","Please select a task to edit.")
            return
        task_to_edit = self.task_list[selected_index[0]]
        new_name = simpledialog.askstring("Edit Task", "Enter new task name:", initialvalue=task_to_edit.name)
        new_priority = simpledialog.askstring("Edit Task", "Enter new priority [High, Medium, Low]:", initialvalue=task_to_edit.priority)

        if new_name and new_priority in {"High", "Medium", "Low"}:
            task_to_edit.name = new_name
            task_to_edit.priority = new_priority
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index,str(task_to_edit))
        else:
            messagebox.showerror("Error", "Invalid input. Please try again.")
    def flip_tasks(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error","Please select a task to update.")
            return
        task_to_edit = self.task_list[selected_index[0]]
        task_to_edit.status = not task_to_edit.status
        self.task_listbox.delete(selected_index)
        self.task_listbox.insert(selected_index,str(task_to_edit))

if __name__ == '__main__':
    root = tk.Tk()
    app = taskManagerGUI(root)
    root.mainloop()