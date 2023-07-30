def upper_str(text):
    """
    Функция, принимающая на вход строку и возвращаюшая ее со всеми заглавными буквами
    """
    return text.upper()


def capitalize_words(text):
    """
    Функция, делающая заглавными первые буквы каждого слова в строке
    """
    return ' '.join(word.capitalize() for word in text.split())
