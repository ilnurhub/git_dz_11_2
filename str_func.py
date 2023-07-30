def upper_str(my_str):
    """
    Функция, принимающая на вход строку и возвращаюшая ее со всеми заглавными буквами
    """
    return my_str.upper()


def capitalize_words(my_str):
    """
    Функция, делающая заглавными первые буквы каждого слова в строке
    """
    return ' '.join(word.capitalize() for word in my_str.split())
