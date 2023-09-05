import collections
import time
import re
import sys

print(sys.path)


text = "My number of the phone is 502 41 62 60 46"

result = re.findall('[0-9]+', text)

print(result)

timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)


numbers = [1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6]

counter = collections.Counter(numbers)
print(counter)
