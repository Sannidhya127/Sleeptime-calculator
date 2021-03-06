from colored import fg, bg, attr
import re
from datetime import date

today = date.today()

leapYear = False

def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    leapYear = True
    return True
  # Else it is not a leap year  
  else:  
    leapYear = False
    return True


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
                print(f"{30*int(sleepPerDay)} hours this {month}")

            elif month in ThirtyOneDaysMonths:
                print(f"{31*int(sleepPerDay)} hours this {month}")
            
            elif month == "February":
                dateNow = today.strftime("%B %d, %Y")
                division = dateNow.split(" ")
                year = division[2]
                CheckLeap(year)
                if CheckLeap == True:
                     print(f"{366*int(sleepPerDay)} hours of sleep.")
                elif CheckLeap == False:
                     print(f"{365*int(sleepPerDay)} hours of sleep")

    else:
        print("Probably entered alphabet. Please recheck")
        SleepForWeek()

def SleepForYear():
    sleepPerDay = input("Enter number of hours you sleep everyday: ")
    result = re.match("[-+]?\d+$", sleepPerDay)
    if result is not None:
        if int(sleepPerDay) > 24:
            print("Well, I am no fool")
        else:
            print(f"{365*int(sleepPerDay)} hours For non leap year")
            print(f"{366*int(sleepPerDay)} hours For leap year")


    else:       
        print("Probably entered alphabet. Please recheck")
        SleepForWeek()

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