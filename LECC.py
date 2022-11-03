# Created by Mintmann, aka: Davi Rich
# https://forums.linuxmint.com/
# 2022-11-03, version 1.1, Probably the final release
# Developed on Linux Mint 21 Cinnamon
# Pycharm 2022.2.3 (Community Edition) & Python 3.10.6
# functions usually use (event) but that causes a stupid warning so instead of (event) use (_)
# place this script somewhere on disk such as in Documents
# using Terminal cd there and follow the instructions below:
# to make this script usable change its permissions to allow running it
# to run this script in Terminal type at $: python3 LECC.py

import os
import stat
import tkinter as tk
import platform
import subprocess
import webbrowser
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from subprocess import PIPE
from datetime import datetime

# works
pcid = platform.system()
pcidr = platform.release()
pcidv = platform.version()


def center(win):
    # centers a tkinter window
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


root = Tk()
# affects window objects and status line but not the menu line
root.option_add("*Font", 'Georgia 10')
root.title(" LECC - Linux Easy Command Center ")
root.geometry("800x600")
root.maxsize(800, 600)
root.minsize(800, 600)
center(root)

# Create an instance of ttk style
# ('aqua', 'step', 'clam', 'alt', 'default', 'classic')
s = ttk.Style()
s.theme_use('default')
s.configure('TNotebook.Tab', background="lightgray")
s.map("TNotebook.Tab", background=[("selected", "magenta")])


tab_control = ttk.Notebook(root)

# Linux
# tab1
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Linux 1')
# tab2
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Linux 2')
tab_control.pack(expand=1, fill='both')
# tab3
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text='Linux 3')
tab_control.pack(expand=1, fill='both')
# tab4
tab4 = ttk.Frame(tab_control)
tab_control.add(tab4, text='Linux 4')
tab_control.pack(expand=1, fill='both')
# tab5
tab5 = ttk.Frame(tab_control)
tab_control.add(tab5, text='Linux Run 1')
tab_control.pack(expand=1, fill='both')
# tab6
tab6 = ttk.Frame(tab_control)
tab_control.add(tab6, text='Linux Run 2')
tab_control.pack(expand=1, fill='both')
# tab6
tab7 = ttk.Frame(tab_control)
tab_control.add(tab7, text='Linux List')
tab_control.pack(expand=1, fill='both')


# entering a password here prevents the prompt
mepaswrd = ""
while len(mepaswrd) == 0:
    mepaswrd = simpledialog.askstring(title="Enter your password to continue!", prompt="My password is: ")
    if mepaswrd == "quit":
        exit()


datenow = datetime.today()
global_slist = []


def abouterr(serr):
    messagebox.showinfo(title="Whoops!", message=str(serr))


# in Terminal cd ~/.config
# cat user-dirs.dirs
# /etc/xdg/
# b'/home/adroit/Desktop\n'
# maybe have rmdir LECC

findme = (os.environ['HOME'])
findme = findme.replace("home", "")
findme = findme.replace("/", "")
global_folder_path = subprocess.check_output(['xdg-user-dir', 'DESKTOP']).decode()
global_folder_path = global_folder_path.strip('\n')
global_folder_path = global_folder_path + "/LECC"
isExist = os.path.exists(global_folder_path)
if isExist == FALSE:
    try:
        os.mkdir(global_folder_path, 0o0777)
    except OSError as error:
        abouterr(error)    # display an error box


def loadfolderlist():
    global global_slist_list
    global ilen
    global_slist_list = os.listdir(global_folder_path)
    ilen = len(global_slist_list)
    if ilen == 0:
        global_slist_list = "nothing"


def refreshcb():
    loadfolderlist()
    win_listOpts.set("")
    win_listOpts.update()
    win_listOpts['values'] = global_slist_list
    win_listOpts.current(0)
    win_listOpts.update()


def urlmint():
    webbrowser.open('https://forums.linuxmint.com/')


def urldistros():
    webbrowser.open('https://distrowatch.com/')


def openaboutwindow():
    about = Toplevel(root)
    about.option_add("*Font", 'Georgia 10')
    about.title("LECC - About")
    about.geometry("520x400")
    about.maxsize(520, 400)
    about.minsize(520, 400)

    statusbar2 = Label(about, bg="#A9A9A9", text="About", bd=1, relief=FLAT, anchor=W)
    statusbar2.pack(side=BOTTOM, fill=X)

    varrequire = StringVar()
    varrequire.set("I am new to Python & Linux distros. This is my first Python script.")
    labelvarvarrequire = Label(about, textvariable=varrequire, font=("Georgia", 10))
    labelvarvarrequire.place(x=20, y=20)

    varintro = StringVar()
    varintro.set("To run this script you will need PyCharm/Python3 & tkinter.")
    labelvarintro1 = Label(about, textvariable=varintro, font=("Georgia", 10))
    labelvarintro1.place(x=20, y=40)

    varintro2 = StringVar()
    varintro2.set("Or run it in Terminal my typing: 'python3 [it's path]LECC.py'.")
    labelvarintro12 = Label(about, textvariable=varintro2, font=("Georgia", 10))
    labelvarintro12.place(x=20, y=60)

    varintro3 = StringVar()
    varintro3.set("Example: $ python3 /home/mememe/Documents/PyCharm_Projects/LECC.py.")
    labelvarintro13 = Label(about, textvariable=varintro3, font=("Georgia", 10))
    labelvarintro13.place(x=20, y=80)

    var1 = StringVar()
    var1.set("Typing Terminal commands became tedious so I made this Python script.")
    label1 = Label(about, textvariable=var1, font=("Georgia", 10))
    label1.place(x=20, y=120)

    var2 = StringVar()
    var2.set("This script does not make any system changes!!")
    label2 = Label(about, textvariable=var2, font=("Georgia", 10))
    label2.place(x=20, y=140)

    var3 = StringVar()
    var3.set("The script will prompt for your password unless you store it in the script.")
    label3 = Label(about, textvariable=var3, font=("Georgia", 10))
    label3.place(x=20, y=160)

    var4 = StringVar()
    var4.set("The first time this program runs a desktop directory will be created, LECC.")
    label4 = Label(about, textvariable=var4, font=("Georgia", 10))
    label4.place(x=20, y=180)

    var5b = StringVar()
    var5b.set("This script puts text files into the desktop folder, LECC.")
    label5b = Label(about, textvariable=var5b, font=("Georgia", 10))
    label5b.place(x=20, y=200)

    var5 = StringVar()
    var5.set("The output file names are a representation of the command.")
    label5 = Label(about, textvariable=var5, font=("Georgia", 10))
    label5.place(x=20, y=220)

    var6 = StringVar()
    var6.set("")
    label6 = Label(about, textvariable=var6, font=("Georgia", 10))
    label6.place(x=20, y=240)

    var7 = StringVar()
    var7.set("Some commands will not work unless they are installed.")
    label7 = Label(about, textvariable=var7, font=("Georgia", 10))
    label7.place(x=20, y=260)

    var8a = StringVar()
    var8a.set("Examples; GParted, HWinfo, LSScsi, Pip, Python, Nvidia, PSensor, VLC.")
    label8a = Label(about, textvariable=var8a, font=("Georgia", 10))
    label8a.place(x=20, y=280)

    var8 = StringVar()
    var8.set("")
    label8 = Label(about, textvariable=var8, font=("Georgia", 10))
    label8.place(x=20, y=300)

    # about menus
    menubar2 = Menu(about, bg="#A9A9A9", relief=FLAT)
    filemenu2 = Menu(menubar2, tearoff=0)

    filemenu2.add_command(label="Close", font=("Georgia", 10), activeforeground="#FF00FF", command=about.destroy)
    menubar2.add_cascade(label="File", font=("Georgia", 10), activeforeground="#FF00FF", menu=filemenu2)

    about.config(menu=menubar2)
    center(about)
    about.mainloop()


