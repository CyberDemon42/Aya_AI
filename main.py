import speech_to_text
import gptlocal
import text_to_speech
import call_cmd

def main():

    """
    Главная функция, реализующая режимы работы голосового помощника.
    """
    
    while True:
        # Запрашиваем у пользователя режим работы
        firstinp = input("Выберите режим работы:\n"
                         "1 - Голосовой запрос\n"
                         "2 - Вызов команды\n"
                         "3 - Выход\n"
                         "Ваш выбор: ")

        # Режим 1: Обработка голосового запроса
        if firstinp == '1':
            print("\nНачинаю запись голосового запроса...")
            
            # Распознаем речь пользователя
            query = speech_to_text.recog_speech()
            print(f"Распознанный запрос: {query}")

            # Отправляем запрос в локальный GPT и получаем ответ
            response = gptlocal.request_to_gpt(query)
            print(f"Ответ GPT: {response}")

            # Озвучиваем ответ с помощью синтеза речи
            text_to_speech.speaker(response)

        # Режим 2: Вызов команды
        elif firstinp == '2':
            text_to_speech.speaker("Вы выбрали выполнение команды.")
            call_cmd.call()

        # Режим 3: Выход из программы
        elif firstinp == '3':
            text_to_speech.speaker("Завершаю работу программы. До свидания!")
            print("Программа завершена.")
            break

        # Обработка некорректного ввода
        else:
            text_to_speech.speaker("Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")
            print("Ошибка: введите корректный номер режима (1, 2 или 3).")

if __name__ == "__main__":
    # Запускаем программу
    main()
