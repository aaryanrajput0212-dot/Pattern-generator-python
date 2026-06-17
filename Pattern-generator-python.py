def pyramid(n):
    print("\nNumber Pyramid")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def reverse_pyramid(n):
    print("\nReverse Pyramid")
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def floyd_triangle(n):
    print("\nFloyd's Triangle")
    num = 1

    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1
        print()


def multiplication_triangle(n):
    print("\nMultiplication Triangle")

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print()


def diamond_pattern(n):
    print("\nDiamond Pattern")

    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


while True:

    print("\n" + "=" * 50)
    print("        PATTERN GENERATOR PRO")
    print("=" * 50)

    print("1. Number Pyramid")
    print("2. Reverse Pyramid")
    print("3. Floyd's Triangle")
    print("4. Multiplication Triangle")
    print("5. Diamond Pattern")
    print("6. Exit")

    choice = input("\nSelect Pattern: ")

    if choice == "6":
        print("\nThank you for using Pattern Generator Pro!")
        break

    n = int(input("Enter Size: "))

    if choice == "1":
        pyramid(n)

    elif choice == "2":
        reverse_pyramid(n)

    elif choice == "3":
        floyd_triangle(n)

    elif choice == "4":
        multiplication_triangle(n)

    elif choice == "5":
        diamond_pattern(n)

    else:
        print("Invalid Choice!")