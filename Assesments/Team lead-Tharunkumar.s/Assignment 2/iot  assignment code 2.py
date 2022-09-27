temp= int(input("Enter the Temperature value in Celsius:"))
hum=int(input("Enter Humidity Value in % :"))
if(temp>=30):
    n=int(input("Number of times to continue the alert :"))
    for i in range(n):
        print("Alert!!!,Alarm is detected")
else:
    print("The Temperature is Moderate")
