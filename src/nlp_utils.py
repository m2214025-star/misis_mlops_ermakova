def tokenize(text: str):
    """Разбивает текст на слова, приводя к нижнему регистру"""
    text = text.lower()
    clean_text = ""
    for ch in text:
        if ch.isalnum():  # буквы и цифры оставляем
            clean_text += ch
        else:
            clean_text += " "
    # разбиваем по пробелам и убираем пустые строки
    return [word for word in clean_text.split() if word]


def word_frequencies(text: str):
    """Возвращает частотный словарь слов"""
    words = tokenize(text)
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq




