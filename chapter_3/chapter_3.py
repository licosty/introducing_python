''' Страница упражнения - 98 '''

# 1
years_list = [1991, 1992, 1993, 1994, 1995, 1996]

# 2
print(years_list[3])

# 3
print()
print(years_list[-1])

# 4
things = ["mozzarella", "cinderella", "salmonella"]

# 5
print()
print(things[1].title())
print(things)

# 6
print()
print(things[0].upper())

# 7
print()
things.remove("salmonella")
print(things)

# 8
surprise = ['Groucho', 'Chico', 'Harpo']

# 9
print()
print(surprise[-1].lower()[::-1].title())

# 10
e2f = {'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}

# 11
print()
print(e2f['walrus'])

# 12
f2e = {}
for key, value in e2f.items():
    f2e[value] = key

# 13
print()
print(f2e['chien'])

# 14
print()
print(set(e2f))

# 15
life = {'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}

# 16
print()
print(life.keys())

# 15
print()
print(life['animals'].keys())

# 16
print()
print(life['animals']['cats'])