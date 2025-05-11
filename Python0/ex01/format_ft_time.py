import time as time
import datetime as datetime

print("Seconds since January 1, 1970: ", end="")
flag = 0
decimal = 0
power = -2
string = str(time.time())
for idx, num in enumerate(string):
    if flag == 0:
        power += 1
    if num == '.':
        flag = 1
    if idx % 3 == 0 and flag == 0 and idx % 9 != 0:
        print(num, end=",")
    else:
        print(num, end="")
    if flag == 1:
        decimal += 1
    if decimal > 4:
        break
print(" or ", string[0],",",string[1:3], "e+", power, " in scientific notation", sep="")
now = datetime.datetime.now()
month = now.month
year = now.year
day = now.day
match month:
    case 1: print("January", end =' ')
    case 2: print("February", end =' ')
    case 3: print("March", end =' ')
    case 4: print("April", end =' ')
    case 5: print("May", end =' ')
    case 6: print("June", end =' ')
    case 7: print("July", end =' ')
    case 8: print("August", end =' ')
    case 9: print("Septemper", end =' ')
    case 10: print("October", end =' ')
    case 11: print("November", end =' ')
    case 12: print("December", end =' ')
    case _:  print("yo wtf", end =' ')
print(day, year)


