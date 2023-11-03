from datetime import date, timedelta


def get_birthdays_per_week(users):
    users_list = {}               # створення списку користувачів
    current_date = date.today()       #
    # current_year = datetime.year      # створення поточного часу
    days_of_week = timedelta(days=7)  #

    if len(users) < 1:                # перевірка на порожній словник
        return {}

    for user in users:
        user_birthday = user["birthday"]  # отртмання ДН користувача

        if user_birthday.month == 1:      # перевіряемо якщо ДН у кінці року, то замінюемо на наступний рік
            user_birthday = user['birthday'].replace(year=current_date.year + 1)
        else:
            user_birthday = user['birthday'].replace(year=current_date.year)  # якщо ні, залишаемо рік без змін

        if user_birthday - current_date > days_of_week or user_birthday < current_date:
            continue    # якщо ДН пройшло або в на наступному тижні, пропускаемо

        if user_birthday.weekday() >= 5:    # якщо ДН у вихідний - переносимо на найближчі будні
            user_birthday += timedelta(days=7 - user_birthday.weekday())
        birthday_weekday = user_birthday.strftime('%A')  # отримуемо назву дня тижня

        if birthday_weekday not in users_list:  # якщо день не зустрічався ще, додаемо йоо до списку
            users_list[birthday_weekday] = []

        users_list[birthday_weekday].append(user["name"])  # додаемо користувача до списку відповідного дня

    return users_list


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": date(2023, 11, 13)},
        {'name': 'Bill', 'birthday': date(2023, 11, 3)},
        {"name": "Janet", "birthday": date(2023, 11, 2)},
        {"name": "Bill Gates", "birthday": date(2023, 11, 28)},
        {'name': 'Jenny', 'birthday': date(2023, 11, 7)},
        {'name': 'Sophiya', 'birthday': date(2023, 11, 5)},
        {'name': 'Johny B', 'birthday': date(2018, 11, 6)},
        {'name': 'Jack D', 'birthday': date(2023, 11, 8)},
        {'name': 'Samanta F', 'birthday': date(2023, 11, 15)},
        {'name': 'Serena T', 'birthday': date(2023, 11, 10)}
    ]

    result = get_birthdays_per_week(users)
    print(result)
