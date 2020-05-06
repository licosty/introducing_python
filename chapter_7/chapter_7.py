''' Страница упражнения - 207 '''


import re
import struct
import unicodedata
from binascii import unhexlify

# 1
mystery = '\U0001f4a9'
name = unicodedata.name(mystery)

print(mystery)
print(name)

# 2
pop_bytes = bytes(mystery.encode('utf-8'))
print(f"\n{pop_bytes}")

# 3
pop_string = pop_bytes.decode('utf-8')
print(f"\n{pop_string}")

# 4
poem = '''
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s''' % ('roast beef', 'ham', 'head', 'clam')
print(poem)

# 5
letter = '''
Dear {0[salutation]} {0[name]},
Thank you for your letter. We are sorry that our {0[product]} {0[verbed]} in your {0[room]}. 
Please note that it should never be used in a {0[room]}, especially near any {0[animals]}.
Send us your receipt and {0[amount]} for shipping and handling.
We will send you another {0[product]} that, in our tests, \
is {0[percent]}% less likely to have {0[verbed]}.
Thank you for your support.
Sincerely,
{0[spokesman]}
{0[job_title]}'''

# 6
response = {'salutation': 'lady', 'name': 'Di', 'product': 'banana', 'verbed': 'lay', 'room': 'bedroom',
            'animals': 'cats', 'amount': 'amount', 'percent': 100, 'spokesman': 'Hoba', 'job_title': 'manager'}
print(letter.format(response))

# 7
print()
mammoth = '''
We have seen thee, queen of cheese,
Lying quietly at your ease,
Gently fanned by evening breeze,
Thy fair form no flies dare seize.
All gaily dressed soon you'll go
To the great Provincial show,
To be admired by many a beau
In the city of Toronto.
Cows numerous as a swarm of bees,
Or as the leaves upon the trees,
It did require to make thee please,
And stand unrivalled, queen of cheese.
May you not receive a scar as
We have heard that Mr. Harris
Intends to send you off as far as
The great world's show at Paris.
Of the youth beware of these,
For some of them might rudely squeeze
And bite your cheek, then songs or glees
We could not sing, oh! queen of cheese.
We'rt thou suspended from balloon,
You'd cast a shade even at noon,
Folks would think it was the moon
About to fall and crush them soon.'''

# 8
print(re.findall(r'\bc\w*\b', mammoth))

# 9
print()
print(re.findall(r'c\w{3}\b', mammoth))

# 10
print()
print(re.findall(r'\b\w*r\b', mammoth))

# 11
print()
print(re.findall(r'\b\w*[aeiou]{3}\w*\b', mammoth))

# 12
print()
gif = bytes(unhexlify('47494638396101000100800000000000ffffff21f9' +
            '0401000000002c000000000100010000020144003b'))

# 13
print(gif)

# 14
width, height = struct.unpack('>HH', gif[6:10])
print(width, height)
