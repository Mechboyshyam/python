import time
# for complete time with hour minute and second
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

# for hour only
hour = int(time.strftime('%H'))
# print(hour)
# for minute only
minute = int(time.strftime('%M'))
# print(minute)
# for second only
second = int(time.strftime('%S'))
# print(second)

if(4>hour<12):
    print("Good Morning Shyam")

elif(12>=hour<17):
    print("Good Afternoon Shyam")

elif(17>=hour<22):
    print("Good Evening Shyam")

else:
    print("Good Night Shyam")    