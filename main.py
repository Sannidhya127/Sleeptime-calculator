from colored import fg, bg, attr
import re




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
    pass

def SleepForYear():
    pass

def SleepForLife():
    pass








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

    else:
        print(f"{fg('red_1')}Invalid Input{attr('reset')}")