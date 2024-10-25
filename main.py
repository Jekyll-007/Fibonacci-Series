def fibonacci_series(n):
    series = []
    if n < 1:
        return series
    elif n == 1:
        return [0]
    series = [0, 1]
    while len(series) < n:
        next_term = series[-1] + series[-2]
        series.append(next_term)
    return series

num_terms = int(input("Enter the number of terms for the Fibonacci Series: "))
result = fibonacci_series(num_terms)
print("Fibonacci series up to", num_terms,"terms:", result)    