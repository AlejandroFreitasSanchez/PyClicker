import threading
import customtkinter
import pyautogui
import time

#variables
running = False

pyautogui.PAUSE = 0.005
#Functions

def run():
    global running
    if running == False:
        try:
            timeSleep = float(timeBeforeStart.get())
            #print("Starting in ",timeSleep," seconds")
            running = True
            time.sleep(timeSleep)
            thread1 = threading.Thread(target=clicks)
            thread1.start()
            #print("Started")
        except:
            #print("Error")
            timeBeforeStart.delete(0, 1000)
            
def stop():
    global running
    if running == True:
        running = False
        #print("Finished")

def clicks():
    global running
    try:
        minuts = float(mins.get())
        secs = float(seconds.get())
        millis = float(milliseconds.get())
        speed = float(minuts * 60 + secs + millis/1000)
        while running == True:
            #print("Click")
            #print(speed)
            if comboBoxClickType.get() == "Double":
                #print(comboBoxClickType.get())
                pyautogui.doubleClick(interval = speed, button = comboBoxMouseButton.get())
            else:
                #print(comboBoxClickType.get())
                pyautogui.click(clicks = 1, interval = speed, button = comboBoxMouseButton.get())
    except:
        mins.delete(0,100)
        seconds.delete(0,100)
        milliseconds.delete(0,100)   
             
def keyEvents(e):
    global running
    if e.char == "q":
        if running == False:
            run()    
        else:
            stop()
          

#Tkinter

#Main window
root = customtkinter.CTk()
root.geometry("320x250")
root.resizable(width = False, height = False)
root.title("AutoClicker")
root.iconbitmap("./Icon/icon.ico")
#Bind functions
root.bind("<KeyPress>",keyEvents)

#widgets
#Start button
botonStart = customtkinter.CTkButton(text = "Start (q)",text_font = ("Sans_Serif",11), command=run)
botonStart.place(x = 25, y = 200, width = 130)
#StopButton
botontStop = customtkinter.CTkButton(text = "Stop (q)",fg_color="red", hover_color="darkred", text_font=("Sans_Serif",11), command=stop)
botontStop.place(x = 160, y = 200, width = 130)
#Speed label
speedLabel = customtkinter.CTkLabel(text = "Click Speed:",text_font = ("Sans_Serif",11))
speedLabel.place(x = -4,y = 30)
#speed values
mins = customtkinter.CTkEntry()
mins.place(x = 160, y = 30, width = 50)
minsLabel= customtkinter.CTkLabel(text="Mins.",text_font=("Sans_Serif",11))
minsLabel.place(x=160, y=1, width=50)
mins.insert(1,0)

seconds = customtkinter.CTkEntry()
seconds.place(x = 205, y=30, width=50)
secondsLabel= customtkinter.CTkLabel(text="Secs.",text_font=("Sans_Serif",11))
secondsLabel.place(x=205, y=1,width=50)
seconds.insert(1,1)

milliseconds = customtkinter.CTkEntry()
milliseconds.place(x = 250, y =30, width=50)
millisLabel= customtkinter.CTkLabel(text="Millis.",text_font=("Sans_Serif",11))
millisLabel.place(x=250, y=1,width=50)
milliseconds.insert(1,0)

#combobox mouse button label
comboBoxLabelMouseButton = customtkinter.CTkLabel(text = "Mouse button:",text_font = ("Sans_Serif",11))
comboBoxLabelMouseButton.place(x = 2, y = 70)
#combobox mouse button
comboBoxMouseButton = customtkinter.CTkComboBox(values=("Left", "Right"))
comboBoxMouseButton.place(x = 160, y = 70)
#combobox click type button label
comboBoxLabelClickType = customtkinter.CTkLabel(text="Click type:",text_font=("Sans_Serif",11))
comboBoxLabelClickType.place(x = -11, y = 110)
#combobox click tupe
comboBoxClickType = customtkinter.CTkComboBox(values=("Single","Double"), variable="none")
comboBoxClickType.place(x = 160, y = 110)
#Entry time before start
timeBeforeStart = customtkinter.CTkEntry()
timeBeforeStart.place(x = 160, y = 150, width = 175)
    #default : 5
timeBeforeStart.insert(1,5)
#time before start label
timeBeforeStartLabel= customtkinter.CTkLabel(text="Time before start:",text_font=("Sans_Serif",11))
timeBeforeStartLabel.place(x = 12, y = 150)

root.mainloop()
