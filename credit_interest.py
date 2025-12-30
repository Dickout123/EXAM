def calculate_interest(amount: float, annual_rate: float) -> float:
    if amount < 0:
        raise ValueError("Сума кредиту не може бути від’ємною")

    if annual_rate < 0:
        raise ValueError("Річна процентна ставка не може бути від’ємною")

    return amount * (annual_rate / 100)


def main():
    try:
        amount = float(input("Введіть суму кредиту: "))
        annual_rate = float(input("Введіть річну процентну ставку (%): "))

        interest = calculate_interest(amount, annual_rate)

        print(f"Річні відсотки за кредитом: {interest:.2f}")

    except ValueError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()
