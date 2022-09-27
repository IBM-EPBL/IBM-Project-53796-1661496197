//Assignment 2:Build a python code,Assume u get temperature and humidity values (generated with random function
to a variable) and write a condition to continuosly detect alarm in case of high temperature//
import random
while(True):
    a=random.randint(10,99)
    b=random.randint(20,99)
    if(a>30 and b>60):
        print("high temperature and humidity of:",a,b,"%","alarm is on")
    elif(a<30 and b<60):
        print("Normal temperature and humidity of:",a,b,"%","alarm is off")
        break
            
