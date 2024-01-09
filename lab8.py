# Your task is very simple here: write a program that uses a for loop to "count mississippi" to five.
#  Having counted to five,
# the program should print to the screen the final message "Ready or not, here I come!"
import time
#Start code below this line:
for x in range(1, 6):
    print(x, "Mississippi")
    time.sleep(1)
print("Ready or not, here I come!")