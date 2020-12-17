#Simple login system in python with a GUI built from tkinter
# 
#           18/12/2020


from tkinter import *          #pip install tkinter
from tkinter import messagebox # Must be for messagebox 
from PIL import *              #pip install pillow



class Login_Sys:
    def __init__(self,root):    
        self.root = root
        self.root.title("Test Window") # Window Title
        self.root.geometry("1120x620") # Window Geometry
        self.root.configure(bg= b_color) # Window Background
    
        self.user_icon = PhotoImage(file="C:/Users/..../..../..../..../xxxx.png") 
        self.password_icon = PhotoImage(file="C:/Users/..../..../..../..../xxxx.png") #or .jpg or.jpeg or .png



# --------------------Login Button Fonction-------------------------------------------------------------------------------------------------------------------------------    

        def login():

            if self.uname.get()=="" or self.pass_.get()=="":
                messagebox.showinfo(title="Error", message="All fields are requried!!")
            
            elif self.uname.get()=="aaaa" and self.pass_.get()=="aaaa":
                messagebox.showinfo(title="Successfull", message="Welcome"+ f" {self.uname.get()}")
            
            else:
                messagebox.showerror(title="Error",message= "Invalid Username or Password ")    



# ----------------------Title Labels----------------------------------------------------------------------------------------------------------------------------          

        title= Label(self.root, text="Login", font=("times new roman", 20, "bold"), bg=(b_color), fg="#e5e5e5", bd=5, relief=FLAT) # In window Main Title
        title.place(x=0, y=0, relwidth=1) # In window Main Title Pleace



# --------------------Login Frame Labels-------------------------------------------------------------------------------------------------------------------------------

        Login_Frame= Frame(self.root)
        Login_Frame.configure(bg=b_color, bd=5)
        Login_Frame.place(x=400, y=150)        
        
        lbluser = Label(Login_Frame, text="Username",image=self.user_icon, compound=LEFT, font=("calibri", 10, "bold"), bg=(b_color), fg="#e5e5e5", bd=5, relief=FLAT).grid(row=1, column=0, pady=10) # User İcon
        self.uname = StringVar() # Take user entry and change to string
        txtuser = Entry(Login_Frame,bd=5, textvar=self.uname, relief=FLAT, font=("",15), bg= (color2)).grid(row=1, column=1, padx=10) # User Entry 

        
        lblpass = Label(Login_Frame, text="Password",image=self.password_icon, compound=LEFT, font=("calibri", 10, "bold"), bg=(b_color), fg="#e5e5e5", bd=5, relief=FLAT).grid(row=2, column=0, pady=10) # Password İcon
        self.pass_ = StringVar() # Take Password entry and change to string
        txtpass = Entry(Login_Frame,bd=5, textvar=self.pass_, show="*", relief=FLAT, font=("",15), bg= (color2)).grid(row=2, column=1, padx=10) # Password Entry --- show="*" is hide the entry 

        Btn_log  = Button(Login_Frame, text="Login", command=login, width=8,  font=("calibri",10,"bold"), bg=(color2), fg= "black", bd=0, relief=FLAT,).grid(row=3, column=1, pady=10) # Login Button
             

                
# -------------------- For all Window-------------------------------------------------------------------------------------------------------------------------------



b_color= "#0b0c0d" # Prefered -------- "#xxxxxx" is Color Hex Code
button_color= "#858586" #I don't use it
color2 = "#cecece" #Prefered

root = Tk() # Reqruied
obj = Login_Sys(root) # Reqruied 
root.iconbitmap("C:/Users/..../..../..../..../xxxx.ico") # For All Window Icon -- .ico
root.mainloop() # You Need For Script Keep Open

