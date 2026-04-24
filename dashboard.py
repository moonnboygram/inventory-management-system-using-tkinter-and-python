from tkinter import *
import sqlite3
from tkinter import ttk
from tkcalendar import DateEntry

#functionality part
def employee_details():
    emp_details_frame=Frame(root,bg="white")
    emp_details_frame.place(x=0, y=95, width=1300, height=1000)
#heading label or display label
    headinglabel=Label(emp_details_frame, text = "Manage Employee Details", font=("times new roman", 16, "bold"),
                       bg="#0f4d7d")
    headinglabel.place(x=0, y=0, relwidth=1) #x=0, y=0, At the top position
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
                                                       "doj","salary","usertype"),show="headings",
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
    employee_treeview.heading("salary",text= "Salary")
    employee_treeview.heading("usertype",text="User Type")

    #reducing the width of employee columns in the treeview
    employee_treeview.column("empID", width=60)
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
    employee_treeview.column("salary",width=140)
    employee_treeview.column("usertype",width=120)

    detail_frame=Frame(emp_details_frame)
    detail_frame.place(x=110, y=300)

    empid_label=Label(detail_frame, text="Empid", font=("times new roman",12))
    empid_label.grid(row=0,column=0,padx=20, pady=10,sticky="w")
    empid_entry=Entry(detail_frame, font=("times new roman",12),bg="lightyellow")
    empid_entry.grid(row=0,column=1,padx=20,pady=10)

    emp_name_label=Label(detail_frame, text="Name", font=("times new roman",12))
    emp_name_label.grid(row=0,column=2,padx=20,pady=10, sticky="w")
    emp_name_entry =Entry(detail_frame, font=("times new roman",12),bg="lightyellow")
    emp_name_entry.grid(row=0,column=3, padx=20,pady=10)

    emp_email_label=Label(detail_frame, text="Email", font=("times new roman",12))
    emp_email_label.grid(row=0,column=4,padx=20,pady=10, sticky="w")
    emp_email_entry =Entry(detail_frame, font=("times new roman",12),bg="lightyellow")
    emp_email_entry.grid(row=0,column=5, padx=20,pady=10)

    emp_gender= Label(detail_frame, text="Gender", font= ("times new roman", 12))
    emp_gender.grid(row=1,column=0,padx=20,pady=10,sticky="w")
    
    emp_gender_type=ttk.Combobox(detail_frame, values=("Male", "Female"),font=("times new roman",12),width=18,state="readonly")
    emp_gender_type.set("Select Gender")
    emp_gender_type.grid(row=1, column=1)

    dob_label=Label(detail_frame, text="Date Of Birth", font=("times new roman",12))
    dob_label.grid(row=1,column=2,padx=20,pady=10, sticky=W)
    
    #INSTALL CALENDER ON TERMINAL - PIP INSTALL TKCALENDAR
    dob_entry=DateEntry(detail_frame, width=18, font=("times new roman",12),bg="lightyellow",
                        date_pattern="dd/mm/yyyy")
    dob_entry.grid(row=1,column=3, padx=20,pady=10)

    contact_label=Label(detail_frame, text="Contact", font=("times new roman",12))
    contact_label.grid(row=1,column=4,padx=20,pady=10,sticky="w")
    contact_entry =Entry(detail_frame, font=("times new roman",12),bg="lightyellow")
    contact_entry.grid(row=1,column=5, padx=20,pady=10)

    employment_type =Label (detail_frame, text="Employment Type", font =("times new roman", 12))
    employment_type.grid(row=2, column=0, padx=20, pady=10,stick="w")
    
    employment_entry=ttk.Combobox (detail_frame, values= ("Full Time", "Per Time","Contract", 'Intern', 'Casual')
                                   ,font=("times new roman", 12),state="readonly", width=18)
    employment_entry.set("Select Type")
    employment_entry.grid(row=2, column=1)

    education_type =Label(detail_frame,text="Education", font=("times new roman", 12))
    education_type.grid(row=2, column=2, padx=20, pady=10,sticky="w")

    education_type_entry=ttk.Combobox (detail_frame, values= ("PHD","HND","MASTERS","OND","WEAC")
                                       ,font=("times new roman", 12),width=18,state="readonly")
    education_type_entry.set("Select Education")
    education_type_entry.grid(row=2, column=3)

    work_shift = Label(detail_frame, text= "Work Shift", font=("times new roman",12))
    work_shift.grid(row=2,column=4, padx=20,pady=10,sticky=W)
    
    work_shift_entry_combobox=ttk.Combobox(detail_frame, values=("Morning","Afternoon","Night","Full day")
                                  ,font=("times new roman", 12),state="readonly", width=18)
    work_shift_entry_combobox.set('Select Work Shift')
    work_shift_entry_combobox.grid(row=2,column=5)

    emp_address = Label(detail_frame, text="Address",font=("times new roman",12))
    emp_address.grid(row=3, column=0,padx=20,pady=10,sticky=W)
    emp_address_entry =Text(detail_frame, font=("times new roman",12),bg="light yellow", height=3,width=20)
    emp_address_entry.grid(row=3,column=1,rowspan=2)
    
    date_of_joining=Label(detail_frame,text="Date Of Joining", font=("times new roman",12))
    date_of_joining.grid(row=3, column=2,padx=20,pady=10,sticky="w")

    date_of_joining_entry=DateEntry(detail_frame,font=("times new roman",12),date_setting="dd/mm/yyyy",width=18)
    date_of_joining_entry.grid(row=3,column=3)

    salary_label=Label(detail_frame, text="Salary",font=("times new roman",12))
    salary_label.grid(row=3,column=4,padx=20,pady=10,sticky=W)
    salary_label_entry=Entry(detail_frame,font=("times new roman",12),bg="light yellow")
    salary_label_entry.grid(row=3,column=5)

    user_type = Label(detail_frame, text="User Type", font=("times new roman",12))
    user_type.grid(row=4, column=2,padx=20,pady=10,sticky="w")

    user_type_entry=ttk.Combobox(detail_frame, values=("Admin","Employee"),font=
                                 ("times new roman",12),state="readonly",width=18)
    user_type_entry.set("Select User")
    user_type_entry.grid(row=4, column=3)

    password_label = Label(detail_frame, text="Password",font=("times new roman",12))
    password_label.grid(row=4, column=4,padx=20,pady=10,sticky=W)
    password_label_entry =Entry(detail_frame, font=("times new roman",12),bg="light yellow")
    password_label_entry.grid(row=4,column=5)
    
