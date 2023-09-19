import calendar
try:
    # taking user from the input
    while True:
        year=int(input("Enter The Year: "))
        print("2023 Calendar")
        for mm in range(1, 13):
            print(calendar.month(year, mm))
            if(mm == 13):
                break
except:
    print("Error ")