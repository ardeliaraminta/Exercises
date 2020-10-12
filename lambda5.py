#Q5
# to find the list up to n, it can be change in the place of no 20

fibonacci = lambda num: num if num <= 1 else fibonacci(num - 1) + fibonacci(num - 2);
fibonacci_num= list(map(fibonacci, range(0, 20, 1)));
print(fibonacci_num);