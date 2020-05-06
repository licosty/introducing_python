''' Страница упражнения - 140 '''

# 1
guess_me = 7
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else:
    print("just right")

# 2
print()
start = 1

while True:
    if start < guess_me:
        print("too low")
    elif start == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    start += 1

# 3
print()
for i in range(3, -1, -1):
    print(i)

# 4
num = [i for i in range(10) if i % 2 == 1]
print(f"\n{num}")

# 5
squares = {key: key**2 for key in range(10)}
print(f"\n{squares}")

# 6
odd = {i for i in range(10) if i % 2 == 0}
print(f"\n{odd}")

# 7
print()
generator = (f"Got: {i}" for i in range(10))
for gen in generator:
    print(gen)

# 8
def good():
    return ["Harry", "Ron", "Hermione"]

# 9
print()
def get_odds():
    for number in range(10):
        if not number % 2:
            yield number
count = 1
for odd in get_odds():
    if count == 3:
        print(odd)
    count += 1

# 10
def test(func):
    def new_function(*args, **kwargs):
        print("start")
        func(*args, **kwargs)
        print("end")
    return new_function

def start_test():
    print("test")

print()
test(start_test)()

# 11
print()
class OopsException(Exception):
    pass
try:
    a = 1
    if a:
        raise OopsException(a)
except OopsException:
    print("Caught an oops")

# 12
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(f"\n{movies}")