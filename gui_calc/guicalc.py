from tkinter import *


#To compile my python file
#Py installer
#Flaticon
#pyinstaller calculator.py

#Empty string to store inputed values
cal=" "

#Functions for the Operations to take place
def press(num):
    global cal
    show_text.delete(1.0,"end")
    cal+=num
    show_text.tag_configure("action2",justify="right")
    show_text.insert(1.0,cal)
    show_text.tag_add("action2",1.0,"end")

def equals():
    global cal
    show_text.delete(1.0,"end")
    answer=eval(cal)
    cal=str(answer)
    show_text.tag_configure("action2",justify="right")
    show_text.insert(1.0,cal)
    show_text.tag_add("action2",1.0,"end")

def delll():
    global cal  
    show_text.delete(1.0,"end")
    cal=cal[0:len(cal)-1]
    show_text.tag_configure("action2",justify="right")
    show_text.insert(1.0,cal)
    show_text.tag_add("action2",1.0,"end")

def cancel():
    global cal
    show_text.delete(1.0,"end")
    cal=" "
    show_text.tag_configure("action2",justify="right")
    show_text.insert(1.0,0)
    show_text.tag_add("action2",1.0,"end")
    
    
#screen 
main_screen=Tk()
main_screen.geometry("390x605")
main_screen.resizable(False,False) # you can aslo use 0,0 43,4
main_screen.title("Calculator")
main_screen.config(bg="#c0c0c0")

# FIRST ROW(standard label)
standard_label=Label(main_screen,text="Standard",font=("Arial",15),bg="#c0c0c0")
standard_label.place(x=50,y=9)

#The text widget
show_text=Text(main_screen,width=23,height=1,bg="#c0c0c0",font=("Arial",19),padx=10,pady=20,bd=0)
show_text.place(x=20,y=60)

# To insert 0 in the text widget
show_text.tag_configure("action1",justify="right")
show_text.insert(1.0,0)
show_text.tag_add("action1",1.0,"end")

#SECOND ROW(MS...)
btn_MC=Button(main_screen,text="MC",width=11,height=1,bg="#c0c0c0",bd=0)
btn_MC.place(x=14,y=150)
btn_MR=Button(main_screen,text="MR",width=11,height=1,bg="#c0c0c0",bd=0)
btn_MR.place(x=106,y=150)
btn_M_add=Button(main_screen,text="M+",width=11,height=1,bg="#c0c0c0",bd=0)
btn_M_add.place(x=198,y=150)
btn_MS=Button(main_screen,text="MS",width=11,height=1,bg="#5865F2",bd=0)
btn_MS.place(x=290,y=150)

# btn_perc=Button(main_screen,text="%",width=10,height=3,bg="#E1D9D1",bd=0)
# btn_perc.place(x=14,y=180)
# btn_CE=Button(main_screen,text="CE",width=10,height=3,bg="#E1D9D1",bd=0)
# btn_CE.place(x=106,y=180)
# btn_C=Button(main_screen,text="C",width=10,height=3,bg="#E1D9D1",bd=0)
# btn_C.place(x=198,y=180)
# btn_Delete=Button(main_screen,text="DEL",width=10,height=3,bg="#E1D9D1",bd=0)
# btn_Delete.place(x=290,y=180)

#ThIRD ROW
btn_perc=Button(main_screen,text="%",width=11,height=4,bg="#E1D9D1",bd=0,command=lambda:press("%"))
btn_perc.place(x=14,y=180)
btn_CE=Button(main_screen,text="CE",width=11,height=4,bg="#E1D9D1",bd=0,command=cancel)
btn_CE.place(x=106,y=180)
btn_C=Button(main_screen,text="C",width=11,height=4,bg="#E1D9D1",bd=0,command=cancel)
btn_C.place(x=198,y=180)
btn_Delete=Button(main_screen,text="DEL",width=11,height=4,bg="#E1D9D1",bd=0,command=delll)
btn_Delete.place(x=290,y=180)

