def number_triangle(n: int) -> str:
    return "\n".join("".join(str(j) for j in range(1, i + 1)) for i in range(1, n + 1))

if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))