#GUI in python #graphical user interface
root = Tk()
root.title("Dashboard")
root.geometry("1270x668+0+0")
root.resizable(0,0)
root.configure(bg = "white")

background_image = PhotoImage(file = "inventory.png")
title = Label(root, image = background_image, compound = LEFT, text= " Inventory Management System", font = ("times new roman", 40, "bold"), 
              bg = "red", fg = "white")
title.place(x = 0, y = 0, relwidth = 1 )

logoutbutton = Button (root, text = "Logout", font = ("times new roman", 12, "bold"), bg = "white", fg = "black")
logoutbutton.place(x = 1100, y = 25)

employee = Label(root, text = "Welcome Admin\t\tDate: 15-04-2026\t\tTime: 3:12 pm", font =("times new roman", 15),bg = "#010c48", fg = 'white')
employee.place(x = 0, y = 70, relwidth=1)

leftframe = Frame(root)
leftframe.place(x = 0, y = 100, width = 200, height = 490)

checklist_image2 = PhotoImage (file = "checklist.png")
background_image2 = Label (leftframe, image = checklist_image2)
background_image2.pack()

menulabel = Label (leftframe, text = "Menu", font = ("times new roman", 20), bg = "#009688")
menulabel.pack(fill = X)

employees_button = Button (leftframe, text = "Employees", font = ("times new roman", 20, "bold"),
                           anchor = "w", command = employee_details)
employees_button.pack(fill = X) 

supplier_button = Button (leftframe, text = "Suppliers", font = ("times new roman", 20, "bold"), anchor = "w")
supplier_button.pack(fill = X)

category_button = Button (leftframe, text = "Categories", font = ("times new roman", 20, "bold"), anchor = "w")
category_button.pack (fill = X)

items_button = Button (leftframe, text = "Items", font = ("times new roman", 20, "bold"), anchor = "w")
items_button.pack (fill = X)

sales_button = Button (leftframe, text = "Sale", font = ("times new roman", 20, "bold"), anchor = "w")
sales_button.pack(fill = X)

exit_button = Button (leftframe, text = "Exit", font = ("times new roman", 20, "bold"), anchor="w")
exit_button.pack(fill = X)

employee_frame = Frame(root, bg = "#2c3e50", border=3, relief=RIDGE)
employee_frame.place(x = 400, y = 125, width = 280, height = 170)

total_employees = Label(employee_frame, text = "Total Employees", font = ("times new roman", 15, "bold"),
                        bg="#2c3e50",fg = "white")
total_employees.place(x=60, y = 50)

no_of_employees = Label(employee_frame, text = "10", font = ("times new roman", 20, "bold"),
                           bg = "#2c3e50", fg = "white")
no_of_employees.place(x = 120, y = 100)

category_frame = Frame (root, bg="#27ae60", border = 3, relief= RIDGE)
category_frame.place(x = 400, y =300, width = 280, height = 170)

total_category = Label (category_frame, text = "Categories", font = ("times new roman", 15, "bold"),
                        bg = "#27ae60", fg="white")
total_category.place (x = 90, y = 50)

no_of_category = Label (category_frame, text = "10", font = ("times new roman", 20, "bold"),
                           bg="#27ae60", fg="white")
no_of_category.place(x=120, y=100)

supplier_frame = Frame (root, bg="#8e44ad", border=3, relief=RIDGE)
supplier_frame.place(x = 800, y=125, width =280, height=170)

suppliers = Label(supplier_frame, text = "Suppliers", font =("times new Roman",15,"bold"),
                  bg="#8e44ad", fg="white")
suppliers.place(x=90, y=50)

no_of_suppliers = Label(supplier_frame, text = "10", font =("times new Roman",20,"bold"),
                  bg="#8e44ad", fg="white")
no_of_suppliers.place(x=120, y=100)


product_frame = Frame(root, bg = "#2c3e50", border=3, relief=RIDGE)
product_frame.place(x = 800, y = 300, width = 280, height = 170)

total_products = Label(product_frame, text = "Total Products", font = ("times new roman", 15, "bold"),
                        bg="#2c3e50",fg = "white")
total_products.place(x=70, y = 50)

no_of_products = Label(product_frame, text = "10", font = ("times new roman", 20, "bold"),
                           bg = "#2c3e50", fg = "white")
no_of_products.place(x = 120, y = 100)



sales_frame = Frame(root, bg = "red", border=3, relief=RIDGE)
sales_frame.place(x = 600, y = 480, width = 280, height = 170)

sales = Label(sales_frame, text = "Total Sales", font = ("times new roman", 15, "bold"),
                        bg="red",fg = "white")
sales.place(x=90, y = 60)

no_of_sales = Label(sales_frame, text = "10", font = ("times new roman", 20, "bold"),
                           bg = "red", fg = "white")
no_of_sales.place(x = 120, y = 110)



root.mainloop()