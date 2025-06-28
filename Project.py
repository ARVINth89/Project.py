from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from pymongo import MongoClient

# MongoDB setup

client = MongoClient("localhost" , 27017)
db = client["Resturant"]
coll = db["Foods"]

# bg & fg

BG_1 = "#00FF2A"
BG_2 = "#00FFEA"
BG_3 = "#FFBC03"
FG_1 = "#2600FF"
FG_2 = "#FF0000"
FG_3 = "#83006D"
ROOT_COLOR = "#C8FF00"

food_list = []
Food_Dict = {}

# def

def Admin() :
    new_Window = Toplevel(root)
    new_Window.title("Admin")
    new_Window.geometry("500x500")
    new_Window.configure(bg = ROOT_COLOR)
    Label(new_Window , text = "Here is Your New Window for Manage Your Resturant", bg = BG_1 , fg = FG_1 ,
          font = ("Aryal" , 15 , "normal")).pack()
    Label(new_Window , text = "Now You Can Add a Food" , bg = BG_3 , fg = FG_3 , font = ("Aryal" , 15 , "bold")).pack()
    Label(new_Window , text = "Food" , bg = ROOT_COLOR , font = ("Aryal" , 15 , "bold")).pack()
    Add_entry = Entry(new_Window , bg = BG_2 , fg = FG_2 , insertbackground = FG_1 , border = 3 ,
                      font = ("Aryal" , 15 , "bold"))
    Add_entry.pack()
    Label(new_Window , text = "Price" , bg = ROOT_COLOR , font = ("Aryal" , 15 , "bold")).pack()
    Price_entry = Entry(new_Window , bg = BG_2 , fg = FG_2 , insertbackground = FG_1 , border = 3 ,
                      font = ("Aryal" , 15 , "normal"))
    Price_entry.pack()
    Label(new_Window , text = "Category" , bg = ROOT_COLOR , font = ("Aryal" , 15 , "bold")).pack()
    Category_entry = Entry(new_Window , bg = BG_2 , fg = FG_2 , insertbackground = FG_1 , border = 3 ,
                           font = ("Aryal" , 15 , "normal"))
    Category_entry.pack()
    def Add_To_List() :
        New_Food = Add_entry.get().strip()
        Food_Price = Price_entry.get().strip()
        Category = Category_entry.get().strip()
        if New_Food and Food_Price and Category :
            Food_Dict = {"name" : New_Food  , "price" : Food_Price , "category" : Category}
            coll.insert_one(Food_Dict)
            messagebox.showinfo("Add" , "Your Food is Added To Your Food List")
            Add_entry.delete(0 , END)
        else :
            messagebox.showerror("Error" , "Your Food isn't Added To Your Food List")
    Add_btn = Button(new_Window , text = "Add" , bg = BG_1 , fg = FG_1 ,
                     font = ("Aryal" , 15 , "italic") , command = Add_To_List)
    Add_btn.pack()

def User() :
    foods = list(Food_Dict.values())
    new_root = Toplevel(root)
    new_root.title("User")
    new_root.geometry("500x500")
    new_root.configure(bg = ROOT_COLOR)
    Label(new_root , text = "You Can Buy anythink From list" , bg = BG_3 , fg = FG_3).pack()
    Add_Combo = ttk.Combobox(new_root , values = foods)
    Add_Combo.pack()
    Add_Combo = food_list
    Buy_btn = Button(new_root , text = "Buy" , font = ("Aryal" , 15 , "normal") , bg = BG_1 , fg = FG_1)
    Buy_btn.pack(pady = 20)
    More_Product_btn = Button(new_root , text = "Do You Want To Buy More Products ?",
                              font = ("Aryal" , 15 , "bold") , bg = BG_3 , fg = FG_3 , command = lambda : Buy_More())
    More_Product_btn.pack()
    More_Product_Example_label = Label(new_root , text = "example : ice creem , cooffe , ..." ,
                                       font = ("Aryal" , 15 , "normal") , bg = BG_3 , fg = FG_3)
    More_Product_Example_label.pack()

    def Buy_More() :
        new_root_new = Toplevel(new_root)
        new_root_new.title("Buy More")
        new_root_new.geometry("300x300")
        new_root_new.configure(bg = ROOT_COLOR)
        Label(new_root_new , text = "Now You Can Buy Products Without Food" , bg = BG_2 , fg = FG_2 ,
              font = ("Aryal" , 10 , "bold")).pack()
        Buy_Combo = ttk.Combobox(new_root_new)
        Buy_Combo.pack()



###############################################################################################################
###############################################################################################################
###############################################################################################################

# root setup

root = Tk()
root.title("🍟🌭🍕🍔Resturant🍔🍕🌭🍟")
root.geometry("600x600")
root.configure(bg = ROOT_COLOR)

######################################################################################################################

# FoolScreen

is_fullscreen = True
root.attributes("-fullscreen" , True)

def toggle_fullscreen() :
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes("-fullscreen" , is_fullscreen)

BTN_toggle = Button(root , text = "💱Toggle Full Screen💱" , bg = ("light gray") , command = toggle_fullscreen)
BTN_toggle.pack(pady = 1 , padx = 40)
######################################################################################################################

# Label & Button
Welcome_lbl = Label(root , text = "Welcome To My Resturant" , bg = BG_3 , fg = FG_3 , font = ("Aryal" , 15 , "underline"))
Welcome_lbl.pack()
Want_lbl = Label(root , text = "Are You Admin or User ?" , bg = BG_2 , fg = FG_2 , font = ("Aryal" , 15 , "normal"))
########font = normal , italic , bold , underline

Want_lbl.pack()
Admin_btn = Button(root , text = "ADMIN" , bg = BG_1 , fg = FG_1 , font = ("Aryal" , 30 , "bold") , command = Admin)
Admin_btn.pack(pady = 20)
User_btn = Button(root , text = "USER" , bg = BG_1 , fg = FG_1 , font = ("Aryal" , 30 , "bold") , command = User)
User_btn.pack(pady = 5)

root.mainloop()