def opennoteswindow():
    notes = Toplevel(root)
    notes.option_add("*Font", 'Georgia 10')
    notes.title("LECC - Notes")
    notes.geometry("510x400")
    notes.maxsize(520, 400)
    notes.minsize(520, 400)

    statusbar2 = Label(notes, bg="#A9A9A9", text="Notes", bd=1, relief=FLAT, anchor=W)
    statusbar2.pack(side=BOTTOM, fill=X)

    varrequire = StringVar()
    varrequire.set("Many Linux commands are listed on the tabs.")
    labelvarvarrequire = Label(notes, textvariable=varrequire, font=("Georgia", 10))
    labelvarvarrequire.place(x=20, y=20)

    varrequire2 = StringVar()
    varrequire2.set("Each one has a Run & Man(ual) button and a description.")
    labelvarvarrequire2 = Label(notes, textvariable=varrequire2, font=("Georgia", 10))
    labelvarvarrequire2.place(x=20, y=40)

    varrequire2b = StringVar()
    varrequire2b.set("The Run buttons execute the command.")
    labelvarvarrequire2b = Label(notes, textvariable=varrequire2b, font=("Georgia", 10))
    labelvarvarrequire2b.place(x=20, y=60)

    varrequire2c = StringVar()
    varrequire2c.set("The Man(ual) buttons retrieve the commands' manual documentation.")
    labelvarvarrequire2c = Label(notes, textvariable=varrequire2c, font=("Georgia", 10))
    labelvarvarrequire2c.place(x=20, y=80)

    varrequire3 = StringVar()
    varrequire3.set("Some commands have a combobox with options/switches.")
    labelvarvarrequire3 = Label(notes, textvariable=varrequire3, font=("Georgia", 10))
    labelvarvarrequire3.place(x=20, y=120)

    varrequire3b = StringVar()
    varrequire3b.set("The Linux List tab will list the files that are in the directory LECC.")
    labelvarvarrequire3b = Label(notes, textvariable=varrequire3b, font=("Georgia", 10))
    labelvarvarrequire3b.place(x=20, y=140)

    varrequire3c = StringVar()
    varrequire3c.set("Choosing a file in the combobox will load it into the editor 'xed'.")
    labelvarvarrequire3c = Label(notes, textvariable=varrequire3c, font=("Georgia", 10))
    labelvarvarrequire3c.place(x=20, y=160)

    varlayout4 = StringVar()
    varlayout4.set("")
    labelvarlayout4 = Label(notes, textvariable=varlayout4, font=("Georgia", 10))
    labelvarlayout4.place(x=20, y=180)

    varlayout4 = StringVar()
    varlayout4.set("Script will prompt for the user password.")
    labelvarlayout4 = Label(notes, textvariable=varlayout4, font=("Georgia", 10))
    labelvarlayout4.place(x=20, y=200)

    varlayout4 = StringVar()
    varlayout4.set("However the password can be entered into the script to skip the prompt.")
    labelvarlayout4 = Label(notes, textvariable=varlayout4, font=("Georgia", 10))
    labelvarlayout4.place(x=20, y=220)

    # about menus
    menubar2 = Menu(notes, bg="#A9A9A9", relief=FLAT)
    filemenu2 = Menu(menubar2, tearoff=0)

    filemenu2.add_command(label="Close", font=("Georgia", 10), activeforeground="#FF00FF", command=notes.destroy)
    menubar2.add_cascade(label="File", font=("Georgia", 10), activeforeground="#FF00FF", menu=filemenu2)

    notes.config(menu=menubar2)
    center(notes)
    notes.mainloop()


def openerrorwindow(prog):
    about = Toplevel(root)
    about.option_add("*Font", 'Georgia 10')
    about.title("Run Error")
    about.geometry("300x100")
    about.maxsize(300, 120)
    about.minsize(300, 120)

    statusbar2 = Label(about, bg="#A9A9A9", text="Notice", bd=1, relief=FLAT, anchor=W)
    statusbar2.pack(side=BOTTOM, fill=X)

    var1 = StringVar()
    var1.set("'" + prog + "' appears to not exist.")
    label1 = Label(about, textvariable=var1, font=("Georgia", 12))
    label1.place(x=20, y=20)

    # menus
    menubar2 = Menu(about, bg="#A9A9A9", relief=FLAT)
    filemenu2 = Menu(menubar2, tearoff=0)

    filemenu2.add_command(label="Close", font=("Georgia", 10), activeforeground="#FF00FF", command=about.destroy)
    menubar2.add_cascade(label="File", font=("Georgia", 10), activeforeground="#FF00FF", menu=filemenu2)

    about.config(menu=menubar2)
    center(about)
    about.mainloop()


def buttonquithandler():
    response = str(messagebox.askquestion("Quit", "Are you sure you want to quit?"))
    if response.lower().startswith("yes"):
        exit()


s = ttk.Style()
s.theme_use('default')
# s.configure("TButton", fieldbackground="orange", background="magenta")     # affects buttons only
s.configure("TCombobox", fieldbackground="orange", background="#0288d1")    # affects combobox dropdown arrow

