import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
s = int(data[1])
a = [int(x) for x in data[2:2 + n]]

left = 0
current_sum = 0
max_len = 0

for right in range(n):
    current_sum += a[right]
    
   
    while current_sum > s and left <= right:
        current_sum -= a[left]
        left += 1
    

    max_len = max(max_len, right - left + 1)

print(max_len)
