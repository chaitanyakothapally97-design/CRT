def right_triangle(n: int) -> str:
    return "\n".join("*" * i for i in range(1, n + 1))

if __name__ == "__main__":
    n = int(input())
    print(right_triangle(n))