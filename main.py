from colored import fg, bg, attr
import re
from datetime import date

today = date.today()

def SleepForWeek():
    sleepPerDay = input("Enter number of hours you sleep everyday: ")
    result = re.match("[-+]?\d+$", sleepPerDay)
    if result is not None:
        if int(sleepPerDay) > 24:
            print("Well, I am no fool")
        else:
            print(7*int(sleepPerDay))
    else:       
        print("Probably entered alphabet. Please recheck")
        SleepForWeek()

def SleepForMonth():
    sleepPerDay = input("Enter number of hours you sleep everyday: ")
    result = re.match("[-+]?\d+$", sleepPerDay)
    if result is not None:
        if int(sleepPerDay) > 24:
            print("Well, I am no fool")
        else:
            ThirtyDaysMonths = ["September", "April", "June", "November"]
            ThirtyOneDaysMonths = ["January", "March", "May", "July", "August", "October", "November", "December"]
            dateNow = today.strftime("%B %d, %Y")
            division = dateNow.split(" ")
            month = division[0]
            if month in ThirtyDaysMonths:
                print(30*int(sleepPerDay))

            elif month in ThirtyOneDaysMonths:
                print(31*int(sleepPerDay))
            
            elif month == "February":
                print(28*int(sleepPerDay) + " For non leap year")
                print(29*int(sleepPerDay) + " For leap year")


    else:
        print("Probably entered alphabet. Please recheck")
        SleepForWeek()

def SleepForYear():
    pass

def SleepForLife():
    pass






while True:

    if __name__=='__main__':

        print(f"{fg('green_1')}Sleep Time Calculator\n{attr('reset')}")

        print(f"{fg('green')}To calculate your total sleep time this week press {fg('red_1')}'w'{attr('reset')}\n{fg('green')}To calculate your total sleep time this month press {fg('red_1')}'m'{attr('reset')}\n{fg('green')}To calculate your total sleep time this year press {fg('red_1')}'y'{attr('reset')}\n{fg('green')}To calculate the total sleep time of your life press {fg('red_1')}'l'{attr('reset')}")

        decison = input("\n\n")

        decison = decison.lower()


        if decison == "w":
            SleepForWeek()

        elif decison == "m":
            SleepForMonth()
        
        elif decison == "y":
            SleepForYear()
        
        elif decison == "l":
            SleepForLife()

        elif decison == "exit":
            exit()

        else:
            print(f"{fg('red_1')}Invalid Input{attr('reset')}")