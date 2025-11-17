import pyautogui
import time
import random

count = int(input("input jumlah chat : "))
 
print("⏳ Starting bot in 5 seconds...")

for i in range(5, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("✅ Bot started!")

cor = [
    "291",
    "377",
    "464",
    "568",
    "713",
    "800",
    "945"
]

for i in range(count):
    time.sleep(1)
    msg = random.choice(cor)
    pyautogui.click(1582,msg)
    time.sleep(25)
