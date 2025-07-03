from src.generators import filter_by_currency_new
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.transaction_reader import open_csv, open_xlsx
from src.utils import open_json
from src.widget import get_date, mask_account_card


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""
    print("Привет!\nДобро пожаловать в программу работы с банковскими транзакциями.")
    file_transactions = []  # список транзакций получаемый из файла
    filtered_file_transactions = []  # отфильтрованный список транзакций
    currency_code = int  # определяется в зависимости от выбранного файла
    user_1 = user_2 = user_3 = user_4 = user_5 = user_6 = "str"  # ввод пользователя
    while user_1 not in ['1', '2', '3']:
        user_1 = input(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
        if user_1 == '1':
            print("Для обработки выбран JSON-файл.\n")
            file_transactions = open_json("data/operations.json")
            currency_code = 1
        elif user_1 == '2':
            print("Для обработки выбран CSV-файл.\n")
            file_transactions = open_csv("data/transactions.csv")
            currency_code = 2
        elif user_1 == '3':
            print("Для обработки выбран XLSX-файл.\n")
            file_transactions = open_xlsx("data/transactions_excel.xlsx")
            currency_code = 2
        else:
            print("Введено неверное значение!")
    while user_2.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
        user_2 = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        if user_2.upper() in ["EXECUTED", "CANCELED", "PENDING"]:
            filtered_file_transactions = filter_by_state(file_transactions, user_2.upper())
        else:
            print(f'Статус операции "{user_2}" недоступен.\n')
    while user_3.lower() not in ["да", "нет"]:
        user_3 = input("Отсортировать операции по дате? Да/Нет\n")
        if user_3.lower() == "да":
            while user_4.lower() not in ["по возрастанию", "по убыванию"]:
                user_4 = input("Отсортировать по возрастанию или по убыванию?\n")
                if user_4.lower() == "по возрастанию":
                    filtered_file_transactions = sort_by_date(filtered_file_transactions)
                elif user_4.lower() == "по убыванию":
                    filtered_file_transactions = sort_by_date(filtered_file_transactions, False)
                else:
                    print("Введено некорректное значение!.\n")
        elif user_3.lower() == "нет":
            break
        else:
            print("Введено некорректное значение!.\n")
    while user_5.lower() not in ["да", "нет"]:
        user_5 = input("Выводить только рублевые транзакции? Да/Нет\n")
        if user_5.lower() == "да":
            code_transaction = "RUB"
            filtered_file_transactions = filter_by_currency_new(
                filtered_file_transactions, code_transaction, currency_code
            )
        elif user_5.lower() == "нет":
            break
        else:
            print("Введено некорректное значение!.\n")
    while user_6.lower() not in ["да", "нет"]:
        user_6 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
        if user_6.lower() == "да":
            user_7 = input("Введите слово для поиска.\n")
            filtered_file_transactions = process_bank_search(filtered_file_transactions, user_7)
        elif user_6.lower() == "нет":
            break
        else:
            print("Введено некорректное значение!.\n")
    if len(filtered_file_transactions) == 0:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации.\n")
    else:
        print("\nРаспечатываю итоговый список транзакций...\n")

        print(f"Всего банковских операций в выборке: {len(filtered_file_transactions)}\n")

        for item in filtered_file_transactions:
            if item.get("description").lower() == "Открытие вклада".lower() and currency_code == 1:
                print(
                    f'{get_date(item["date"])} {item["description"]}\n'
                    f'{mask_account_card(item["to"])}\n'
                    f'Сумма: {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["code"]}\n'
                )
            elif item.get("description").lower() == "Открытие вклада".lower() and currency_code == 2:
                print(
                    f'{get_date(item["date"])} {item["description"]}\n'
                    f'{mask_account_card(item["to"])}\n'
                    f'Сумма: {item["amount"]} {item["currency_code"]}\n'
                )
            elif currency_code == 1:
                print(
                    f'{get_date(item["date"])} {item["description"]}\n'
                    f'{mask_account_card(item["from"])} -> {mask_account_card(item["to"])}\n'
                    f'Сумма: {item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["code"]}\n'
                )
            elif currency_code == 2:
                print(
                    f'{get_date(item["date"])} {item["description"]}\n'
                    f'{mask_account_card(item["from"])} -> {mask_account_card(item["to"])}\n'
                    f'Сумма: {item["amount"]} {item["currency_code"]}\n'
                )


if __name__ == "__main__":
    main()
