from tkinter import *
from employees import employee_details


 
#GUI in python #graphical user interface

root = Tk()
root.title("Dashboard")
root.geometry("1270x668+0+0")
# root.resizable(0,0)
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
                           anchor = "w", command = lambda: employee_details(root))
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