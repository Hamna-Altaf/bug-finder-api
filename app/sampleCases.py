sample_cases = [
    {
        "language": "python",
        "code": "def is_even(n): return n % 2 == 1",
        "bug_type": "Logical Bug",
        "description": "The function returns True for odd numbers. It should return True for even numbers.",
        "suggestion": "Use `n % 2 == 0` instead."
    },
    {
        "language": "python",
        "code": "if x = 5: print('x is 5')",
        "bug_type": "Syntax Error",
        "description": "Using `=` instead of `==` in condition.",
        "suggestion": "Use `==` to compare values: `if x == 5`."
    },
    {
        "language": "javascript",
        "code": "if (x = 5) { console.log('x is 5'); }",
        "bug_type": "Logical Bug",
        "description": "Assignment `=` is used instead of comparison.",
        "suggestion": "Use `x === 5` or `x == 5` instead."
    },
    {
        "language": "c",
        "code": "#include <stdio.h>\nint main() {\n  int x;\n  if (x == 0) printf(\"Zero\");\n  return 0;\n}",
        "bug_type": "Logical Bug",
        "description": "Variable `x` is used without initialization.",
        "suggestion": "Initialize `x` before using it."
    },
    {
        "language": "python",
        "code": "for i in range(0, len(arr)+1): print(arr[i])",
        "bug_type": "Off-by-One Error",
        "description": "Loop goes out of bounds by accessing index `len(arr)`.",
        "suggestion": "Use `range(len(arr))` or `range(0, len(arr))`."
    },
    {
        "language": "python",
        "code": "def divide(x, y): return x / y",
        "bug_type": "Runtime Error",
        "description": "Division by zero can crash the program.",
        "suggestion": "Check if `y != 0` before dividing."
    }
]
