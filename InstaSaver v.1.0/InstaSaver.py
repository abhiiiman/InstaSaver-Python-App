from pathlib import Path
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
import requests
import instaloader as insta
from instaloader import Post
import webbrowser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# creating the fucntions here for the Button.
def minimize(): #button_1
    window.update_idletasks()
    window.state('withdrawn')
    window.overrideredirect(False)
    window.state('iconic')
def close(): #button_2
    os._exit(0)
#Function to check the internet connection
def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        print("You're connected to internet\n")
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
        return error
    except requests.ConnectionError:
        print("No internet connection available.")
    return False
def pp_download():
    mod = insta.Instaloader()
    pp_link = entry_1.get()
    try:
        if "https" in pp_link:
            short_link = pp_link[22:]
            username_list = short_link.split("?")
            username = username_list[0]
            print(username)
        else:
            username = str(pp_link)
        mod.download_profile(username, profile_pic_only = True)
        messagebox.showinfo("InstaSaver Message", "Profile Picture Downloaded Successfully")
    except Exception as error:
        messagebox.showerror("InstaSaver Message","Invalid Link Detected !")
def post_download():
    mod = insta.Instaloader()
    post_link = entry_2.get()
    try:
        link = post_link[28:]
        shortlink = link.split("/")
        post_tag = shortlink[0]
        post = Post.from_shortcode(mod.context, post_tag)
        mod.download_post(post, target = "Instasaver Post Downloads")
        messagebox.showinfo("InstaSaver Message", "Post Downloaded Successfully")
    except Exception as error:
        messagebox.showerror("InstaSaver Message","Invalid Link Detected !")
def tutorial():
    messagebox.showinfo("InstaSaver Message", "Opening In Your Default Browser")
    webbrowser.open("https://drive.google.com/file/d/1XRINurkUOuosYCxBVJ_5-bTRbfvmxVs6/view?usp=sharing")
def my_profile():
    messagebox.showinfo("InstaSaver Message", "Opening In Your Default Browser")
    webbrowser.open("https;//instagram.com/_m_abhijit_?utm_medium=copy_link")

window = Tk()
window.geometry("750x550")
window.configure(bg = "#576574")
window.iconbitmap(relative_to_assets("icon_logo.ico"))
window.title("InstaSaver : By Abhijit Mandal")
Tk_Width = 750
Tk_Height = 550
x_Left = int(window.winfo_screenwidth()/2 - Tk_Width/2)
y_Top = int(window.winfo_screenheight()/2 - Tk_Height/2)
window.geometry("+{}+{}".format(x_Left, y_Top))
# use the overredirect concept here
window.overrideredirect(True)
canvas = Canvas(
    window,
    bg = "#576574",
    height = 550,
    width = 750,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(375.0,275.0,image=image_image_1)

#creating the label for the internet connection.
if connection() == True:
    label = Label(window, text = "Connected :)", font = ("Microsoft YaHei UI Light",15,), bg = "#718093", fg = "#48dbfb")
    label.place(x = 600, y = 37)
elif connection() == error:
    label = Label(window, text = "Server Down !", font = ("Microsoft YaHei UI Light",15,), bg = "#718093", fg = "#48dbfb")
    label.place(x = 600, y = 37)
elif connection() == False:
    label = Label(window, text = "Not Connected :(", font = ("Microsoft YaHei UI Light",15,), bg = "#718093", fg = "#48dbfb")
    label.place(x = 600, y = 37)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    bg = "#222F3E",
    activebackground = "#222F3E",
    command=minimize,
    relief="flat"
)
button_1.place(
    x=696.0,
    y=10.0,
    width=21.0,
    height=10.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    bg = "#222F3E",
    activebackground = "#222F3E",
    command=close,
    relief="flat"
)
button_2.place(
    x=717.0,
    y=2.0,
    width=28.0,
    height=22.0
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(557.5,215.5,image=entry_image_1)
entry_1 = Entry(
    bd=0,
    bg="#576574",
    highlightthickness=0,
    font = ("Microsoft YaHei UI Light",14,),
    fg = "#A3CB38",
)
entry_1.place(
    x=404.0,
    y=194.0,
    width=307.0,
    height=41.0
)
entry_1.focus()
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    bg = "#718093",
    activebackground = "#718093",
    command=pp_download,
    relief="flat"
)
button_3.place(
    x=478.0,
    y=254.0,
    width=161.0,
    height=43.0
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    bg = "#718093",
    activebackground = "#718093",
    command=post_download,
    relief="flat"
)
button_4.place(
    x=481.0,
    y=471.0,
    width=161.0,
    height=43.0
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(558.5,432.5,image = entry_image_2)
entry_2 = Entry(
    bd=0,
    bg="#576574",
    highlightthickness=0,
    font = ("Microsoft YaHei UI Light",14,),
    fg = "#C4E538",
)
entry_2.place(
    x=405.0,
    y=411.0,
    width=307.0,
    height=41.0
)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    bg = "#576574",
    activebackground = "#576574",
    command=my_profile,
    relief="flat"
)
button_5.place(
    x=332.0,
    y=528.0,
    width=16.0,
    height=16.0
)

button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    bg = "#718093",
    activebackground = "#718093",
    command=tutorial,
    relief="flat"
)
button_6.place(
    x=37.0,
    y=474.0,
    width=303.0,
    height=37.0
)
window.resizable(False, False)
window.mainloop()
