from fuzzywuzzy import process
import commands
import text_to_speech

def compare(text):


    """
    Функция для сравнения текста с списком команд и поиска лучшего совпадения.

    Параметры:
    text (str): Строка текста, которую необходимо сравнить.
    commands_list (list): Список команд для поиска лучшего совпадения.

    Возвращает:
    Лучшее совпадение в виде строки (команда).
    """


    commands_list = commands.allfn() # Загрузка комманд из файла
    
    try:
        # Используем fuzzywuzzy для нахождения лучшего совпадения
        best_match = process.extractOne(text, commands_list)
        
        # Возвращаем найденное лучшее совпадение
        return best_match[0]

    except Exception as e:
        # Ловим возможные ошибки, если что-то пойдет не так
        text_to_speech.speaker(f"Произошла ошибка при сравнении текста: {e}")
        return None
