import tkinter as tk

# Creating root window
root = tk.Tk()
root.title("TODO List")

# Entry widget for adding tasks
task_entry = tk.Entry(root, width=35)
task_entry.grid(row=0, column=0)

# Button for adding tasks
add_button = tk.Button(root, text="Add Task", width=15)
add_button.grid(row=0, column=1)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=1, column=0, columnspan=2)

# Button for deleting selected tasks
delete_button = tk.Button(root, text="Delete Task", width=15)
delete_button.grid(row=2, column=0, columnspan=2)


# Function to add tasks to the listbox
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)


# Function to delete selected task
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except IndexError:
        pass


# Add functionality to buttons
add_button.config(command=add_task)
delete_button.config(command=delete_task)

# Start the main event loop of app
root.mainloop()
