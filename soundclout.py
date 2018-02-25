import Tkinter as tk
import tkFont as tkfont

# THIS CODE IS WRITTEN IN PYTHON 2.7

class Soundclout(tk.Tk):    # this class is the controller for our overall app

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is a stack of frames
        # on top of each other, then the one we want visible
        # will be placed above the others
        container = tk.Frame(self)
        container.pack()
        container.grid_rowconfigure(0, weight=1)        # weight is 1 so
        container.grid_columnconfigure(0, weight=1)     # components can resize

        self.frames = {}
        for F in (Home, DeviceTester, EditGroupBehavior):    # be sure to list all the classes here
            page_name = F.__name__
            frame = F(parent=container, controller=self)    # soundclout class controls everything
            self.frames[page_name] = frame                  # so all app-wide variables go in here

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Home")                     # show home on start, obviously

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class Home(tk.Frame):       # home screen of our app

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Button(self, text="Home", bg="lightblue")
        label.grid(row=0, column=0, sticky="nw") # label in top left corner

        # these are all the buttons for the different pages you can go to
        button1 = tk.Button(self, text="Start", fg="blue", bg="green", width=20)
        button2 = tk.Button(self, text="Device Tester",
                            command=lambda: controller.show_frame("DeviceTester"), width=20, bg="lightblue")
        button3 = tk.Button(self, text="Connect Devices",
                            command=lambda: controller.show_frame("ConnectDevices"), width=20, bg="lightblue")
        button4 = tk.Button(self, text="Edit Device Groups",
                            command=lambda: controller.show_frame("EditDeviceGroups"), width=20, bg="lightblue")
        button5 = tk.Button(self, text="Edit Group Behavior",
                            command=lambda: controller.show_frame("EditGroupBehavior"), width=20, bg="lightblue")
        button1.grid(row=3, column=2, pady=5, padx=20, columnspan=2)
        button2.grid(row=4, column=2, pady=5, padx=20, columnspan=2)
        button3.grid(row=5, column=2, pady=5, padx=20, columnspan=2)
        button4.grid(row=6, column=2, pady=5, padx=20, columnspan=2)
        button5.grid(row=7, column=2, pady=5, padx=20, columnspan=2)

        # spacer in between buttons and connected devices
        spacer = tk.Frame(self, width=75)
        spacer.grid(row=0, column=3, rowspan=6)

        # this section displays the connected devices
        devicelabel = tk.Label(self, text="Connected Devices")
        devicelabel.grid(column=4, row=3, padx=50, stick="nsew")
        conncteddevs = tk.Message(self, text="testing", width=150, bg="gray")
        conncteddevs.grid(column=4, row=4)
        # using the message widget we can create a list of the connected devices that
        # updates appropriately using a function we need to make in the main app class

#---------------------These are the subsequent screens----------------------

