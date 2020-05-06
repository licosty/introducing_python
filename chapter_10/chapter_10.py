''' Страница упражнения - 300 '''

# 1
# today.txt

# 2
import locale
import multiprocessing
import os
import random
import time
from datetime import date, timedelta

with open('today.txt', 'r') as rfile:
    today_string = rfile.read()

# 3
fmt = "%Y-%m-%d %H:%M"
fmt2 = "%Y-%m-%d"
today = time.strptime(today_string, fmt)
print(time.strftime(fmt2, today))

# 4
print(f"\n{os.listdir('.')}")

# 5
print(f"\n{os.listdir('..')}")

# 6
def do_this():
    print()
    print(time.strftime("%H:%M:%S", time.localtime()))


process_2 = multiprocessing.Process(target=do_this)
process_3 = multiprocessing.Process(target=do_this)


if __name__ == "__main__":
    for proc in range(0, 3):
        process = multiprocessing.Process(target=do_this)
        process.start()
        num = random.randint(1, 5)
        time.sleep(num)
        process.terminate()


# 7
birthday = date(1991, 9, 29)

# 8
locale.setlocale(locale.LC_TIME, 'ru_ru')
print(f"\n{date.strftime(birthday, '%A')}")

# 9
day_10_000 = timedelta(days=10_000)
print(f"\n10,000 days after birth: {birthday + day_10_000}")
