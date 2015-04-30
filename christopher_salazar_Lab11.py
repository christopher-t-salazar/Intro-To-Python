# christopher_salazar_Lab11.py
# Name: Christopher Salazar
# Date: 04/29/2015
# This program calculates total prices for repair services.

# Import Modules
import tkinter
import tkinter.messagebox

class RepairGUI:

    def __init__(self):

        #Create Main Window
        self.main_window = tkinter.Tk()

        #Two frames for checkboxes and buttons
        self.check_frame=tkinter.Frame(self.main_window)
        self.button_frame=tkinter.Frame(self.main_window)

        # Create the IntVar Objects for check buttons
        self.cb_OilChange = tkinter.IntVar()
        self.cb_LubeJob = tkinter.IntVar()
        self.cb_Radiator = tkinter.IntVar()
        self.cb_Transmission = tkinter.IntVar()
        self.cb_Inspection = tkinter.IntVar()
        self.cb_Muffler = tkinter.IntVar()
        self.cb_Tire = tkinter.IntVar()

        # Set the intVar objects with value        
        self.cb_OilChange.set(0)
        self.cb_LubeJob.set(0)
        self.cb_Radiator.set(0)
        self.cb_Transmission.set(0)
        self.cb_Inspection.set(0)
        self.cb_Muffler.set(0)
        self.cb_Tire.set(0)

        # Create checkbutton widgets
        self.cb1 = tkinter.Checkbutton(self.check_frame, \
                text='Oil Change - $26.00', variable=self.cb_OilChange)
        self.cb2 = tkinter.Checkbutton(self.check_frame, \
                text='Lube Job - $18.00', variable=self.cb_LubeJob)                 
        self.cb3 = tkinter.Checkbutton(self.check_frame, \
                text='Radiator Flush - $30.00', variable=self.cb_Radiator)
        self.cb4 = tkinter.Checkbutton(self.check_frame, \
                text='Transmission Flush - $80.00', variable=self.cb_Transmission)
        self.cb5 = tkinter.Checkbutton(self.check_frame, \
                text='Inspection - $15.00', variable=self.cb_Inspection)
        self.cb6 = tkinter.Checkbutton(self.check_frame, \
                text='Muffler Replacement - $100.00', variable=self.cb_Muffler)
        self.cb7 = tkinter.Checkbutton(self.check_frame, \
                text='Tire Rotation - $20.00', variable=self.cb_Tire)

        # Pack checkbutton
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Create Calculate and Quit buttons
        self.calc_button=tkinter.Button(self.button_frame, \
                        text='Calculate Charges', command=self.calculate)
        self.quit_button=tkinter.Button(self.button_frame, \
                        text='Quit', command=self.main_window.destroy)

        #pack RadioButtons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        #Pack Frames
        self.check_frame.pack()
        self.button_frame.pack()

        # Determine checkbuttons selected
    def calculate(self):
        self.total_value=0.0
        if self.cb_OilChange.get()==1:
            self.total_value+=26.00
        if self.cb_LubeJob.get()==1:
            self.total_value+=18.00
        if self.cb_Radiator.get()==1:
            self.total_value+=30.00
        if self.cb_Transmission.get()==1:
            self.total_value+=80.00
        if self.cb_Inspection.get()==1:
            self.total_value+=15.00
        if self.cb_Muffler.get()==1:
            self.total_value+=100.00
        if self.cb_Tire.get()==1:
            self.total_value+=20.00
        

        # Display message box
        tkinter.messagebox.showinfo('Total Charges',\
                                    format(self.total_value, '.2f'))

carcharges=RepairGUI()
