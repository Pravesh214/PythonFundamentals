#For loop
for i in range(10):
    print("Current value of i is: ", i)

import time
for i in range(1, 6):
    print("Tik Tik", i)
    time.sleep(1)

for i in range(10):
    if(i % 2 == 0):
        continue
    print("Current iteration number", i)
    if(i == 7):
        break

my_list = [2,3,4,5,6]
for item in my_list:
    print("Current Item", item)

my_name = "MasterRav"
for letter in my_name.upper():
    print("Letter Sequence: ", letter)


