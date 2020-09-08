__author__      = "Rohit kumar"
__copyright__   = "Copyright 2020" "This is only for study purpose dont use it for Diffrent purposes"



from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class student:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="SCHOOL STUDENT MANAGEMENT SYSTEM",bd=8,relief=GROOVE,font=("Yu Gothic UI Semibold",35,"bold"),bg="#F93800",fg="#143D59")
        #fg = forground color (text color)
        title.pack(side=TOP,fill=X)

        #-------------variables------------#
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        #--------variables for search button------------#
        self.search_by=StringVar()
        self.search_txt=StringVar()

        #-------------manage frame left frame ---------------
        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#F93800")
        manage_frame.place(x=20,y=94,width=500,height=600)

        #creating inputs feild for manage frame
        m_title=Label(manage_frame,text="Manage Student",bg="#F93800",fg="#283350",font=("Yu Gothic UI Semibold",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10,padx=40)

        lbl_roll=Label(manage_frame,text="Roll No.",bg="#F93800",fg="#283350",font=("Yu Gothic UI Semibold",17,"bold"))
        lbl_roll.grid(row=1,column=0,padx=10,pady=10,sticky="w")

        txt_roll=Entry(manage_frame,textvariable=self.Roll_No_var,width=23,font=("Yu Gothic UI Semibold",17,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,padx=10,pady=10,sticky="w")

        lbl_name=Label(manage_frame,text="NAME",bg="#F93800",fg="#283350",font=("Yu Gothic UI Semibold",17,"bold"))
        lbl_name.grid(row=2,column=0,padx=10,pady=10,sticky="w")

        txt_name=Entry(manage_frame,textvariable=self.name_var,width=23,font=("Yu Gothic UI Semibold",17,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,padx=10,pady=10,sticky="w")

        lbl_email=Label(manage_frame,text="E-MAIL",bg="#F93800",fg="#283350",font=("Yu Gothic UI Semibold",17,"bold"))
        lbl_email.grid(row=3,column=0,padx=10,pady=10,sticky="w")

        txt_email=Entry(manage_frame,textvariable=self.email_var,width=23,font=("Yu Gothic UI Semibold",17,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,padx=10,pady=10,sticky="w")

        lbl_gender=Label(manage_frame,text="GENDER",bg="#F93800",fg="#283350",font=("Yu Gothic UI Semibold",17,"bold"))
        lbl_gender.grid(row=4,column=0,padx=10,pady=10,sticky="w")

        #txt_gender=Entry(manage_frame,font=("Yu Gothic UI Semibold",20,"bold"),bd=5,relief=GROOVE)
        #txt_gender.grid(row=4,column=1,padx=10,pady=10,sticky="w")
        #chosing combo box
        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var,font=("Yu Gothic UI Semibold",19,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=10,pady=10,sticky="w")

        lbl_contact=Label(manage_frame,text="CONTACT",bg="#F93800",fg="#283350",font=("Yu Gothic UI Semibold",17,"bold"))
        lbl_contact.grid(row=5,column=0,padx=10,pady=10,sticky="w")

        txt_contact=Entry(manage_frame,textvariable=self.contact_var,width=23,font=("Yu Gothic UI Semibold",17,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,padx=10,pady=10,sticky="w")

        lbl_dob=Label(manage_frame,text="D.O.B",bg="#F93800",fg="#283350",font=("Yu Gothic UI Semibold",17,"bold"))
        lbl_dob.grid(row=6,column=0,padx=10,pady=10,sticky="w")

        txt_dob=Entry(manage_frame,textvariable=self.dob_var,width=23,font=("Yu Gothic UI Semibold",17,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,padx=10,pady=10,sticky="w")

        lbl_address=Label(manage_frame,text="ADDRESS",bg="#F93800",fg="#283350",font=("Yu Gothic UI Semibold",17,"bold"))
        lbl_address.grid(row=7,column=0,padx=10,pady=10,sticky="w")

        #txt_address=Entry(manage_frame,font=("Yu Gothic UI Semibold",20,"bold"),bd=5,relief=GROOVE)
        #txt_address.grid(row=7,column=1,padx=10,pady=10,sticky="w")
        self.txt_address=Text(manage_frame,width=28,height=2,font=("",15))
        self.txt_address.grid(row=7,column=1,padx=10,pady=20,sticky="w")

#======BUTTON FRAME=======
        btn_frame=Frame(manage_frame,bd=4,relief=RIDGE,bg="#F93800")
        btn_frame.place(x=7,y=535,width=450)

        addbtn=Button(btn_frame,text="ADD",width=11,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame,text="UPDATE",width=11,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_frame,text="DELETE",width=11,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_frame,text="CLEAR",width=11,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        #-------------detail frame right frame ---------------
        detail_frame=Frame(self.root,bd=5,relief=RIDGE,bg="#F93800")
        detail_frame.place(x=550,y=94,width=780,height=600)

        m_title=Label(detail_frame,text="Student Database",bg="#F93800",fg="#283350",font=("Yu Gothic UI Semibold",25,"bold"))
        m_title.grid(row=0,columnspan=6,pady=10,padx=40)
        
        lbl_search=Label(detail_frame,text="SEARCH BY",bg="#F93800",fg="#283350",width=10,font=("Yu Gothic UI Semibold",17,"bold"))
        lbl_search.grid(row=1,column=0,padx=10,pady=10,sticky="w")

        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=10,font=("Yu Gothic UI Semibold",17,"bold"),state='readonly')
        combo_search['values']=("roll_no","name","contact")
        combo_search.grid(row=1,column=1,padx=0,pady=10,sticky="w")

        txt_search=Entry(detail_frame,textvariable=self.search_txt,width=15,font=("Yu Gothic UI Semibold",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=1,column=2,padx=10,pady=10,sticky="w")
        
        searchbtn=Button(detail_frame,text="SEARCH",width=14,height=2,command=self.search_data).grid(row=1,column=3,padx=10,pady=10)
        showbtn=Button(detail_frame,text="SHOW",width=14,height=2,command=self.fetch_data).grid(row=1,column=4,padx=10,pady=10)

        #----------------Table frame-------------------#
        
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="#F93800")
        table_frame.place(x=10,y=130,width=750,height=445)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("roll",text="Roll No.")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("contact",text="Contact")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("roll",width=50)
        self.student_table.column("name",width=100)
        self.student_table.column("email",width=150)
        self.student_table.column("gender",width=70)
        self.student_table.column("contact",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("address",width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        self.fetch_data()
        #student_table.pack()

    def add_student(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.contact_var.get()=="" or self.gender_var.get()=="" or self.dob_var.get()=="" or self.email_var.get()=="":
                messagebox.showerror("Error","All fields are required!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",
                                                    (self.Roll_No_var.get(),
                                                    self.name_var.get(),
                                                    self.email_var.get(),
                                                    self.gender_var.get(),
                                                    self.contact_var.get(),
                                                    self.dob_var.get(),
                                                    self.txt_address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted sucessfully..")
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("",END,values=row)
            con.commit()
        con.close()      
    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        curosor_row=self.student_table.focus()
        contents=self.student_table.item(curosor_row)
        row=contents['values']
        #print(row)
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])


    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                self.name_var.get(),
                                                                                                self.email_var.get(),
                                                                                                self.gender_var.get(),
                                                                                                self.contact_var.get(),
                                                                                                self.dob_var.get(),
                                                                                                self.txt_address.get('1.0',END),
                                                                                                self.Roll_No_var.get()
                                                                                                ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()      

root = Tk()
ob = student(root)
root.mainloop()