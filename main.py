# sum of natural numbers
def func(n):
    iteration = 0
    result = n * (n + 1) / 2
    iteration += 1
    print(f"For input size {n}, iteration is: {iteration}")
    return result

print(func(500))

# constant time complexity: O(1)