system_info = platform.platform()
statusbar = Label(root, bg="#A9A9A9", text=system_info, bd=1, relief=FLAT, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

loadfolderlist()


# inxi
def inxi_changed(_):
    msg = inxiOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


# tab 1 comboboxes
inxiOptions = ('b - cpu,speeds,mem,system,machine,cpu,graphics,network,drives,processes',
               'i - Network device info', 'r - Distro repositories', 's - Sensors (temps & fan speeds',
               'tcm - Show CPU process & Show memory used (top 5)', 'w - Weather (local)',
               'A - Show Audio/sound card(s) info & driver(s)', 'B - System battery',
               'C - Show full CPU output, include core speeds & CPU max speed (if available)',
               'D - Shows total disk space & used percentage', 'F - Show Full output for inxi',
               'G - Show graphic card(s) info & driver(s)',
               'I - Show Info: processes, uptime, memory, GiB used, shell, version',
               'M - Show computer information?', 'N - Show network info & driver',
               'S - Show System info: host name, kernel, desktop environment',
               'Fxpmzr - Show system information list')

selected_inxi = tk.StringVar()
inxiOpts = ttk.Combobox(tab1, textvariable=selected_inxi, width=30)    
inxiOpts['values'] = inxiOptions
inxiOpts['state'] = 'readonly'
inxiOpts.current(0)
inxiOpts.place(relx=.32, rely=0.158)       # place does nothing
inxiOpts.bind('<<ComboboxSelected>>', inxi_changed)


# df
def df_changed(_):
    msg = dfOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


dfOptions = ('a - List pseudo, duplicate, inaccessible', 'l - List local file systems',
             'm - List mounted file systems', 'h - Disk usage')

selected_df = tk.StringVar()
dfOpts = ttk.Combobox(tab1, textvariable=selected_df, width=30)    
dfOpts['values'] = dfOptions
dfOpts['state'] = 'readonly'
dfOpts.current(0)
dfOpts.place(relx=.32, rely=0.329)       # place does nothing
dfOpts.bind('<<ComboboxSelected>>', df_changed)


# dmidecode -t
def dmidecode_changed(_):
    msg = dmidecodeOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


dmidecodestr = ('0 - BIOS', '1 - System', '2 - Baseboard', '3 - Chassis', '4 - Processor', '5 - Memory Controller',
                '6 - Memory Module', '7 - Cache', '8 - Port Connector', '9 - System Slots',
                '10 - On-Board Devices', '11 - OEM Strings', '12 - System Config Options',
                '13 - Bios Language', '16 - Physical Memory Array', '17 - Memory Devices', '18 - 32bit Memory Error',
                '19 - Memory Array Mapped', '20 - Memory Devices Mapped', '26 - Voltage Probe',
                '27 - Cooling Device', '28 - Temperature Probes', '29 - Electrical Current Probe',
                '32 - System Boot', '34 - Mgmt Device', '35 - Mgmt Device Comp',
                '36 - Mgmt Device Threshold Data', '39 - Power Supply', '40 - Additional Info.',
                '41 - Onboard Devices Ext. Info.')

dmidecodeOptions = dmidecodestr
selected_dmidecode = tk.StringVar()
dmidecodeOpts = ttk.Combobox(tab1, textvariable=selected_dmidecode, width=30)    
dmidecodeOpts['values'] = dmidecodeOptions
dmidecodeOpts['state'] = 'readonly'
dmidecodeOpts.current(0)
dmidecodeOpts.place(relx=.32, rely=0.216)       # place does nothing
dmidecodeOpts.bind('<<ComboboxSelected>>', dmidecode_changed)


# xinput
def xinput_changed(_):
    msg = xinputOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


xinputOptions = ("list - All the input devices",
                 "list --long - Includes detailed info about capabilities of devices")

selected_xinput = tk.StringVar()
xinputOpts = ttk.Combobox(tab1, textvariable=selected_xinput, width=30)    
xinputOpts['values'] = xinputOptions
xinputOpts['state'] = 'readonly'
xinputOpts.current(0)
xinputOpts.place(relx=.32, rely=0.274)       # place does nothing
xinputOpts.bind('<<ComboboxSelected>>', xinput_changed)


# lpstat
def lpstat_changed(_):
    msg = lpstatOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


lpstatstr = ("d - Current default destination", "e - Available destinations on local network",
             "H - Server host name and port", "l - Long listing of printers, classes, jobs", "r - CUPS server status",
             "s - Status summery", "t - All status information: a,c,d,o,p,r,v",
             "u - List current user print jobs", "v - List printers")

lpstatOptions = lpstatstr
selected_lpstat = tk.StringVar()
lpstatOpts = ttk.Combobox(tab1, textvariable=selected_lpstat, width=30)    
lpstatOpts['values'] = lpstatOptions
lpstatOpts['state'] = 'readonly'
lpstatOpts.current(0)
lpstatOpts.place(relx=.32, rely=0.619)       # place does nothing
lpstatOpts.bind('<<ComboboxSelected>>', lpstat_changed)


# uname
def uname_changed(_):
    msg = unameOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


unamestr = ("a - Print all known information", "i - hardware platform", "m - system architecture",
            "n - network node hostname", "o - operating system", "p - processor type",
            "r - kernel release", "s - kernel name", "v - kernel version")

unameOptions = unamestr
selected_uname = tk.StringVar()
unameOpts = ttk.Combobox(tab1, textvariable=selected_uname, width=30)    
unameOpts['values'] = unameOptions
unameOpts['state'] = 'readonly'
unameOpts.current(0)
unameOpts.place(relx=.32, rely=0.386)       # place does nothing
unameOpts.bind('<<ComboboxSelected>>', uname_changed)


# nvidia
def nvidia_changed(_):
    msg = nvidiaOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


nvidiastr = ("@ - No switch shows gpu driver info", "L - Shows gpu name")

nvidiaOptions = nvidiastr
selected_nvidia = tk.StringVar()
nvidiaOpts = ttk.Combobox(tab1, textvariable=selected_nvidia, width=30)    
nvidiaOpts['values'] = nvidiaOptions
nvidiaOpts['state'] = 'readonly'
nvidiaOpts.current(0)
nvidiaOpts.place(relx=.32, rely=0.099)       # place does nothing
nvidiaOpts.bind('<<ComboboxSelected>>', nvidia_changed)


# hostname
def hostname_changed(_):
    msg = hostnameOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


hostnamestr = ("@ - No switch shows the host name", "I - Shows the ip adddress")

hostnameOptions = hostnamestr
selected_hostname = tk.StringVar()
hostnameOpts = ttk.Combobox(tab1, textvariable=selected_hostname, width=30)    
hostnameOpts['values'] = hostnameOptions
hostnameOpts['state'] = 'readonly'
hostnameOpts.current(0)
hostnameOpts.place(relx=.32, rely=0.447)       # place does nothing
hostnameOpts.bind('<<ComboboxSelected>>', hostname_changed)


# tab 2 comboboxes
# ifconfig
def ifconfig_changed(_):
    msg = ifconfigOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


ifconfigstr = ("a - List all available interfaces", "s - Short list of interfaces")

ifconfigOptions = ifconfigstr
selected_ifconfig = tk.StringVar()
ifconfigOpts = ttk.Combobox(tab2, textvariable=selected_ifconfig, width=30)    
ifconfigOpts['values'] = ifconfigOptions
ifconfigOpts['state'] = 'readonly'
ifconfigOpts.current(0)
ifconfigOpts.place(relx=.32, rely=0.271)       # place does nothing
ifconfigOpts.bind('<<ComboboxSelected>>', ifconfig_changed)


# netstat
def netstat_changed(_):
    msg = netstatOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


netstatstr = ("i - Show Kernel interface table", "r - Show Kernel routing table", "pnltu - Show active listen ports")

netstatOptions = netstatstr
selected_netstat = tk.StringVar()
netstatOpts = ttk.Combobox(tab2, textvariable=selected_netstat, width=30)    
netstatOpts['values'] = netstatOptions
netstatOpts['state'] = 'readonly'
netstatOpts.current(0)
netstatOpts.place(relx=.32, rely=0.329)       # place does nothing
netstatOpts.bind('<<ComboboxSelected>>', netstat_changed)


# ip
def ip_changed(_):
    msg = ipOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


ipstr = ("address - Show addresses", "link show - Show network devices",
         "neigh - Shows current neighbor table in kernel", "route - Show routing table")

ipOptions = ipstr
selected_ip = tk.StringVar()
ipOpts = ttk.Combobox(tab2, textvariable=selected_ip, width=30)    
ipOpts['values'] = ipOptions
ipOpts['state'] = 'readonly'
ipOpts.current(0)
ipOpts.place(relx=.32, rely=0.386)       # place does nothing
ipOpts.bind('<<ComboboxSelected>>', ip_changed)


# ss
def ss_changed(_):
    msg = ssOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


ssstr = ("-t -a - List TCP sockets", "-u -a - List all UDP sockets")

ssOptions = ssstr
selected_ss = tk.StringVar()
ssOpts = ttk.Combobox(tab2, textvariable=selected_ss, width=30)    
ssOpts['values'] = ssOptions
ssOpts['state'] = 'readonly'
ssOpts.current(0)
ssOpts.place(relx=.32, rely=0.448)       # place does nothing
ssOpts.bind('<<ComboboxSelected>>', ss_changed)


# du
def du_changed(_):
    msg = ssOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


dustr = ("a - Size for directories & files", "s - Summerize all", "S - Size for directories only")

duOptions = dustr
selected_du = tk.StringVar()
duOpts = ttk.Combobox(tab2, textvariable=selected_du, width=30)    
duOpts['values'] = duOptions
duOpts['state'] = 'readonly'
duOpts.current(0)
duOpts.place(relx=.32, rely=0.158)       # place does nothing
duOpts.bind('<<ComboboxSelected>>', du_changed)


# sysctl
def sysctl_changed(_):
    msg = sysctlOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


sysctlstr = ("abi - parameters", "debug - parameters", "dev - parameters", "fs - parameters",
             "kernel - parameters", "net - parameters", "user - parameters")

sysctlOptions = sysctlstr
selected_sysctl = tk.StringVar()
sysctlOpts = ttk.Combobox(tab3, textvariable=selected_sysctl, width=30)    
sysctlOpts['values'] = sysctlOptions
sysctlOpts['state'] = 'readonly'
sysctlOpts.current(0)
sysctlOpts.place(relx=.32, rely=0.850)       # place does nothing
sysctlOpts.bind('<<ComboboxSelected>>', sysctl_changed)


# top
def top_changed(_):
    msg = topOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


topstr = ('U - root', 'U - ' + findme, 'U - daemon')

topOptions = topstr
selected_top = tk.StringVar()
topOpts = ttk.Combobox(tab4, textvariable=selected_top, width=30)    
topOpts['values'] = topOptions
topOpts['state'] = 'readonly'
topOpts.current(0)
topOpts.place(relx=.32, rely=0.278)       # place does nothing
topOpts.bind('<<ComboboxSelected>>', top_changed)


# locate .conf
def locate_changed(_):
    msg = locateOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


# find /usr -type f -name "*.conf"
locatestr = ('@ - etc', '@ - home', '@ - usr', '@ - var')

locateOptions = locatestr
selected_locate = tk.StringVar()
locateOpts = ttk.Combobox(tab4, textvariable=selected_locate, width=30)    
locateOpts['values'] = locateOptions
locateOpts['state'] = 'readonly'
locateOpts.current(0)
locateOpts.place(relx=.32, rely=0.218)       # place does nothing
locateOpts.bind('<<ComboboxSelected>>', locate_changed)


# locate extensions
def locateext_changed(_):
    msg = locateextOpts.get()
    statusbar.config(text=msg)
    statusbar.update()


locateextstr = ('@ - *.bash', '@ - *.bin', '@ - *.bmp', '@ - *.class', '@ - *.cfg',
                '@ - *.cpp', '@ - *.css', '@ - *.csv', '@ - *.efi', '@ - *.gz',
                '@ - *.gif', '@ - *.html', '@ - *.ini', '@ - *.java', '@ - *.jpg',
                '@ - *.js', '@ - *.log', '@ - *.linux', '@ - *.pdf', '@ - *.php',
                '@ - *.pl', '@ - *.png', '@ - *.py', '@ - *.rtf', '@ - *.tiff',
                '@ - *.txt', '@ - *.wav', '@ - *.zip')

locateextOptions = locateextstr
selected_locateext = tk.StringVar()
locateextOpts = ttk.Combobox(tab4, textvariable=selected_locateext, width=30)
locateextOpts['values'] = locateextOptions
locateextOpts['state'] = 'readonly'
locateextOpts.current(0)
locateextOpts.place(relx=.32, rely=0.3368)
locateextOpts.bind('<<ComboboxSelected>>', locateext_changed)


def win_list_changed(_):
    msg = win_listOpts.get()
    statusbar.config(text=msg)
    statusbar.update()
    if msg != "nothing":
        linuxopenfile(global_folder_path + "/" + msg)


win_liststr = global_slist_list

win_listOptions = win_liststr
selected_win_list = tk.StringVar()
win_listOpts = ttk.Combobox(tab7, textvariable=selected_win_list, width=83, height=29)
win_listOpts['values'] = win_listOptions
win_listOpts['state'] = 'readonly'
win_listOpts.focus_set()               # not sure what this is doing
win_listOpts.bind('<Down>')            # not sure what this is doing
win_listOpts.event_generate('<Down>')  # does not work
win_listOpts.current(0)

# win_listOpts.configure(height=30)    # affects the dropdown height
win_listOpts.place(relx=.02, rely=0.040)
win_listOpts.bind('<<ComboboxSelected>>', win_list_changed)


def is_tool(name):
    rc = subprocess.call(['which', name])
    if rc == 0:
        return 'found'
    else:
        return 'not found'


# new combined
def popen_function_common(cmd2):
    cmd2 = cmd2.replace('-@', '')
    cmd = cmd2

    if '*' in cmd2:
        cmd2 = cmd2.replace(' ', '_')
        if '.conf' in cmd2:
            ctxt = cmd2.replace('*', '')
            ctxt = ctxt.replace('.', '')
            ctxt = ctxt.replace('/', '_')
            ctxt = ctxt.replace('__', '_')
            log = open(global_folder_path + '/' + ctxt + '.txt', 'w')
        else:
            if '*' in cmd2:
                cmd2 = cmd2.replace('*', '')
                cmd2 = cmd2.replace('__', '_')
                log = open(global_folder_path + '/' + cmd2 + '.txt', 'w')
            else:
                cmd, opt = cmd2.split('*')
                log = open(global_folder_path + '/' + cmd + ' ' + opt + '.txt', 'w')
    else:
        if ('cpuinfo' in cmd2) or ('os-release' in cmd2) or ('sysctl' in cmd2):
            cmd2 = cmd2.replace(' ', '_')
            cmd2 = cmd2.replace('/', '_')
            cmd2 = cmd2.replace('__', '_')
            log = open(global_folder_path + '/' + cmd2 + '.txt', 'w')
        elif 'dmidecode' in cmd2:
            cmd2 = cmd2.replace('!', ' ')
            # 'dmidecode -t 6!Memory Module'
            x = cmd2.split(" ")
            cmd2 = cmd2.replace(' ', '_')
            log = open(global_folder_path + '/' + cmd2 + '.txt', 'w')
            cmd = x[0] + " " + x[1] + " " + x[2]

        else:
            cmd2 = cmd2.replace(' ', '_')
            cmd2 = cmd2.replace('/', '_')
            cmd2 = cmd2.replace('__', '_')
            log = open(global_folder_path + '/' + cmd2 + '.txt', 'w')

    cmd2 = cmd2.replace('_etc_', ' etc/')
    cmd2 = cmd2.replace('_', ' ')

    if '.conf' not in cmd2:
        cmd = cmd.replace('*', '')

    if 'whoami' not in cmd2 and 'uname' not in cmd2:
        cmd = ('sudo -S ' + cmd)

    proc = subprocess.Popen(cmd.split(), bufsize=1, encoding='UTF-8', errors='ignore',
                            stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    proc.stdin.write(mepaswrd)
    proc.stdin.write('\n')
    proc.stdin.flush()
    stdout = proc.communicate()

    if proc.returncode != 0:
        log.write("\nPopen failed.\n\nWas the password entered correctly?")
        log.flush()
        abouterr("\nPopen failed.\n\nWas the password entered correctly?")

    if proc.returncode == 0:
        counter = 0
        for line in stdout:
            # print(line)     # TEMPORARY
            if ("sysctl" in cmd) and ("grep" in cmd):
                a, b, c, d, e, f, g = cmd.split(' ')
                if (("abi." in line) and ("abi" in g) or ("debug." in line) and ("debug" in g) or
                        ("dev." in line) and ("dev" in g) or ("fs." in line) and ("fs" in g) or
                        ("kernel." in line) and ("kernel" in g) or ("net." in line) and ("net" in g) or
                        ("user." in line) and ("user" in g) or ("vm." in line) and ("vm" in g)):
                    line = line.replace("\x03", "")  # works for the ETX control key
                    line = line.replace("12", "")
                    line = line.replace("   Memory top 5", " : Memory top 5")
                    line2 = ('{:02d}: {}'.format(counter, line))
                    counter = counter + 1
                    log.write(line2)

            else:
                line = line.replace("\x03", "")  # works for the ETX control key
                line = line.replace("12", "")
                line = line.replace("   Memory top 5", " : Memory top 5")
                line2 = ('{:02d}: {}'.format(counter, line))
                counter = counter + 1
                # '01: [sudo] password for whomever: '
                if '[sudo] password' not in line2:
                    log.write(line2)

    proc.terminate()


def popen_function_run(cmd):
    result = is_tool(cmd)

    if result == 'not found':
        abouterr("\nWhoops." + "\n\nCommand '" + cmd + "' appears not to exist.")
    else:
        if 'vlc' in cmd:
            cmd = cmd
        else:
            cmd = 'sudo -S ' + cmd

        proc = subprocess.Popen(cmd.split(), errors='ignore', stdin=PIPE, stdout=PIPE, stderr=PIPE)
        proc.stdin.write(mepaswrd)
        proc.stdin.write('\n')
        proc.stdin.flush()
        proc.communicate()

        if proc.returncode != 0:
            abouterr("\nPopen.\n\nCommand '" + cmd + "' has failed.")

        proc.terminate()


# tab 1 button handlers
def fdisk1():
    popen_function_common('fdisk -l')


def fdisk1b():
    popen_function_common('man fdisk')


def nvidia2():
    msg = nvidiaOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('nvidia-smi -' + resultchoice)


def nvidia2b():
    popen_function_common('man nvidia-smi')


def inxi3():
    msg = inxiOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('inxi -' + resultchoice)


def inxi3b():
    popen_function_common('man inxi')


def dmidecode4():
    msg = dmidecodeOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('dmidecode -t ' + resultchoice + '!' + resultdesc)
    # popen_function_common('dmidecode -t ' + resultchoice)


def dmidecode4b():
    popen_function_common('man dmidecode')


def xinput5():
    msg = xinputOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('xinput --' + resultchoice)


def xinput5b():
    popen_function_common('man xinput')


def df6():
    msg = dfOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('df -' + resultchoice)


def df6b():
    popen_function_common('man df')


def uname7():
    msg = unameOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('uname -' + resultchoice)


def uname7b():
    popen_function_common('man uname')


def hostname8():
    msg = hostnameOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('hostname -' + resultchoice)


def hostname8b():
    popen_function_common('man hostname')


def pip39():
    popen_function_common('pip3 list')


def pip39b():
    popen_function_common('man pip3')


def python310():
    popen_function_common('python3 -V')


def python310b():
    popen_function_common('man python3')


def lpstat11():
    msg = lpstatOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('lpstat -' + resultchoice)


def lpstat11b():
    popen_function_common('man lpstat')


def whoami12():
    popen_function_common('whoami')


def whoami12b():
    popen_function_common('man whoami')


def dpkg13():
    popen_function_common('dpkg -l')


def dpkg13b():
    popen_function_common('man dpkg')


def free14():
    popen_function_common('free -h')


def free14b():
    popen_function_common('man free')


def lshw15():
    popen_function_common('lshw')


def lshw15b():
    popen_function_common('man lshw')


def lspci16():
    popen_function_common('lspci -tv')


def lspci16b():
    popen_function_common('man lspci')


# tab 2 button handlers
def ps21():
    popen_function_common('ps')


def ps21b():
    popen_function_common('man ps')


def pstree22():
    popen_function_common('pstree')


def pstree22b():
    popen_function_common('man pstree')


def du23():
    msg = duOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('du -' + resultchoice)


def du23b():
    popen_function_common('man du')


def lsblk24():
    popen_function_common('lsblk')


def lsblk24b():
    popen_function_common('man lsblk')


def ifconfig25():
    msg = ifconfigOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('ifconfig -' + resultchoice)

    # -a List interfaces available
    # -s Short list


def ifconfig25b():
    popen_function_common('man ifconfig')


def netstat26():
    msg = netstatOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('netstat -' + resultchoice)


def netstat26b():
    popen_function_common('man netstat')


def ip27():
    msg = ipOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('ip ' + resultchoice)


def ip27b():
    popen_function_common('man ip')


def ss28():
    msg = ssOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('ss ' + resultchoice)


def ss28b():
    popen_function_common('man ss')


def lscpu29():
    popen_function_common('lscpu')


def lscpu29b():
    popen_function_common('man lscpu')


def lsusb30():
    popen_function_common('lsusb -tv')


def lsusb30b():
    popen_function_common('man lsusb')


def env31():
    popen_function_common('env ')


def env31b():
    popen_function_common('man env')


def ufw32():
    popen_function_common('ufw status')


def ufw32b():
    popen_function_common('man ufw')


def lspci33():
    popen_function_common('lspci')


def lspci33b():
    popen_function_common('man lspci')


def lsscsi34():
    popen_function_common('lsscsi')


def lsscsi34b():
    popen_function_common('man lsscsi')


def w35():
    popen_function_common('w')


def w35b():
    popen_function_common('man w')


def hwinfo36():
    popen_function_common('hwinfo * --disk')


def hwinfo36b():
    popen_function_common('man hwinfo')


def dmesg37():
    popen_function_common('dmesg')


def dmesg37b():
    popen_function_common('man dmesg')


# tab 3 button handlers
def blkid50():
    popen_function_common('blkid')


def blkid50b():
    popen_function_common('man blkid')


def ps51():
    popen_function_common('ps -au')


def ps51b():
    popen_function_common('man ps')


def findmnt52():
    popen_function_common('findmnt')


def findmnt52b():
    popen_function_common('man findmnt')


def ufw53():
    popen_function_common('ufw status verbose')


def ufw53b():
    popen_function_common('man ufw')


def parted54():
    popen_function_common('parted -l')


def parted54b():
    popen_function_common('man parted')


def who55():
    popen_function_common('who')


def who55b():
    popen_function_common('man who')


def lsb_release56():
    popen_function_common('lsb_release -a')


def lsb_release56b():
    popen_function_common('man lsb_release')


def osrelease57():
    popen_function_common('cat /etc/os-release')


def osrelease57b():
    popen_function_common('man os-release')


def lslogins58():
    popen_function_common('lslogins -u')


def lslogins58b():
    popen_function_common('man lslogins')


def confpaths():
    popen_function_common('cat /home/adroit/.config/user-dirs.dirs')


def confpathsb():
    popen_function_common('man user-dirs.dirs')


def hcitool69():
    popen_function_common('hcitool dev')


def hcitool69b():
    popen_function_common('man hcitool')


def cpuinfo70():
    popen_function_common('cat /proc/cpuinfo')


def cpuinfo70b():
    popen_function_common('man cat')


def sysctl71():
    popen_function_common('cat /etc/sysctl.conf')


def sysctl71b():
    popen_function_common('man cat')


def sysctl72():
    popen_function_common('sysctl -a')


def sysctl72b():
    popen_function_common('man sysctl')


def sysctl73():
    msg = sysctlOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('sysctl -a | grep ' + resultchoice)


def sysctl73b():
    popen_function_common('man sysctl')


def ls74():
    popen_function_common("pip3 list")


def ls74b():
    popen_function_common('man pip3')


# list 4 button handlers
def lsbin70():
    popen_function_common('ls /bin')


def lsbin70b():
    popen_function_common('man ls')


def lsetc71():
    popen_function_common('ls /etc')


def lsetc71b():
    popen_function_common('man ls')


def lssbin72():
    popen_function_common('ls /sbin')


def lssbin72b():
    popen_function_common('man ls')


def listconf73():
    msg = locateOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('find /' + resultdesc + ' -type f -name ' + '*.conf')


def listconf73b():
    popen_function_common('man locate')


def top75():
    msg = topOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('top -b -n1 -U ' + resultdesc)


def top75b():
    popen_function_common('man top')


def locateext75():
    msg = locateextOpts.get()
    resultchoice, resultdesc = msg.split(' - ')
    popen_function_common('locate ' + resultdesc)


def locateext75b():
    popen_function_common('man locate')


# tab 5 run programs
def xed60():
    popen_function_run('xed')


def xed60b():
    popen_function_common('man xed')


def gparted61():
    popen_function_run('gparted')


def gparted61b():
    popen_function_common('man gparted')


def nvidia62():
    popen_function_run('nvidia-settings')


def nvidia62b():
    popen_function_common('man nvidia-settings --help')


def rhythmbox63():
    popen_function_run('rhythmbox')


def rhythmbox63b():
    popen_function_common('man rhythmbox')


def vlc64():
    popen_function_run('vlc')


def vlc64b():
    popen_function_common('man vlc')


def psensor66():
    popen_function_run('psensor')


def psensor66b():
    popen_function_common('man psensor')


def linuxopenfile(cmd):
    os.chmod(cmd, stat.S_IRWXU)
    # subprocess.run(["/usr/bin/xed", cmd], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=FALSE)
    subprocess.Popen(["/usr/bin/xed", cmd])


# TAB 1 TEXT & BUTTONS

# fdisk
text1 = Label(tab1, text="fdisk -l", fg="black", font=("Georgia", 10))
text1.place(x=156, y=25)
text1 = Label(tab1, text="lists disk(s) partition(s) table(s) information", fg="black", font=("Georgia", 10))
text1.place(x=530, y=25)


btn1 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=fdisk1)
btn1.place(x=25, y=20)
btn1b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=fdisk1b)
btn1b.place(x=90, y=20)


