"""
Multiplication using divide and conquer
:Input: Two integers x and y
:Output: The product of x and y
time complexity: O(n^log2(3)) ~ O(n^1.585)

T(n) = 3T(n/2) + O(n)
"""

def multiplication(x: int, y: int) -> int:
    if x < 10 or y < 10: # simplication for small numbers
        return x * y
    n = max(len(bin(x)[2:]), len(bin(y)[2:]))
    m = n // 2
    xl, xr = divmod(x, 2 ** m)
    yl, yr = divmod(y, 2 ** m)
    p1 = multiplication(xl, yl)
    p2 = multiplication(xr, yr)
    p3 = multiplication(xl + xr, yl + yr)
    return p1 * 2 ** (2 * m) + (p3-p1-p2) * 2 ** m + p2

print(multiplication(1234, 5678)) # 1234 * 5678 = 7006652