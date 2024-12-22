import subprocess
import text_to_speech

def execute(cmd):


    """
    Функция для выполнения команд в shell.
    
    Параметры:
    cmd (str): строка, содержащая команду для выполнения в shell.

    Возвращает:
    subprocess.CompletedProcess: объект с результатом выполнения команды.
    """

    
    try:
        # Выполняем команду в shell с параметрами по умолчанию (без перенаправления вывода)
        result = subprocess.run(cmd, shell=True)
        
        # Если команда выполнена успешно, возвращаем результат
        text_to_speech.speaker(f"Команда выполнена успешно: {cmd}")
        return result

    except subprocess.CalledProcessError as e:
        # Если команда вернула ошибку, выводим ошибку
        text_to_speech.speaker(f"Ошибка выполнения команды: {cmd}")
        text_to_speech.speaker(f"Ошибка: {e}")
        return e

    except Exception as e:
        # Ловим другие возможные ошибки
        text_to_speech.speaker(f"Произошла ошибка: {str(e)}")
        return e