# nvidia-smi
text2 = Label(tab1, text="nvidia-smi", fg="black", font=("Georgia", 10))
text2.place(x=156, y=53)
text2 = Label(tab1, text="Nvidia GPU driver or device(s) information", fg="black", font=("Georgia", 10))
text2.place(x=530, y=53)


btn2 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=nvidia2)
btn2.place(x=25, y=50)
btn2b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=nvidia2b)
btn2b.place(x=90, y=50)


# inxi
text3 = Label(tab1, text="inxi", fg="black", font=("Georgia", 10))
text3.place(x=156, y=83)
text3 = Label(tab1, text="GPU / Distro repository information", fg="black", font=("Georgia", 10))
text3.place(x=530, y=83)


btn3 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=inxi3)
btn3.place(x=25, y=80)
btn3b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=inxi3b)
btn3b.place(x=90, y=80)


# dmidecode
text4 = Label(tab1, text="dmidecode -t ", fg="black", font=("Georgia", 10))
text4.place(x=156, y=113)
text4 = Label(tab1, text="List DMI table information", fg="black", font=("Georgia", 10))
text4.place(x=530, y=113)


btn4 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=dmidecode4)
btn4.place(x=25, y=110)
btn4b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=dmidecode4b)
btn4b.place(x=90, y=110)


