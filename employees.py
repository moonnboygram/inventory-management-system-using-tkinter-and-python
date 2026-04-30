from tkinter import *
# import sqlite3
from tkinter import ttk
from tkcalendar import DateEntry
import pymysql
from tkinter import messagebox as msg

def connect_database():
   try:
       connection=pymysql.connect(host="localhost", user="root", password="samwell20")
       cursor = connection.cursor()

   except:
          msg.showerror("Error", "Database connectivitity issue try again, open mysql command prompt" )
          return
   cursor.execute("CREATE DATABASE IF NOT EXISTS inventory_system")
   cursor.execute("USE inventory_system")
   cursor.execute("CREATE TABLE IF NOT EXISTS employee_data (empID INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), " \
                                                 "gender VARCHAR(50), dob VARCHAR(50),contact VARCHAR(50), employment_type VARCHAR(50)," \
                                                 "education VARCHAR(100), work_shift VARCHAR(50), address VARCHAR(100)," \
                                                 "doj VARCHAR (50), salary VARCHAR(50),password VARCHAR(50))")
   connect_database()




#functionality part
def employee_details(root):
    emp_details_frame=Frame(root,bg="white")
    emp_details_frame.place(x=0, y=95, width=1370, height=1000)
#heading label or display label
    headinglabel=Label(emp_details_frame, text = "Manage Employee Details", font=("times new roman", 16, "bold"),
                       bg="#0f4d7d")
    headinglabel.place(x=0, y=0,relwidth=1) #x=0, y=0, At the top position
#backbutton creation
    back_btn=Button(emp_details_frame, text = "Back",font = ("times new roman",12, "bold"),cursor="hand2"
                    ,command=lambda: emp_details_frame.place_forget()) #lamda:emp_details_frame.place_forget() lambda is a small function that  execute the back button
    back_btn.place(x=0, y=30)

    topframe = Frame (emp_details_frame, bg="white")
    topframe.place(x=0, y=65, relwidth=1, height=235)
    search_frame = Frame(topframe, bg="white")
    search_frame.pack()
    search_combobox= ttk.Combobox(search_frame, values =("Id","Name","Email"), font = ("times new roman", 12), state="readonly") 
                                    #state="readonly" does not allow typing inside the frame or entry box )
    search_combobox.grid(row = 0, column= 0, padx=20) #grid method helps us arrange the frame or input box side by side
    search_combobox.set("Search") #this function assigns the write up "Search" to the frame or entry box
    
    search_entry = Entry(search_frame, font= ("times new roman", 12),bg = "lightyellow")
    search_entry.grid(row=0, column=1) #we use column one because we want the input field to go to the next side afrter the search

    search_btn=Button (search_frame, text= "Search", font= ("times new roman", 12),width=10, cursor="hand2",
                       fg ="white", bg="#0f4d7d")
    search_btn.grid(row=0, column=2, padx=10)

    show_button = Button (search_frame, text ="Show All", font = ("times new roman", 12),width = 10, 
                          cursor="hand2", bg="#0f4d7d", fg="white")
    show_button.grid(row=0, column=3,)

