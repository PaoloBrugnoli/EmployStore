# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from tkinter import messagebox

from capgemini.store.resourses.sql import *
from capgemini.store.utility.replace import MakeQuery
from capgemini.store.emploee.daoEmployee import DaoEmpDetails

# connessione
host = "127.0.0.1"
user = "root"
passwd = "MySQL"
database = "employee"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def add_data(d_data):
    # Refresh show_data
    show_data.delete(0,show_data.size())
    for key, value in d_data.items():
        s_row = "[ID:"+str(key)+"] [(NAME;DEPT):("+value+")]"
        show_data.insert(show_data.size()+1, s_row)

# Call actions
def insert_action(s_id,s_name,s_dept):
    # Insert data into db
    if (s_id=='' or s_name=='' or s_dept==''):
        messagebox.showwarning('Cannot Insert', 'All the fields are required !')
    else:
        # Call daoEmployee - insert_data
        print("Call daoEmployee - insert_data")
        dao_employee = DaoEmpDetails(host, user, passwd, database)
        b_success, s_msg = dao_employee.insert_data(s_id, s_name, s_dept)
        if b_success:
            messagebox.showinfo('Ok Insert', s_msg)
        else:
            messagebox.showerror('Cannot Insert', s_msg)
    reset_action()

def update_action(s_id,s_name,s_dept):
    # Update data into db
    if (s_id=='' or s_name=='' or s_dept==''):
        messagebox.showwarning('Cannot Update', 'All the fields are required !')
    else:
        # Call daoEmployee - update_data
        print("Call daoEmployee - update_data")
        dao_employee = DaoEmpDetails(host, user, passwd, database)
        b_success, s_msg = dao_employee.update_data(s_id, s_name, s_dept)
        if b_success:
            messagebox.showinfo('Ok Update', s_msg)
        else:
            messagebox.showerror('Cannot Update', s_msg)
    reset_action()

def fetch_action(s_id):
    # Update data into db
    if (s_id==''):
        messagebox.showwarning('Cannot fetch info', 'Id is required !')
    else:
        # Call daoEmployee - fetch_data
        print("Call daoEmployee - fetch_data")
        dao_employee = DaoEmpDetails(host, user, passwd, database)
        b_success, s_msg, d_data = dao_employee.get_data(s_id)
        if b_success:
            num_items = len(d_data.items())
            print(f"Number of items {num_items}")
            if not(num_items==0):
                for key, value in d_data.items():
                    s_msg += "\n" + f"[ID:{key}][(NAME;DEPT):({value})]"
                messagebox.showinfo('Ok Fetch', s_msg)
            else:
                s_msg = "No Information present !"
                messagebox.showwarning('No Fetch', s_msg)
        else:
            messagebox.showerror('Cannot Fetch', s_msg)

def delete_action(s_id):
    # Delete data into db
    if (s_id==''):
        messagebox.showwarning('Cannot delete', 'Id is required !')
    else:
        # Call daoEmployee - delete_data
        print("Call daoEmployee - delete_data")
        dao_employee = DaoEmpDetails(host, user, passwd, database)
        b_success, s_msg = dao_employee.delete_data(s_id)
        if b_success:
            messagebox.showinfo('Ok deleted', s_msg)
        else:
            messagebox.showerror('Cannot delete', s_msg)

def show_action():
    # Show all data into db
    # Call daoEmployee - show_data
    print("Call daoEmployee - show_data")
    dao_employee = DaoEmpDetails(host, user, passwd, database)
    b_success, s_msg, d_data = dao_employee.show_data()
    if b_success:
        num_items = len(d_data.items())
        print(f"Number of items {num_items}")
        if not(num_items==0):
            add_data(d_data)
            for key, value in d_data.items():
                s_msg += "\n" + f"[ID:{key}][(NAME;DEPT):({value})]"
            messagebox.showinfo('Ok Show', s_msg)
        else:
            s_msg = "No Information present !"
            messagebox.showwarning('No Show', s_msg)
    else:
        messagebox.showerror('Cannot Show', s_msg)

def reset_action():
    enter_id.delete(0,"end")
    enter_name.delete(0, "end")
    enter_dept.delete(0, "end")

# Create an event handler
def button_click(item):
    # Manage the action 's button
    # Read text
    s_id = enter_id.get()
    print(f"id :{s_id}")
    s_name = enter_name.get()
    print(f"name :{s_name}")
    s_dept = enter_dept.get()
    print(f"dept :{s_dept}")
    print(item)
    if item == 'insert':
        # Call insert action
        insert_action(s_id,s_name,s_dept)
    elif item == 'update':
        # Call update action
        update_action(s_id, s_name, s_dept)
    elif item == 'delete':
        # Call delete action
        delete_action(s_id)
    elif item == 'fetch':
        # Call fetch action
        fetch_action(s_id)
    elif item == 'show':
        # Call show action
        show_action()
    elif item == 'reset':
        # Call reset action
        reset_action()
    else:
        print("no action !")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Create a window object
    window = Tk()
    window.attributes('-alpha', 0.0)
    window.geometry("675x270")
    window.title("Employee CRUD App")

    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    window.config(menu=menubar)

    center(window)

    # All labels
    emp_Id = Label(window, text="Employee ID", font=("Serif", 10))
    emp_Id.place(x=20, y=30)
    emp_Name = Label(window, text="Employee Name", font=("Serif", 10))
    emp_Name.place(x=20, y=60)
    emp_Dept = Label(window, text="Employee Dept", font=("Serif", 10))
    emp_Dept.place(x=20, y=90)

    # All Entry Boxes respective to Labels
    enter_id = Entry(window)
    enter_id.place(x=150, y=30)
    enter_name = Entry(window)
    enter_name.place(x=150, y=60)
    enter_dept = Entry(window)
    enter_dept.place(x=150, y=90)

    # List
    show_data = Listbox(window, width=60)
    show_data.place(x=300, y=30)

    # All Buttons
    insert_btn = Button(window, text="Insert", font=("Sans", 10), bg="white", command=lambda:button_click("insert"), width=10)
    insert_btn.place(x=50, y=220)
    update_btn = Button(window, text="Update", font=("Sans", 10), bg="white", command=lambda:button_click("update"), width=10)
    update_btn.place(x=150, y=220)
    fetch_btn = Button(window, text="Fetch", font=("Sans", 10), bg="white", command=lambda:button_click("fetch"), width=10)
    fetch_btn.place(x=250, y=220)
    show_btn = Button(window, text="Show", font=("Sans", 10), bg="white", command=lambda:button_click("show"), width=10)
    show_btn.place(x=350, y=220)
    delete_btn = Button(window, text="Delete", font=("Sans", 10), bg="white", command=lambda:button_click("delete"), width=10)
    delete_btn.place(x=450, y=220)
    reset_btn = Button(window, text="Reset", font=("Sans", 10), bg="white", command=lambda:button_click("reset"), width=10)
    reset_btn.place(x=550, y=220)


    window.attributes('-alpha', 1.0)
    window.mainloop()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
