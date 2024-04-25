def calculate_score(name, age, gender="unknown", height=None, weight=None, scores=[]):
    """
    Розраховує загальний рейтинг користувача.

    Args:
        name (str): Ім'я користувача.
        age (int): Вік користувача.
        gender (str, optional): Стать користувача. За замовчуванням "unknown".
        height (int, optional): Зріст користувача.
        weight (int, optional): Вага користувача.
        scores (list or dict, optional): Список або словник з оцінками користувача.

    Returns:
        int: Загальний рейтинг користувача.
    """

    if not scores:
        raise ValueError("Необхідно надати список або словник з оцінками")

    total_score = sum(scores.values() if isinstance(scores, dict) else scores)
    is_adult = age >= 18

    print(f"Ім'я: {name}")
    print(f"Вік: {age}")
    print(f"Стать: {gender}")
    if height:
        print(f"Зріст: {height}")
    if weight:
        print(f"Вага: {weight}")
    print(f"Загальний рейтинг: {total_score}")
    print(f"Повнолітній: {is_adult}")

    return total_score

# Приклад використання
calculate_score("John", 25, scores=[85, 90, 75, 88, 92])
calculate_score("Jane", 30, gender="Female", height=170, weight=65, scores={"math": 95, "physics": 80, "chemistry": 77})