#scrollbar. creating this horizontal and vertical scrollbar with the help of the scrollbar class.....scrollbar()
    horizontal_scrollbar=Scrollbar(topframe,orient=HORIZONTAL,cursor="hand2")
    vertical_scrollbar=Scrollbar(topframe,orient=VERTICAL)
    employee_treeview= ttk.Treeview(topframe,columns=("empID","name","email","gender","dob","contact",
                                                       "employment_type","education","work_shift","address",
                                                       "doj","salary","usertype","password"),show="headings",
                                        xscrollcommand=horizontal_scrollbar.set, yscrollcommand=vertical_scrollbar.set)#show="headings" hides the 4th extra column
    #x and y scroll command helps us execute and place the scrollbar in their appropriate place
    #then we also need to place it manually using the pack()
    horizontal_scrollbar.pack(side=BOTTOM, fill=X)
    vertical_scrollbar.pack(side=RIGHT,fill=Y)#pady=(10,0)if there is too much spacing on the right scrollbar
    horizontal_scrollbar.config(command=employee_treeview.xview)
    vertical_scrollbar.config(command=employee_treeview.yview)
    employee_treeview.pack(pady=(10,0))

    #code to see the headings
    employee_treeview.heading("empID",text="empID")
    employee_treeview.heading("name",text= "Name")
    employee_treeview.heading("email",text="Email")
    employee_treeview.heading("gender",text="Gender")
    employee_treeview.heading("dob",text= "Date Of Birth")
    employee_treeview.heading("contact",text="Contact")
    employee_treeview.heading("employment_type",text="Employment Type")
    employee_treeview.heading("education",text="Education")
    employee_treeview.heading("work_shift",text= "Work Shift")
    employee_treeview.heading("address",text="Address")
    employee_treeview.heading("doj",text="Date Of Joining")
    employee_treeview.heading("salary",text="Salary")
    employee_treeview.heading("usertype",text="Usertype")
    employee_treeview.heading("password",text="Password")

    #reducing the width of employee columns in the treeview
    employee_treeview.column("empID",width=60)
    employee_treeview.column("name",width=140)
    employee_treeview.column("email",width=180)
    employee_treeview.column("gender",width=80)
    employee_treeview.column("dob",width=100)
    employee_treeview.column("contact",width=100)
    employee_treeview.column("employment_type",width=120)
    employee_treeview.column("education",width=120)
    employee_treeview.column("work_shift",width=100)
    employee_treeview.column("address",width=200)
    employee_treeview.column("doj",width=100) 
    employee_treeview.column("salary",width=120)
    employee_treeview.column("usertype",width=120)
    employee_treeview.column("password",width=120)

    detail_frame=Frame(emp_details_frame,bg=("white"))
    detail_frame.place(x=110, y=300)

    empid_label=Label(detail_frame, text="ID", font=("times new roman",12),bg="white")
    empid_label.grid(row=0,column=0,padx=20, pady=10,sticky="w")
    empid_entry=Entry(detail_frame, font=("times new roman",12),bg="lightyellow")
    empid_entry.grid(row=0,column=1,padx=20,pady=10)

    emp_name_label=Label(detail_frame, text="Name", font=("times new roman",12),bg="white")
    emp_name_label.grid(row=0,column=2,padx=20,pady=10, sticky="w")
    emp_name_entry =Entry(detail_frame, font=("times new roman",12),bg="lightyellow")
    emp_name_entry.grid(row=0,column=3, padx=20,pady=10)

    emp_email_label=Label(detail_frame, text="Email", font=("times new roman",12),bg="white")
    emp_email_label.grid(row=0,column=4,padx=20,pady=10, sticky="w")
    emp_email_entry =Entry(detail_frame, font=("times new roman",12),bg="lightyellow")
    emp_email_entry.grid(row=0,column=5, padx=20,pady=10)

    emp_gender= Label(detail_frame, text="Gender", font= ("times new roman", 12),bg="white")
    emp_gender.grid(row=1,column=0,padx=20,pady=10,sticky="w")
    
    emp_gender_type=ttk.Combobox(detail_frame, values=("Male", "Female"),font=("times new roman",12),width=18,state="readonly")
    emp_gender_type.set("Select Gender")
    emp_gender_type.grid(row=1, column=1)

    dob_label=Label(detail_frame, text="Date Of Birth", font=("times new roman",12),bg="white")
    dob_label.grid(row=1,column=2,padx=20,pady=10, sticky=W)
    
    #INSTALL CALENDER ON TERMINAL - PIP INSTALL TKCALENDAR
    dob_entry=DateEntry(detail_frame, width=18, font=("times new roman",12),bg="lightyellow",
                        date_pattern="dd/mm/yyyy")
    dob_entry.grid(row=1,column=3, padx=20,pady=10)

    contact_label=Label(detail_frame, text="Contact", font=("times new roman",12),bg="white")
    contact_label.grid(row=1,column=4,padx=20,pady=10,sticky="w")
    contact_entry =Entry(detail_frame, font=("times new roman",12),bg="lightyellow")
    contact_entry.grid(row=1,column=5, padx=20,pady=10)

    employment_type =Label (detail_frame, text="Employment Type", font =("times new roman", 12),bg="white")
    employment_type.grid(row=2, column=0, padx=20, pady=10,stick="w")
    
    employment_entry=ttk.Combobox (detail_frame, values= ("Full Time", "Per Time","Contract", 'Intern', 'Casual')
                                   ,font=("times new roman", 12),state="readonly", width=18)
    employment_entry.set("Select Type")
    employment_entry.grid(row=2, column=1)

    education_type =Label(detail_frame,text="Education", font=("times new roman", 12),bg="white")
    education_type.grid(row=2, column=2, padx=20, pady=10,sticky="w")

    education_type_entry=ttk.Combobox (detail_frame, values= ("PHD","HND","MASTERS","OND","WEAC")
                                       ,font=("times new roman", 12),width=18,state="readonly")
    education_type_entry.set("Select Education")
    education_type_entry.grid(row=2, column=3)

    work_shift = Label(detail_frame, text= "Work Shift", font=("times new roman",12),bg="white")
    work_shift.grid(row=2,column=4, padx=20,pady=10,sticky=W)
    
    work_shift_entry_combobox=ttk.Combobox(detail_frame, values=("Morning","Afternoon","Night","Full day")
                                  ,font=("times new roman", 12),state="readonly", width=18)
    work_shift_entry_combobox.set('Select Work Shift')
    work_shift_entry_combobox.grid(row=2,column=5)

    emp_address = Label(detail_frame, text="Address",font=("times new roman",12),bg="white")
    emp_address.grid(row=3, column=0,padx=20,pady=10,sticky=W)
    emp_address_entry =Text(detail_frame, font=("times new roman",12),bg="light yellow", height=3,width=20)
    emp_address_entry.grid(row=3,column=1,rowspan=2)
    
    date_of_joining=Label(detail_frame,text="Date Of Joining", font=("times new roman",12),bg="white")
    date_of_joining.grid(row=3, column=2,padx=20,pady=10,sticky="w")

    date_of_joining_entry=DateEntry(detail_frame,font=("times new roman",12),date_setting="dd/mm/yyyy",width=18)
    date_of_joining_entry.grid(row=3,column=3)

    salary_label=Label(detail_frame, text="Salary",font=("times new roman",12),bg="white")
    salary_label.grid(row=3,column=4,padx=20,pady=10,sticky=W)
    salary_label_entry=Entry(detail_frame,font=("times new roman",12),bg="light yellow")
    salary_label_entry.grid(row=3,column=5)

    user_type = Label(detail_frame, text="User Type", font=("times new roman",12),bg="white")
    user_type.grid(row=4, column=2,padx=20,pady=10,sticky="w")

    user_type_entry=ttk.Combobox(detail_frame, values=("Admin","Employee"),font=
                                 ("times new roman",12),state="readonly",width=18)
    user_type_entry.set("Select User")
    user_type_entry.grid(row=4, column=3)

    password_label = Label(detail_frame, text="Password",font=("times new roman",12),bg="white")
    password_label.grid(row=4, column=4,padx=20,pady=10,sticky=W)
    password_label_entry =Entry(detail_frame, font=("times new roman",12),bg="light yellow")
    password_label_entry.grid(row=4,column=5)
    
    button_frame = Frame(emp_details_frame,bg="white")
    button_frame.place(x=200, y=520) 

    add_button =Button (button_frame,text= "Add", font=("times new roman",12),bg="blue",fg="white",width=10)
    add_button.grid(row=0, column=0, padx= 70, pady=20)

    update_button =Button (button_frame,text= "Update", font=("times new roman",12),bg="blue",fg="white",width=10)
    update_button.grid(row=0, column=1, padx=70, pady=20)

    delete_button =Button (button_frame,text= "Delete", font=("times new roman",12),bg="blue",fg="white",width=10)
    delete_button.grid(row=0, column=2, padx=70, pady=20)

    clear_button =Button (button_frame,text= "Clear", font=("times new roman",12),bg="blue",fg="white",width=10)
    clear_button.grid(row=0, column=3,padx=70, pady=20)

#INSTALL SQL - pip install pymysql