class DeviceTester(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # name the screen
        label = tk.Label(self, text="Device Tester")
        label.grid(column=3, row=0, sticky="ew", columnspan=3)

        # setting up the home button
        homebutton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"), bg="lightblue")
        homebutton.grid(row=0, column=0, sticky="nw")

        # the test devices window
        button1 = tk.Button(self, text="Test Device", bg="lightblue", width=20)
        button1.grid(row=3, column=2, pady=5, padx=20, columnspan=2)
        # need to make a scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(sticky="e", column=3)
        connecteddevs = tk.Listbox(self, yscrollcommand=scrollbar.set)
        connecteddevs.grid(row=4, column=2, padx=20, pady=10, columnspan=2)
        scrollbar.config(command=connecteddevs.yview)
        # This is how you populate the connected devices list
        for item in ["one", "two", "three", "four"]:
            connecteddevs.insert("end", item)
        # We should populate it with a list of connected device names
        # each time this page is loaded we all need to clear the old list with
        # delete(0, END)
        # You can refer to the active, or selected, item with the keyword "active"

        # the device information window
        infolabel = tk.Label(self, text="Device Information")
        infolabel.grid(row=3, column=5, padx=20, pady=10, columnspan=2)

class ConnectDevices(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # name the screen
        label = tk.Label(self, text="Connect Devices")
        label.grid(column=3, row=0, sticky="ew", columnspan=3)

        # setting up the home button
        homebutton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"), bg="lightblue")
        homebutton.grid(row=0, column=0, sticky="nw")

        # scan button
        button1 = tk.Button(self, text="Scan", bg="lightblue", width=6)
        button1.grid(row=3, column=1, pady=5, padx=20, columnspan=2)
        # scam button
        button2 = tk.Button(self, text="Connect", bg="lightblue", width=6)
        button2.grid(row=3, column=3, pady=10, padx=0, columnspan=2)

        # need to make a scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(sticky="e", column=3)
        connecteddevs = tk.Listbox(self, yscrollcommand=scrollbar.set)
        connecteddevs.grid(row=4, column=2, padx=20, pady=10, columnspan=2)
        scrollbar.config(command=connecteddevs.yview)
        # This is how you populate the connected devices list
        for item in ["one", "two", "three", "four"]:
            connecteddevs.insert("end", item)
        # We should populate it with a list of connected device names
        # each time this page is loaded we all need to clear the old list with
        # delete(0, END)
        # You can refer to the active, or selected, item with the keyword "active"

        # the device information window
        infolabel = tk.Label(self, text="Device Information")
        infolabel.grid(row=3, column=5, padx=20, pady=10, columnspan=2)

class EditDeviceGroups(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # name the screen
        label = tk.Label(self, text="Edit Device Groups")
        label.grid(column=3, row=0, sticky="ew", columnspan=3)

        # setting up the home button
        homebutton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"), bg="lightblue")
        homebutton.grid(row=0, column=0, sticky="nw")

        # the test devices window
        button1 = tk.Button(self, text="Test Device", bg="lightblue", width=20)
        button1.grid(row=3, column=2, pady=5, padx=20, columnspan=2)
        # need to make a scrollbar
        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(sticky="e", column=3)
        connecteddevs = tk.Listbox(self, yscrollcommand=scrollbar.set)
        connecteddevs.grid(row=4, column=2, padx=20, pady=10, columnspan=2)
        scrollbar.config(command=connecteddevs.yview)
        # This is how you populate the connected devices list
        for item in ["one", "two", "three", "four"]:
            connecteddevs.insert("end", item)
        # We should populate it with a list of connected device names
        # each time this page is loaded we all need to clear the old list with
        # delete(0, END)
        # You can refer to the active, or selected, item with the keyword "active"

        # the device information window
        infolabel = tk.Label(self, text="Device Information")
        infolabel.grid(row=3, column=5, padx=20, pady=10, columnspan=2)

class EditGroupBehavior(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # name the screen
        label = tk.Label(self, text="Edit Group Behavior")
        label.grid(column=3, row=0, sticky="ew")

        # setting up the home button
        homebutton = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("Home"), bg="lightblue")
        homebutton.grid(row=0, column=0, sticky="nw")

        # Selecting a group
        select = tk.Label(self, text="Select Group:")
        select.grid(row=2, column=2, pady=10)
        scrollbar = tk.Scrollbar(self)
        scrollbar.grid(sticky="w", column=4, row=2)
        groupselect = tk.Listbox(self, yscrollcommand=scrollbar.set, width=20, height=2)
        groupselect.grid(row=2, column=3, sticky="nsew", pady=10, padx=5)
        scrollbar.config(command=groupselect.yview)
        for item in ["one", "two", "three", "four", "five", "six"]:
            groupselect.insert("end", item)
        # We should populate it with a list of connected device names
        # each time this page is loaded we all need to clear the old list with
        # delete(0, END)
        # You can refer to the active, or selected, item with the keyword "active"

        # Setting overall time length
        overlabel = tk.Label(self, text="Set Overall Time Length")
        overlabel.grid(row=3, column=3, pady=10, sticky="nsew")
        overall = tk.IntVar()        # keep track of this selection with integers
        tk.Radiobutton(self, text="Set", variable=overall, value=1).grid(row=4, column=3, sticky="w")
        tk.Radiobutton(self, text="Range", variable=overall, value=2).grid(row=4, column=3, sticky="e")
        tk.Label(self, text="Between ").grid(row=5, column=2)
        tk.Label(self, text=" And ").grid(row=5, column=3)
        tk.Label(self, text=" Minutes").grid(row=5, column=5)
        overallentry1 = tk.StringVar()      # Variables that keep track of the text
        overallentry2 = tk.StringVar()      # field entries
        overallval1 = tk.Entry(self, textvariable=overallentry1, width=3)
        overallval2 = tk.Entry(self, textvariable=overallentry2, width=3)
        overallval1.grid(row=5, column=3, columnspan=2, sticky="w")
        overallval2.grid(row=5, column=3, columnspan=2, sticky="e")

        # Setting the event time length
        eventlabel = tk.Label(self, text="Set Event Time Length")
        eventlabel.grid(row=6, column=3, pady=10, sticky="nsew")
        eventlength = tk.IntVar()        # keep track of this selection with integers
        tk.Radiobutton(self, text="Set", variable=eventlength, value=1).grid(row=7, column=3, sticky="w")
        tk.Radiobutton(self, text="Range", variable=eventlength, value=2).grid(row=7, column=3, sticky="e")
        tk.Label(self, text="Between ").grid(row=8, column=2)
        tk.Label(self, text=" And ").grid(row=8, column=3)
        tk.Label(self, text=" Minutes").grid(row=8, column=5)
        evententry1 = tk.StringVar()      # Variables that keep track of the text
        evententry2 = tk.StringVar()      # field entries
        eventval1 = tk.Entry(self, textvariable=evententry1, width=3)
        eventval2 = tk.Entry(self, textvariable=evententry2, width=3)
        eventval1.grid(row=8, column=3, columnspan=2, sticky="w")
        eventval2.grid(row=8, column=3, columnspan=2, sticky="e")

        # Setting the event amounts
        amountlabel = tk.Label(self, text="Set Amount of Events")
        amountlabel.grid(row=9, column=3, pady=10, sticky="nsew")
        amountrange = tk.IntVar()        # keep track of this selection with integers
        tk.Radiobutton(self, text="Set", variable=amountrange, value=1).grid(row=10, column=3, sticky="w")
        tk.Radiobutton(self, text="Range", variable=amountrange, value=2).grid(row=10, column=3, sticky="e")
        tk.Label(self, text="Between ").grid(row=11, column=2)
        tk.Label(self, text=" And ").grid(row=11, column=3)
        tk.Label(self, text=" Events").grid(row=11, column=5)
        amountentry1 = tk.StringVar()      # Variables that keep track of the text
        amountentry2 = tk.StringVar()      # field entries
        amountval1 = tk.Entry(self, textvariable=amountentry1, width=3)
        amountval2 = tk.Entry(self, textvariable=amountentry2, width=3)
        amountval1.grid(row=11, column=3, columnspan=2, sticky="w")
        amountval2.grid(row=11, column=3, columnspan=2, sticky="e")

#---------------------This is the main method (duh)----------------------

if __name__ == "__main__":
    app = Soundclout()
    #frame = tk.Frame(app, width=1024, height=768)  # create a window around the app
    #frame.pack()                                   # of the designated size (but this size is too big)
    app.mainloop()