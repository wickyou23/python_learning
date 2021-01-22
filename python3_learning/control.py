#####Python Control Statements
#####if-else
# i = 9
# if i % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")



#####if-elseif-elseif
# import datetime

# today_weekday = datetime.datetime.now().weekday()
# if today_weekday == 0:
#     print("Mon")
# elif today_weekday == 1:
#     print("Tue")
# elif today_weekday == 2:
#     print("Wed")
# elif today_weekday == 3:
#     print("Thu")
# elif today_weekday == 4:
#     print("Fri")
# elif today_weekday == 5:
#     print("Sat")
# elif today_weekday == 6:
#     print("Sun")
# else:
#     print("Undefine")



#####Nested if statements
today = "holiday"
back_balance = 25001
if today == "holiday":
    if back_balance > 25000:
        print("Goto shopping")
    else:
        print("Stay at home")
else:
    print("Normal day")