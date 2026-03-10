import sys

data = sys.stdin.read().split()

n = int(data[0])
t = int(data[1])
a = [int(x) for x in data[2:2 + n]]

left = 0
current_sum = 0
max_books = 0

for right in range(n):
    current_sum += a[right]
    
    while current_sum > t and left <= right:
        current_sum -= a[left]
        left += 1
    
    max_books = max(max_books, right - left + 1)

print(max_books)