# xinput
text5 = Label(tab1, text="xinput", fg="black", font=("Georgia", 10))
text5.place(x=156, y=143)
text5 = Label(tab1, text="List of available input devices", fg="black", font=("Georgia", 10))
text5.place(x=530, y=143)


btn5 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=xinput5)
btn5.place(x=25, y=140)
btn5b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=xinput5b)
btn5b.place(x=90, y=140)

# df
text6 = Label(tab1, text="df", fg="black", font=("Georgia", 10))
text6.place(x=156, y=173)
text6 = Label(tab1, text="List file systems", fg="black", font=("Georgia", 10))
text6.place(x=530, y=173)


btn6 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=df6)
btn6.place(x=25, y=170)
btn6b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=df6b)
btn6b.place(x=90, y=170)


# uname
text7 = Label(tab1, text="uname", fg="black", font=("Georgia", 10))
text7.place(x=156, y=202)
text7 = Label(tab1, text="List system information", fg="black", font=("Georgia", 10))
text7.place(x=530, y=202)


btn7 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=uname7)
btn7.place(x=25, y=200)
btn7b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=uname7b)
btn7b.place(x=90, y=200)


# hostname
text8 = Label(tab1, text="hostname", fg="black", font=("Georgia", 10))
text8.place(x=156, y=234)
text8 = Label(tab1, text="My host name or ip address", fg="black", font=("Georgia", 10))
text8.place(x=530, y=234)


