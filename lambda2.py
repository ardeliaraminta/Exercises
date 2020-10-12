#q2
def multiply_function(n):
  return lambda x : x * n

answer = multiply_function(10)
print(answer(15))
