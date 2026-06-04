import tkinter as tk
from tkinter import ttk
import customtkinter as CTk
from customtkinter import *
from tkinter import *
from PIL import Image
import customtkinter as ctk
from tkinter import messagebox, simpledialog, StringVar, ttk, Button
from openpyxl import Workbook, load_workbook
import os

# ------------------- Constants -------------------
EXCEL_FILE = "users.xlsx"
ADMIN_CREDENTIALS = {"username": "admin",
                    "password": "admin123"}

# Example item lists
hot_coffee_items = [("Espresso", 100.0)]
snacks_items = [("Muffin", 50.0)]
iced_tea_items = [("Lemon Iced Tea", 60.0)]
iced_coffee_items = [("Iced Latte", 120.0)]

# ------------------- Excel Helpers -------------------
def ensure_excel_file():
    if not os.path.exists(EXCEL_FILE):
        wb = Workbook()
        ws = wb.active
        ws.append(["Username",
                    "Password"]
                    )
        
        wb.save(EXCEL_FILE)
def load_users_from_excel():
    ensure_excel_file()
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    users = {}
    for row in ws.iter_rows(min_row=2,
                                            values_only=True
                                            ):
        
        if row[0] and row[1]:
            users[row[0]] = row[1]
    return users
def add_user_to_excel(username, password):
    wb = load_workbook(EXCEL_FILE)
    ws = wb.active
    ws.append([username, password])
    wb.save(EXCEL_FILE)

# - - - - - Function For Background Image - - - - -
def set_window_background(window, image_path):
        bg_image = ctk.CTkImage(Image.open(image_path),
                                         size=(window.winfo_width(),
                                               window.winfo_height())
                                         )
        
        bg_label = ctk.CTkLabel(window,
                                         image=bg_image,
                                         text=""
                                         )
        
        bg_label.place(x=0, y=0,
                                   relwidth=1,
                                   relheight=1
                                   )
        
        bg_label.lower()

        def update_bg_image(event):
            new_bg_image = ctk.CTkImage(Image.open(image_path),
                                                             size=(event.width, event.height))
            
            bg_label.configure(image=new_bg_image)

        window.bind("<Configure>", update_bg_image)