btn8 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=hostname8)
btn8.place(x=25, y=230)
btn8b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=hostname8b)
btn8b.place(x=90, y=230)


# pip3
text9 = Label(tab1, text="pip3 list", fg="black", font=("Georgia", 10))
text9.place(x=156, y=263)
text9 = Label(tab1, text="List installed packages", fg="black", font=("Georgia", 10))
text9.place(x=530, y=263)


btn9 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=pip39)
btn9.place(x=25, y=260)
btn9b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=pip39b)
btn9b.place(x=90, y=260)


# python3
text10 = Label(tab1, text="python3 -V", fg="black", font=("Georgia", 10))
text10.place(x=156, y=293)
text10 = Label(tab1, text="Python's version", fg="black", font=("Georgia", 10))
text10.place(x=530, y=293)


btn10 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=python310)
btn10.place(x=25, y=290)
btn10b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=python310b)
btn10b.place(x=90, y=290)


# lpstat
text11 = Label(tab1, text="lpstat", fg="black", font=("Georgia", 10))
text11.place(x=156, y=324)
text11 = Label(tab1, text="Printer info [make sure printer is online]", fg="black", font=("Georgia", 10))
text11.place(x=530, y=324)


btn11 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lpstat11)
btn11.place(x=25, y=320)
btn11b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lpstat11b)
btn11b.place(x=90, y=320)


# whoami
text12 = Label(tab1, text="whoami", fg="black", font=("Georgia", 10))
text12.place(x=156, y=354)
text12 = Label(tab1, text="Who am I", fg="black", font=("Georgia", 10))
text12.place(x=530, y=354)


btn12 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=whoami12)
btn12.place(x=25, y=350)
btn12b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=whoami12b)
btn12b.place(x=90, y=350)


# dpkg
text13 = Label(tab1, text="dpkg -l", fg="black", font=("Georgia", 10))
text13.place(x=156, y=384)
text13 = Label(tab1, text="List all packages", fg="black", font=("Georgia", 10))
text13.place(x=530, y=384)


btn13 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=dpkg13)
btn13.place(x=25, y=380)
btn13b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=dpkg13b)
btn13b.place(x=90, y=380)


# free
text14 = Label(tab1, text="free -h", fg="black", font=("Georgia", 10))
text14.place(x=156, y=414)
text14 = Label(tab1, text="Display free & used memory", fg="black", font=("Georgia", 10))
text14.place(x=530, y=414)


btn14 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=free14)
btn14.place(x=25, y=410)
btn14b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=free14b)
btn14b.place(x=90, y=410)


# lshw
text15 = Label(tab1, text="lshw", fg="black", font=("Georgia", 10))
text15.place(x=156, y=444)
text15 = Label(tab1, text="List all hardware", fg="black", font=("Georgia", 10))
text15.place(x=530, y=444)


btn15 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lshw15)
btn15.place(x=25, y=440)
btn15b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lshw15b)
btn15b.place(x=90, y=440)


# lspci
text16 = Label(tab1, text="lspci -tv", fg="black", font=("Georgia", 10))
text16.place(x=156, y=475)
text16 = Label(tab1, text="List all PCI devices", fg="black", font=("Georgia", 10))
text16.place(x=530, y=475)


btn16 = Button(tab1, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lspci16)
btn16.place(x=25, y=470)
btn16b = Button(tab1, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lspci16b)
btn16b.place(x=90, y=470)


# TAB 2 TEXT & BUTTONS

# ps
text21 = Label(tab2, text="ps", fg="black", font=("Georgia", 10))
text21.place(x=156, y=25)
text21 = Label(tab2, text="List all user processes", fg="black", font=("Georgia", 10))
text21.place(x=530, y=25)


btn21 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ps21)
btn21.place(x=25, y=20)
btn21b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ps21b)
btn21b.place(x=90, y=20)


# pstree
text22 = Label(tab2, text="pstree", fg="black", font=("Georgia", 10))
text22.place(x=156, y=53)
text22 = Label(tab2, text="Show process tree", fg="black", font=("Georgia", 10))
text22.place(x=530, y=53)


btn22 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=pstree22)
btn22.place(x=25, y=50)
btn22b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=pstree22b)
btn22b.place(x=90, y=50)

# du
text23 = Label(tab2, text="du", fg="black", font=("Georgia", 10))
text23.place(x=156, y=83)
text23 = Label(tab2, text="List disk usage in current directory.", fg="black", font=("Georgia", 10))
text23.place(x=530, y=83)


btn23 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=du23)
btn23.place(x=25, y=80)
btn23b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=du23b)
btn23b.place(x=90, y=80)


# lsblk
text24 = Label(tab2, text="lsblk", fg="black", font=("Georgia", 10))
text24.place(x=156, y=113)
text24 = Label(tab2, text="List all block devices", fg="black", font=("Georgia", 10))
text24.place(x=530, y=113)


btn24 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsblk24)
btn24.place(x=25, y=110)
btn24b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsblk24b)
btn24b.place(x=90, y=110)


# ifconfig
text25 = Label(tab2, text="ifconfig", fg="black", font=("Georgia", 10))
text25.place(x=156, y=143)
text25 = Label(tab2, text="Show IP information", fg="black", font=("Georgia", 10))
text25.place(x=530, y=143)


btn25 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ifconfig25)
btn25.place(x=25, y=140)
btn25b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ifconfig25b)
btn25b.place(x=90, y=140)


# netstat
text26 = Label(tab2, text="netstat", fg="black", font=("Georgia", 10))
text26.place(x=156, y=173)
text26 = Label(tab2, text="Kernel interface/routing tables", fg="black", font=("Georgia", 10))
text26.place(x=530, y=173)


btn26 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=netstat26)
btn26.place(x=25, y=170)
btn26b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=netstat26b)
btn26b.place(x=90, y=170)


# ip
text27 = Label(tab2, text="ip", fg="black", font=("Georgia", 10))
text27.place(x=156, y=202)
text27 = Label(tab2, text="Show ip addresses or routing table", fg="black", font=("Georgia", 10))
text27.place(x=530, y=202)


btn27 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ip27)
btn27.place(x=25, y=200)
btn27b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ip27b)
btn27b.place(x=90, y=200)


# ss
text28 = Label(tab2, text="ss", fg="black", font=("Georgia", 10))
text28.place(x=156, y=234)
text28 = Label(tab2, text="Investigate sockets", fg="black", font=("Georgia", 10))
text28.place(x=530, y=234)


btn28 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ss28)
btn28.place(x=25, y=230)
btn28b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ss28b)
btn28b.place(x=90, y=230)


# lscpu
text29 = Label(tab2, text="lscpu", fg="black", font=("Georgia", 10))
text29.place(x=156, y=264)
text29 = Label(tab2, text="Show CPU architecture", fg="black", font=("Georgia", 10))
text29.place(x=530, y=264)


btn29 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lscpu29)
btn29.place(x=25, y=260)
btn29b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lscpu29b)
btn29b.place(x=90, y=260)


