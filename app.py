import pandas as pd

def main():
    # Загружаем данные из data.csv
    data = pd.read_csv('data.csv')

    # Вычисляем среднюю зарплату всех сотрудников
    average_salary = data['salary'].mean()
    print(f"Средняя зарплата: {average_salary:.2f}")

    # Отбираем сотрудников, которым больше 30 лет
    over_30 = data[data['age'] > 30]
    print("\nСотрудники старше 30 лет:")
    print(over_30)

if __name__ == "__main__":
    main()
