#COUNTDOWN TIMER SIMULATOR
import time

start = int(input("Enter starting number: ---> "))

print("Countdown Started:")
time.sleep(1)

for y in range(start, -1, -1):
      print(y)
      time.sleep(1)

print("\nLiftoff!")