# btn_7=Button(main_screen,text="7",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_7.place(x=14,y=245)
# btn_8=Button(main_screen,text="8",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_8.place(x=106,y=245)
# btn_9=Button(main_screen,text="9",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_9.place(x=198,y=245)
# btn_X=Button(main_screen,text="X",width=10,height=3,bg="#E1D9D1",bd=0)
# btn_X.place(x=290,y=245)

#FOURTH ROW
btn_7=Button(main_screen,text="7",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("7"))
btn_7.place(x=14,y=260)
btn_8=Button(main_screen,text="8",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("8"))
btn_8.place(x=106,y=260)
btn_9=Button(main_screen,text="9",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("9"))
btn_9.place(x=198,y=260)
btn_X=Button(main_screen,text="X",width=11,height=4,bg="#E1D9D1",bd=0,command=lambda:press("*"))
btn_X.place(x=290,y=260)

# btn_4=Button(main_screen,text="4",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_4.place(x=14,y=310)
# btn_5=Button(main_screen,text="5",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_5.place(x=106,y=310)
# btn_6=Button(main_screen,text="6",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_6.place(x=198,y=310)
# btn_subtract=Button(main_screen,text="-",width=10,height=3,bg="#E1D9D1",bd=0)
# btn_subtract.place(x=290,y=310)

#FIFTH ROW
btn_4=Button(main_screen,text="4",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("4"))
btn_4.place(x=14,y=340)
btn_5=Button(main_screen,text="5",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("5"))
btn_5.place(x=106,y=340)
btn_6=Button(main_screen,text="6",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("6"))
btn_6.place(x=198,y=340)
btn_subtract=Button(main_screen,text="-",width=11,height=4,bg="#E1D9D1",bd=0,command=lambda:press("-"))
btn_subtract.place(x=290,y=340)

# btn_1=Button(main_screen,text="1",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_1.place(x=14,y=375)
# btn_2=Button(main_screen,text="2",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_2.place(x=106,y=375)
# btn_3=Button(main_screen,text="3",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_3.place(x=198,y=375)
# btn_addition=Button(main_screen,text="+",width=10,height=3,bg="#E1D9D1",bd=0)
# btn_addition.place(x=290,y=375)

#SiXTH ROW
btn_1=Button(main_screen,text="1",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("1"))
btn_1.place(x=14,y=420)
btn_2=Button(main_screen,text="2",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("2"))
btn_2.place(x=106,y=420)
btn_3=Button(main_screen,text="3",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("3"))
btn_3.place(x=198,y=420)
btn_addition=Button(main_screen,text="+",width=11,height=4,bg="#E1D9D1",bd=0,command=lambda:press("+"))
btn_addition.place(x=290,y=420)

# btn_division=Button(main_screen,text="/",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_division.place(x=14,y=440)
# btn_zero=Button(main_screen,text="0",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_zero.place(x=106,y=440)
# btn_dot=Button(main_screen,text=".",width=10,height=3,bg="#FFFFFF",bd=0)
# btn_dot.place(x=198,y=440)
# btn_equals_to=Button(main_screen,text="=",width=10,height=3,bg="#5865F2",bd=0)
# btn_equals_to.place(x=290,y=440)

#LAST ROW
btn_division=Button(main_screen,text="/",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("/"))
btn_division.place(x=14,y=500)
btn_zero=Button(main_screen,text="0",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("0"))
btn_zero.place(x=106,y=500)
btn_dot=Button(main_screen,text=".",width=11,height=4,bg="#FFFFFF",bd=0,command=lambda:press("."))
btn_dot.place(x=198,y=500)
btn_equals_to=Button(main_screen,text="=",width=11,height=4,bg="#5865F2",bd=0,command=equals)
btn_equals_to.place(x=290,y=500)

#FOR HOLDING THE SCREEN
main_screen.mainloop()