def time24hr(a):
    amorpm = a[5:]
    hr= a[:2]
    h = int(hr)
    min = a[3:5]
    m = int(min)
    if h<=12 and m<=59:
        if amorpm == 'am' or amorpm == 'AM':
            if h==12:
                print("00"+""+min+"hr")
            else:
                print(hr+""+min+"hr")
        elif amorpm == 'pm' or amorpm == 'PM':
            if h==12:
                print(hr+""+min+"hr")
            else:
                print(str(h+12)+""+min+"hr")
        else:
            print("Invalid time")
    else:
        print("Invalid time")
a = input("Enter time = ")
time24hr(a)
