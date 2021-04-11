# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
result = max(sum(int(s) for s in str(n**i)) for n in range(1,100) for i in range(1, 100))
print(result)