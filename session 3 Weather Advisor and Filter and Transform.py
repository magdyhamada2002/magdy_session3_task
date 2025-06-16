# session 3 task Task: Weather Advisor and Task: Filter and Transform a List
# Weather Advisor
temp = 30
if temp < 10 :
    print("It's a cold day. Stay warm")
elif temp >= 10 and temp <19 :
    print("It's a cool day. Wear a jacket!")
elif temp >= 20 and temp <29 :
    print("It's a warm day. Enjoy the weather!")
else:
    print("It's a hot day. Stay hydrated!")
# Filter and Transform a List
mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
for x in range (len(mylist)):
    if mylist[x] % 3 == 0:
     print(mylist[x])