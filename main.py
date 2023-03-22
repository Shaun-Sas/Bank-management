import tkinter as tk

class Login:
    def __init__(self, window,):

        self.window = window
        self.window.title("Login")

        self.frame = tk.Frame(self.window)
        self.frame.pack()
        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()


        self.submit_button = tk.Button(self.frame, text="Login", command=self.login)
        self.submit_button.pack()


        self.status_label = tk.Label(self.frame, text="")
        self.status_label.pack()


    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = "1234"
        passw= "1234"

        if user==username and password==passw:
            self.window.after(10000, self.hello())

        else:
            self.status_label.config(text="Invalid username or password")

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def hello(self):
        self.window.destroy()
        window = tk.Tk()
        mainWindow(window)
        window.mainloop()

class mainWindow:
    def __init__(self,window):
        self.balance = 0
        self.window = window
        self.window.title("Main page")
        self.window.config(padx=10,pady=10)

        self.canvas = tk.Canvas(height=400, width=400)
        self.canvas.grid(row=0,column=1)
        self.text = self.canvas.create_text(200,100,text="Login Successful")

        self.text2 = self.canvas.create_text(200, 135, text="Account=Shaunak")

        self.enquiry = tk.Button(text="Enquiry",command=self.enq)
        self.enquiry.grid(row=2,column=0)
        self.deposit = tk.Button(text="Deposit",command=self.dep)
        self.deposit.grid(row=2, column=1)
        self.withdraw = tk.Button(text="Withdraw",command=self.withdr)
        self.withdraw.grid(row=2, column=2)

        self.text3= self.canvas.create_text(200, 170, text="")

        self.text4 = tk.Label()
        self.text4.grid(row=1, column=2)

        self.input = tk.Entry()
        self.input.grid(row=1,column=1)


    def enq(self):
        self.canvas.itemconfig(self.text3,text=f"The total balance is :{ self.balance}")

    def dep(self):
        self.canvas.itemconfig(self.text3,text="Enter an amount you want to deposit")
        self.balance = int(self.balance)
        self.amount = self.input.get()
        self.amount = int(self.amount)
        print(type(self.amount))

        self.balance = int(self.balance) + self.amount
        self.balance= str(self.balance)
        self.text4.config(text=f"The total balance is  {self.balance}")

    def withdr(self):
        self.amount = self.input.get()
        self.balance = int(self.balance)
        self.amount = int(self.amount)
        if self.amount < self.balance:
            self.balance = int(self.balance)- self.amount
            self.balance = str(self.balance)
            self.text4.config(text=f"The total balance left is  {self.balance}")
        else:
            self.text4.config(text=f"You Have Insufficient funds")

root = tk.Tk()
login_window = Login(root)
root.mainloop()

