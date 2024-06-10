def bank(X, Y):
    deposit = X  # Начальный вклад пользователя
    interest_rate = 0.10  # Годовая процентная ставка

    for _ in range(Y):
        deposit += deposit * interest_rate  # Увеличиваем вклад на проценты

    return deposit

# Пример использования функции
X = 1000  # Начальная сумма вклада
Y = 5     # Срок вклада в годах
result = bank(X, Y)
print("Сумма на счету спустя", Y, "лет будет равна", round(result, 2), "рублей")