# - - - - - Log in Functions - - - - -
def login():
    username = login_frame_username.get().strip()
    password = login_frame_password.get().strip()
    users = load_users_from_excel()

    if username == ADMIN_CREDENTIALS["username"] and password == ADMIN_CREDENTIALS["password"]:
        messagebox.showinfo("Login Success", "Welcome, Admin!")
        second_main_window()
        main_window.withdraw()
    elif username in users and users[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        second_main_window()
        main_window.withdraw()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")
        return

def sign_up():
    def register():
        new_user = new_username.get().strip()
        new_pass = new_password.get().strip()
        users = load_users_from_excel()

        if not new_user or not new_pass:
            messagebox.showerror("Error", "Username and Password cannot be empty.")
        elif new_user in users:
            messagebox.showerror("Error", "Username already exists.")
        elif new_user == ADMIN_CREDENTIALS["username"]:
            messagebox.showerror("Error", "Cannot use admin username.")
        else:
            add_user_to_excel(new_user, new_pass)
            messagebox.showinfo("Success", "Account created successfully!")
            main_window.deiconify()
            sign_up_tab.destroy()

    sign_up_tab = CTk()
    sign_up_tab.geometry('300x300')
    main_window.withdraw()

    # - - - - - L A B E L - - - - - 
    CTkLabel(master=sign_up_tab, text="Create Account",
             font=('Arial', 25), text_color="white"
             ).place(relx=0.5, rely=0.2, anchor="center")

    # - - - - - E N T R Y - - - - - 
    new_username = CTkEntry(master=sign_up_tab, placeholder_text="Enter Email",
                            border_color="white",
                            width=250, fg_color="white",
                            text_color="black")
    new_username.place(relx=0.5, rely=0.38, anchor="center")

    new_password = CTkEntry(master=sign_up_tab,
                            placeholder_text="Enter Password",
                            border_color="white", width=250,
                            fg_color="white",
                            text_color="black",
                            show='•')
    new_password.place(relx=0.5, rely=0.5, anchor="center")

    # - - - - - B U T T O N S - - - - -
    create_account_button = CTkButton(master=sign_up_tab,
                                      text="Create Account",
                                      corner_radius=5,
                                      fg_color="cyan4",
                                      hover_color="#3AB09E",
                                      command=register
                                      )
    create_account_button.place(relx=0.48, rely=0.65, anchor="center")

    cancel_button = CTkButton(master=sign_up_tab,
                                 text="Cancel",
                                 corner_radius=5,
                                 fg_color="cyan4",
                                 hover_color="#3AB09E",
                                 command=lambda: [main_window.deiconify(), sign_up_tab.destroy()]
                                 )
    cancel_button.place(relx=0.48, rely=0.758, anchor="center")
    
    sign_up_tab.mainloop()

# - - - - - Second Main Window - - - - -
def second_main_window():
    main_window.withdraw()
    global lobby_window
    lobby_window = CTk()
    lobby_window.geometry('600x470')
    lobby_window.title('Coffee Life')
    lobby_window.config(bg='white')
    lobby_window.resizable(False, False)
    

    #  - - - - - Lobby Frame - - - - -
    global scrollable_lobby_frame
    scrollable_lobby_frame = CTkScrollableFrame(master=lobby_window,
                                             fg_color='#F5DEB3',
                                             bg_color='white',
                                             width=475,
                                             height=390,
                                             scrollbar_button_color='#a48b73',
                                             scrollbar_button_hover_color='#d7b57f',
                                             )
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')
    CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')

    scrollable_lobby_frame.place(relx=0.999, rely=1, anchor='se')

    lobby_window_frame1 = CTkFrame(master=lobby_window,
                                 fg_color='#dfbb7e',
                                 bg_color='transparent',
                                 border_color='#6B4423',
                                 border_width=1,
                                 width=200,
                                 height=700
                                 )

    lobby_window_frame1.place(relx=0.01,rely=0.5, anchor='center')

    lobby_window_frame2 = CTkFrame(master=lobby_window,
                                 fg_color='#3D2B1F',
                                 bg_color='transparent',
                                 border_color='#3D2B1F',
                                 border_width=1,
                                 width=750,
                                 height=100
                                 )

    lobby_window_frame2.place(relx=0.5, rely=0.05, anchor='center')

    # - - - - - Label - - - - -
    lobby_window_title = CTkLabel(master=lobby_window_frame2,
                                     text="☕COFFEE LIFE ૮ ˶ᵔ ᵕ ᵔ˶ ა",
                                     font=('Times New Roman', 35),
                                     bg_color='transparent',
                                     text_color='white',
                                     )

    lobby_window_title.place(relx=0.38, rely=0.62, anchor='center')

    # - - - - - Buttons - - - - -
    global lobby_window_logout
    global lobby_window_account_info
    global lobby_window_order_menu
    global currently_open_menu

    currently_open_menu = None

    def show_order_menu():
        global currently_open_menu
        if currently_open_menu != "order":
            clear_lobby_frame_content()
            order_menu_window()
            currently_open_menu = "order"

    def scrollable_frame():
        global currently_open_menu
        if currently_open_menu != "scrollable_lobby_frame":
            lobby_window.destroy()
            second_main_window()
            currently_open_menu = "scrollable_lobby_frame"
    
    def show_account_info():
        global currently_open_menu
        if currently_open_menu != "account_info":
            clear_lobby_frame_content()
            account_info()
            currently_open_menu = "account_info"

    def clear_lobby_frame_content():
        for widget in scrollable_lobby_frame.winfo_children():
            widget.destroy()

        CTkLabel(master=scrollable_lobby_frame,
             text="Welcome to Coffee Life",
             text_color='black',
             fg_color='#F5DEB3',
             bg_color='#F5DEB3',
             font=('Times New Roman', 35)
             ).pack(pady=10, anchor='center')

    lobby_window_logout = CTkButton(master=lobby_window_frame1,
                                     text='Logout',
                                     fg_color='#3D2B1F',
                                     hover_color='#6F4E37',
                                     font=('Times New Roman', 12),
                                     width=15,
                                     border_spacing=5,
                                     corner_radius=20,
                                     command=lambda:
                                     [lobby_window.destroy(),
                                      main_window.deiconify()]
                                     ).place(relx=0.721, rely=0.8, anchor="center")

    lobby_window_account_info = CTkButton(master=lobby_window_frame1,
                                      text='Account Info',
                                      fg_color='#3D2B1F',
                                      hover_color='#6F4E37',
                                      font=('Times New Roman', 12),
                                      width=13,
                                      border_spacing=2,
                                      corner_radius=20,
                                      command=show_account_info
                                      ).place(relx=0.721, rely=0.751, anchor="center")

    lobby_window_order_menu = CTkButton(master=lobby_window_frame1,
                                        text='Order Menu',
                                        fg_color='#3D2B1F',
                                        hover_color='#6F4E37',
                                        font=('Times New Roman', 12),
                                        width=12,
                                        border_spacing=2.1,
                                        corner_radius=20,
                                        command=show_order_menu
                                        ).place(relx=0.721, rely=0.705, anchor="center")
    
    lobby_window_home = CTkButton(master=lobby_window_frame1,
                                        text='    Home    ',
                                        fg_color='#3D2B1F',
                                        hover_color='#6F4E37',
                                        font=('Times New Roman', 12.5),
                                        width=12,
                                        border_spacing=2.3,
                                        corner_radius=20,
                                        command=scrollable_frame
                                        ).place(relx=0.721, rely=0.659, anchor="center")
    
    lobby_window.mainloop()

# - - - - - Order Menu Window - - - - -
def order_menu_window():
    global menu_checkout_frame
    global scrollable_lobby_frame
    snacks_menu = CTkScrollableFrame(master=scrollable_lobby_frame,
                                    fg_color='white',
                                    bg_color='transparent',
                                    width=400,
                                    height=200,
                                    scrollbar_button_color='#3D2B1F',
                                    scrollbar_button_hover_color='#954535',
                                    )
    snack_menu_label = CTkLabel(master=snacks_menu,
                                text="Snacks Menu",
                                text_color='black',
                                fg_color='white',
                                bg_color='white',
                                font=('Times New Roman', 20)
                                ).pack(pady=10, anchor='n')
    snacks_menu.pack(pady=10, expand=True)

    tea_menu = CTkScrollableFrame(master=scrollable_lobby_frame,
                                    fg_color='white',
                                    bg_color='transparent',
                                    width=400,
                                    height=200,
                                    scrollbar_button_color='#3D2B1F',
                                    scrollbar_button_hover_color='#954535',
                                    )
    tea_menu_label = CTkLabel(master=tea_menu,
                                text="Tea Menu",
                                text_color='black',
                                fg_color='white',
                                bg_color='white',
                                font=('Times New Roman', 20)
                                ).pack(pady=10, anchor='n')
    tea_menu.pack(pady=10, expand=True)

    coffee_menu = CTkScrollableFrame(master=scrollable_lobby_frame,
                                    fg_color='white',
                                    bg_color='transparent',
                                    width=400,
                                    height=200,
                                    scrollbar_button_color='#3D2B1F',
                                    scrollbar_button_hover_color='#954535',
                                    )
    coffee_menu_label = CTkLabel(master=coffee_menu,
                                text="Coffee Menu",
                                text_color='black',
                                fg_color='white',
                                bg_color='white',
                                font=('Times New Roman', 20)
                                ).pack(pady=10, anchor='n')
    coffee_menu.pack(pady=10, expand=True)

    non_coffee_menu = CTkScrollableFrame(master=scrollable_lobby_frame,
                                    fg_color='white',
                                    bg_color='transparent',
                                    width=400,
                                    height=200,
                                    scrollbar_button_color='#3D2B1F',
                                    scrollbar_button_hover_color='#954535',
                                    )
    non_coffee_menu_label = CTkLabel(master=non_coffee_menu,
                                text="Non-Coffee Menu",
                                text_color='black',
                                fg_color='white',
                                bg_color='white',
                                font=('Times New Roman', 20)
                                ).pack(pady=10, anchor='center')
    non_coffee_menu.pack(pady=10, expand=True)

    menu_checkout_frame = CTkFrame(master=scrollable_lobby_frame,
                                    fg_color='white',
                                    bg_color='transparent',
                                    width=400,
                                    height=200,
                                    )

    # - - - - - Order Menu Button - - - - -
    checkout_button = CTkButton(master=menu_checkout_frame,
                                  text='Checkout',
                                  fg_color='#3D2B1F',
                                  hover_color='#6F4E37',
                                  font=('Times New Roman', 15),
                                  width=15,
                                  border_spacing=2,
                                  corner_radius=15,
                                  command=lambda:[checkout_window()]
                                  )
    checkout_button.place(relx=0.85, rely=0.85, anchor="center")
    menu_checkout_frame.pack(pady=10, expand=True)

def checkout_window():
    checkout_main_window = CTk()
    lobby_window.withdraw()
    checkout_main_window.geometry('370x460')
    checkout_main_window.config(bg='white')
    checkout_main_window.title('Coffe Life | Checkout')
    checkout_main_window.resizable(False, False)

    # - - - - - Checkout Main Window Frame - - - - -
    checkout_main_window_frame = CTkFrame(master=checkout_main_window,
                                          fg_color='white',
                                          bg_color='transparent',
                                          border_color='black',
                                          border_width=2,
                                          width=300,
                                          height=380
                                          )
    checkout_main_window_frame.place(relx=0.5, rely=0.53, anchor='center')

# - - - - - Checkout Main Window Label - - - - -
    CTkLabel(master=checkout_main_window,
             text='   O  R  D  E  R     F  O  R  M   ',
             text_color='black',
             fg_color='white',
             bg_color='white',
             font=('Times New Roman', 20),
             ).place(relx=0.5, rely=0.12, anchor='center')
    
    # - - - - - Checkout Main Window Button - - - - - 
    checkout_main_window_button = CTkButton(master=checkout_main_window,
                                    text='Cancel',
                                    fg_color='#3D2B1F',
                                    bg_color='white',
                                    hover_color='#6F4E37',
                                    font=('Times New Roman', 15),
                                    width=18,
                                    border_spacing=3,
                                    corner_radius=32,
                                    command=lambda:[lobby_window.deiconify(), checkout_main_window.destroy()])
    checkout_main_window_button.place(relx=0.5, rely=0.85, anchor="center")
    
    checkout_main_window.mainloop()

# - - - - - Account Info Window- - - -
def account_info():
    account_info_window = CTkFrame(master=scrollable_lobby_frame,
                               fg_color='#d7b57f',
                               bg_color='transparent',
                               width=450,
                               height=720,
                               corner_radius=20
                               )
    account_info_window.pack(padx=15,pady=10, expand=True)

    # - - - - - Account Info Label - - - - -
    username = login_frame_username.get().strip()
    account_info_label = CTkLabel(master=account_info_window,
                                  text=f"  Hello {username}!",
                                  text_color='#3D2B1F',
                                  font=('Times New Roman', 15, "bold"),
                                  bg_color='#F5DEB3',
                                  corner_radius=200,
                                  width=270,
                                  anchor='w'
                                  )
    account_info_label.place(relx=0.14, rely=0.16, anchor='nw')

    account_info_label = CTkLabel(master=account_info_window,
                                  text="  Username :",
                                  text_color='#3D2B1F',
                                  corner_radius=15,
                                  bg_color='#F5DEB3',
                                  font=('Times New Roman', 17, "bold"),
                                  width=100,
                                  anchor='w'
                                  )
    account_info_label.place(relx=0.2, rely=0.13, anchor='center')

# - - - - - Main Window - - - - -
main_window = CTk()
main_window.geometry('600x470')
main_window.title('Coffe Life | Log In')
main_window.resizable(False, False)


# - - - - - Background Picture - - - - -
image_path = "Coffee_Life.jpg"
set_window_background(main_window, image_path)


# - - - - - Frame - - - - -
login_frame = CTkFrame(master=main_window,
                         fg_color='#6B4423',
                         bg_color='transparent',
                         border_color='#6B4423',
                         border_width=3,
                         width=500,
                         height=471
                         )

login_frame.place(relx=0.40, rely=0.5, anchor='w')

# - - - - - Label - - - - -
login_frame_label = CTkLabel(master=login_frame,
                                     text="☕COFFEE LIFE",
                                     text_color='white',
                                     fg_color='#6B4423',
                                     bg_color='#6B4423',
                                     font=('Times New Roman', 45)
                                     ).place(relx=0.36, rely=0.31, anchor='center')

# - - - - - Entry - - - - -
login_frame_username = CTkEntry(master=login_frame,
                                                 placeholder_text="Username",
                                                 width=250,
                                                 fg_color='white',
                                                 text_color='black',
                                                 border_color='white'
                                                 )
login_frame_username.place(relx=0.37, rely=0.45, anchor="center")

login_frame_password = CTkEntry(master=login_frame,
                                                 placeholder_text="Password",
                                                 width=250,
                                                 fg_color='white',
                                                 text_color='black',
                                                 border_color='white',
                                                 show='•'
                                                 )
login_frame_password.place(relx=0.37, rely=0.53, anchor="center",)

# - - - - - Buttons - - - - -
login_frame_signin = CTkButton(master=login_frame,
                                text='Sign In',
                                fg_color='#3D2B1F',
                                hover_color='#6F4E37',
                                font=('Times New Roman', 15),
                                width=18,
                                border_spacing=3,
                                command=login,
                                corner_radius=32,).place(relx=0.54, rely=0.62, anchor="center")

login_frame_signup = CTkButton(master=login_frame,
                                             text='Sign Up',
                                             fg_color='#3D2B1F',
                                             hover_color='#6F4E37',
                                             font=('Times New Roman', 15),
                                             width=18,
                                             border_spacing=3,
                                             corner_radius=32,
                                             command=sign_up
                                             ).place(relx=0.2, rely=0.62, anchor="center")

main_window.mainloop()