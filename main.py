from lib import add_numbers, multiply_numbers

def main():
    num1 = 10.0
    num2 = 5.0

    sum_res = add_numbers(num1, num2)
    mult_res = multiply_numbers(num1, num2)

    print(f"Результат додавання {num1} + {num2} = {sum_res}")
    print(f"Результат множення {num1} * {num2} = {mult_res}")

if __name__ == "__main__":
    main()
    