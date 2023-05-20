fibonacci = [0, 1]
n = 5
for i in range(2, n+1):
	num = fibonacci[i-1] + fibonacci[i-2]
	fibonacci.append(num)
	# print(fibonacci)

# print(fibonacci[5])

def fibonacci(n):
	# 기저조건
	if n <= 1:
		return n
	return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))