# lsusb
text39 = Label(tab2, text="lsusb", fg="black", font=("Georgia", 10))
text39.place(x=156, y=294)
text39 = Label(tab2, text="Show USB devices", fg="black", font=("Georgia", 10))
text39.place(x=530, y=294)


btn30 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsusb30)
btn30.place(x=25, y=290)
btn30b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsusb30b)
btn30b.place(x=90, y=290)


# env
text40 = Label(tab2, text="env", fg="black", font=("Georgia", 10))
text40.place(x=156, y=324)
text40 = Label(tab2, text="Display environmental variables", fg="black", font=("Georgia", 10))
text40.place(x=530, y=324)


btn31 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=env31)
btn31.place(x=25, y=320)
btn31b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=env31b)
btn31b.place(x=90, y=320)


# ufw
text41 = Label(tab2, text="ufw", fg="black", font=("Georgia", 10))
text41.place(x=156, y=354)
text41 = Label(tab2, text="Firewall status", fg="black", font=("Georgia", 10))
text41.place(x=530, y=354)


btn32 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ufw32)
btn32.place(x=25, y=350)
btn32b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ufw32b)
btn32b.place(x=90, y=350)


# lsscsi
text42 = Label(tab2, text="lsscsi", fg="black", font=("Georgia", 10))
text42.place(x=156, y=384)
text42 = Label(tab2, text="List SCSI disks", fg="black", font=("Georgia", 10))
text42.place(x=530, y=384)


btn34 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsscsi34)
btn34.place(x=25, y=380)
btn34b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsscsi34b)
btn34b.place(x=90, y=380)


# w
text43 = Label(tab2, text="w", fg="black", font=("Georgia", 10))
text43.place(x=156, y=414)
text43 = Label(tab2, text="Who is logged in & doing what", fg="black", font=("Georgia", 10))
text43.place(x=530, y=414)


btn35 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=w35)
btn35.place(x=25, y=410)
btn35b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=w35b)
btn35b.place(x=90, y=410)


# hwinfo
text44 = Label(tab2, text="hwinfo --disk", fg="black", font=("Georgia", 10))
text44.place(x=156, y=444)
text44 = Label(tab2, text="Probe for hardware", fg="black", font=("Georgia", 10))
text44.place(x=530, y=444)


btn36 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=hwinfo36)
btn36.place(x=25, y=440)
btn36b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=hwinfo36b)
btn36b.place(x=90, y=440)


# dmesg
text45 = Label(tab2, text="dmesg", fg="black", font=("Georgia", 10))
text45.place(x=156, y=474)
text45 = Label(tab2, text="Display Kernal ring buffer messages", fg="black", font=("Georgia", 10))
text45.place(x=530, y=474)


btn37 = Button(tab2, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=dmesg37)
btn37.place(x=25, y=470)
btn37b = Button(tab2, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=dmesg37b)
btn37b.place(x=90, y=470)


# TAB 3 TEXT & BUTTONS

# blkid
text50 = Label(tab3, text="blkid", fg="black", font=("Georgia", 10))
text50.place(x=156, y=25)
text50 = Label(tab3, text="locate/print block device attributes", fg="black", font=("Georgia", 10))
text50.place(x=530, y=25)


btn50 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=blkid50)
btn50.place(x=25, y=20)
btn50b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=blkid50b)
btn50b.place(x=90, y=20)


# ps
text51 = Label(tab3, text="ps -au", fg="black", font=("Georgia", 10))
text51.place(x=156, y=55)
text51 = Label(tab3, text="Display a list of all users' processes", fg="black", font=("Georgia", 10))
text51.place(x=530, y=55)


btn51 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ps51)
btn51.place(x=25, y=50)
btn51b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ps51b)
btn51b.place(x=90, y=50)


# findmnt
text52 = Label(tab3, text="findmnt", fg="black", font=("Georgia", 10))
text52.place(x=156, y=85)
text52 = Label(tab3, text="List all mounted filesystems", fg="black", font=("Georgia", 10))
text52.place(x=530, y=85)


btn52 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=findmnt52)
btn52.place(x=25, y=80)
btn52b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=findmnt52b)
btn52b.place(x=90, y=80)


# ufw
text53 = Label(tab3, text="ufw", fg="black", font=("Georgia", 10))
text53.place(x=156, y=115)
text53 = Label(tab3, text="Show ufw status verbose", fg="black", font=("Georgia", 10))
text53.place(x=530, y=115)


btn53 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ufw53)
btn53.place(x=25, y=110)
btn53b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ufw53b)
btn53b.place(x=90, y=110)


# parted
text54 = Label(tab3, text="parted", fg="black", font=("Georgia", 10))
text54.place(x=156, y=145)
text54 = Label(tab3, text="Lists partition layout on all block devices", fg="black", font=("Georgia", 10))
text54.place(x=530, y=145)


btn54 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=parted54)
btn54.place(x=25, y=140)
btn54b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=parted54b)
btn54b.place(x=90, y=140)


#  who
text55 = Label(tab3, text="who", fg="black", font=("Georgia", 10))
text55.place(x=156, y=175)
text55 = Label(tab3, text="List uses logged on", fg="black", font=("Georgia", 10))
text55.place(x=530, y=175)


btn55 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=who55)
btn55.place(x=25, y=170)
btn55b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=who55b)
btn55b.place(x=90, y=170)


# lsb_release -a
text56 = Label(tab3, text="lsb_release -a", fg="black", font=("Georgia", 10))
text56.place(x=156, y=205)
text56 = Label(tab3, text="Distribution specific information", fg="black", font=("Georgia", 10))
text56.place(x=530, y=205)


btn56 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsb_release56)
btn56.place(x=25, y=200)
btn56b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsb_release56b)
btn56b.place(x=90, y=200)


# os-release
text57 = Label(tab3, text="os-release", fg="black", font=("Georgia", 10))
text57.place(x=156, y=235)
text57 = Label(tab3, text="Operating system identification", fg="black", font=("Georgia", 10))
text57.place(x=530, y=235)


btn57 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=osrelease57)
btn57.place(x=25, y=230)
btn57b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=osrelease57b)
btn57b.place(x=90, y=230)


# lslogins
text58 = Label(tab3, text="lslogins", fg="black", font=("Georgia", 10))
text58.place(x=156, y=265)
text58 = Label(tab3, text="Show all logins", fg="black", font=("Georgia", 10))
text58.place(x=530, y=265)


btn58 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lslogins58)
btn58.place(x=25, y=260)
btn58b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lslogins58b)
btn58b.place(x=90, y=260)


# ~/.configuser-dirs.dirs  list paths
text69 = Label(tab3, text="cat ~/.config/user-dirs.dirs", fg="black", font=("Georgia", 10))
text69.place(x=156, y=295)
text69 = Label(tab3, text="List system paths", fg="black", font=("Georgia", 10))
text69.place(x=530, y=295)


btn69 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=confpaths)
btn69.place(x=25, y=290)
btn69b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=confpathsb)
btn69b.place(x=90, y=290)


# hcitool
text69 = Label(tab3, text="hcitool", fg="black", font=("Georgia", 10))
text69.place(x=156, y=325)
text69 = Label(tab3, text="Bluetooth connections", fg="black", font=("Georgia", 10))
text69.place(x=530, y=325)


btn69 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=hcitool69)
btn69.place(x=25, y=320)
btn69b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=hcitool69b)
btn69b.place(x=90, y=320)


# cat /proc/cpuinfo.txt
text70 = Label(tab3, text="cat /proc/cpuinfo", fg="black", font=("Georgia", 10))
text70.place(x=156, y=355)
text70 = Label(tab3, text="CPU info all cores", fg="black", font=("Georgia", 10))
text70.place(x=530, y=355)


btn70 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=cpuinfo70)
btn70.place(x=25, y=350)
btn70b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=cpuinfo70b)
btn70b.place(x=90, y=350)


# cat /proc/sysctl.conf
text71 = Label(tab3, text="cat /etc/sysctl.conf", fg="black", font=("Georgia", 10))
text71.place(x=156, y=385)
text71 = Label(tab3, text="Show all system variables", fg="black", font=("Georgia", 10))
text71.place(x=530, y=385)


btn71 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=sysctl71)
btn71.place(x=25, y=380)
btn71b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=sysctl71b)
btn71b.place(x=90, y=380)


# sysctl
text72 = Label(tab3, text="sysctl -a", fg="black", font=("Georgia", 10))
text72.place(x=156, y=415)
text72 = Label(tab3, text="Show all kernel parameters & values", fg="black", font=("Georgia", 10))
text72.place(x=530, y=415)


btn72 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=sysctl72)
btn72.place(x=25, y=410)
btn72b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=sysctl72b)
btn72b.place(x=90, y=410)


# sysctl -a | grep (choice)
text73 = Label(tab3, text="sysctl -a (select)", fg="black", font=("Georgia", 10))
text73.place(x=156, y=445)
text73 = Label(tab3, text="Show all selected parameters & values", fg="black", font=("Georgia", 10))
text73.place(x=530, y=445)


btn73 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=sysctl73)
btn73.place(x=25, y=440)
btn73b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=sysctl73b)
btn73b.place(x=90, y=440)


# ls List installed packages
text74 = Label(tab3, text="list applications", fg="black", font=("Georgia", 10))
text74.place(x=156, y=475)
text74 = Label(tab3, text="List installed application packages & version", fg="black", font=("Georgia", 10))
text74.place(x=530, y=475)


btn74 = Button(tab3, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=ls74)
btn74.place(x=25, y=470)
btn74b = Button(tab3, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=ls74b)
btn74b.place(x=90, y=470)


# TAB 4 TEXT & BUTTON

# ls bin
text70 = Label(tab4, text="ls bin", fg="black", font=("Georgia", 10))
text70.place(x=156, y=25)
text70 = Label(tab4, text="List files in 'bin'", fg="black", font=("Georgia", 10))
text70.place(x=530, y=25)


btn70 = Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsbin70)
btn70.place(x=25, y=20)
btn70b = Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsbin70b)
btn70b.place(x=90, y=20)


# ls etc
text71 = Label(tab4, text="ls etc", fg="black", font=("Georgia", 10))
text71.place(x=156, y=55)
text71 = Label(tab4, text="List files in 'etc'", fg="black", font=("Georgia", 10))
text71.place(x=530, y=55)


btn71 = Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lsetc71)
btn71.place(x=25, y=50)
btn71b = Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lsetc71b)
btn71b.place(x=90, y=50)


# ls sbin
text72 = Label(tab4, text="ls sbin", fg="black", font=("Georgia", 10))
text72.place(x=156, y=85)
text72 = Label(tab4, text="List files in 'sbin'", fg="black", font=("Georgia", 10))
text72.place(x=530, y=85)


btn72 = Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=lssbin72)
btn72.place(x=25, y=80)
btn72b = Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=lssbin72b)
btn72b.place(x=90, y=80)


# list all .conf
text73 = Label(tab4, text="find", fg="black", font=("Georgia", 10))
text73.place(x=156, y=115)
text73 = Label(tab4, text="find '.conf' files", fg="black", font=("Georgia", 10))
text73.place(x=530, y=115)


btn73 = Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=listconf73)
btn73.place(x=25, y=110)
btn73b = Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=listconf73b)
btn73b.place(x=90, y=110)


# top
text75 = Label(tab4, text="top", fg="black", font=("Georgia", 10))
text75.place(x=156, y=145)
text75 = Label(tab4, text="Display Linux processes (once)", fg="black", font=("Georgia", 10))
text75.place(x=530, y=145)


btn75 = Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=top75)
btn75.place(x=25, y=140)
btn75b = Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=top75b)
btn75b.place(x=90, y=140)


# locate extenions
text76 = Label(tab4, text="locate", fg="black", font=("Georgia", 10))
text76.place(x=156, y=175)
text76 = Label(tab4, text="Locate extensions", fg="black", font=("Georgia", 10))
text76.place(x=530, y=175)


btn76 = Button(tab4, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=locateext75)
btn76.place(x=25, y=170)
btn76b = Button(tab4, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=locateext75b)
btn76b.place(x=90, y=170)


# TAB 5 Run & BUTTONS

# xed
text60 = Label(tab5, text="xed", fg="black", font=("Georgia", 10))
text60.place(x=156, y=25)
text60 = Label(tab5, text="Text editor (root)", fg="black", font=("Georgia", 10))
text60.place(x=530, y=25)


btn60 = Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=xed60)
btn60.place(x=25, y=20)
btn60b = Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=xed60b)
btn60b.place(x=90, y=20)


# gparted
text61 = Label(tab5, text="gparted", fg="black", font=("Georgia", 10))
text61.place(x=156, y=55)
text61 = Label(tab5, text="Partition editor (caution)", fg="black", font=("Georgia", 10))
text61.place(x=530, y=55)


btn61 = Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=gparted61)
btn61.place(x=25, y=50)
btn61b = Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=gparted61b)
btn61b.place(x=90, y=50)


# nvidia server settings
text62 = Label(tab5, text="Nvidia", fg="black", font=("Georgia", 10))
text62.place(x=156, y=85)
text62 = Label(tab5, text="Server settings", fg="black", font=("Georgia", 10))
text62.place(x=530, y=85)


btn62 = Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=nvidia62)
btn62.place(x=25, y=80)
btn62b = Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=nvidia62b)
btn62b.place(x=90, y=80)


# rhythmbox
text62 = Label(tab5, text="rhythmbox", fg="black", font=("Georgia", 10))
text62.place(x=156, y=115)
text62 = Label(tab5, text="rhythmbox music player", fg="black", font=("Georgia", 10))
text62.place(x=530, y=115)


btn62 = Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=rhythmbox63)
btn62.place(x=25, y=110)
btn62b = Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=rhythmbox63b)
btn62b.place(x=90, y=110)


# vlc media player
text63 = Label(tab5, text="vlc", fg="black", font=("Georgia", 10))
text63.place(x=156, y=145)
text63 = Label(tab5, text="vlc media player", fg="black", font=("Georgia", 10))
text63.place(x=530, y=145)


btn63 = Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=vlc64)
btn63.place(x=25, y=140)
btn63b = Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=vlc64b)
btn63b.place(x=90, y=140)


# Psensor was tab3
text59 = Label(tab5, text="Psensor", fg="black", font=("Georgia", 10))
text59.place(x=156, y=175)
text59 = Label(tab5, text="Temperature monitoring application", fg="black", font=("Georgia", 10))
text59.place(x=530, y=175)


btn59 = Button(tab5, text="Run", fg='magenta', relief=GROOVE, activeforeground="#00ff00", command=psensor66)
btn59.place(x=25, y=170)
btn59b = Button(tab5, text="Man", fg='darkcyan', relief=GROOVE, activeforeground="#00ff00", command=psensor66b)
btn59b.place(x=90, y=170)


# menus
menubar = Menu(root, bg="#A9A9A9", relief=FLAT)
filemenu = Menu(menubar, tearoff=0)

# filemenu.add_command(label="Open", font=("Georgia", 10), activeforeground="#FF00FF", command=NONE)
filemenu.add_command(label="Exit", font=("Georgia", 10), activeforeground="#FF00FF", command=buttonquithandler)
menubar.add_cascade(label="File", font=("Georgia", 10), activeforeground="#FF00FF", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", font=("Georgia", 10), activeforeground="#FF00FF", menu=editmenu)
editmenu.add_command(label="About", font=("Georgia", 10), activeforeground="#FF00FF", command=openaboutwindow)
editmenu.add_command(label="Notes", font=("Georgia", 10), activeforeground="#FF00FF", command=opennoteswindow)


mintmenu = Menu(menubar, tearoff=0)
menubar.add_command(label="!Mint Forum", font=("Georgia", 10), activeforeground="#FF00FF", command=urlmint)
distrosmenu = Menu(menubar, tearoff=0)
menubar.add_command(label="!Distros Watch", font=("Georgia", 10), activeforeground="#FF00FF", command=urldistros)

whoami = Menu(menubar, tearoff=0)
menubar.add_command(label='   Login name: ' + findme, font=("Georgia", 10), foreground="cyan", command=NONE)

cbrefresh = Menu(menubar, tearoff=0)
menubar.add_command(label=' Refresh combobox ', font=("Georgia", 10), foreground="orange", command=refreshcb)


root.config(menu=menubar)
root.mainloop()
