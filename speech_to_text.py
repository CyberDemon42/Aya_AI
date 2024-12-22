import vosk
import sys
import sounddevice as sd
import queue
import json
import text_to_speech

def recog_speech():


    """
    Функция распознавания речи с использованием Vosk.
    Возвращает текст, распознанный из аудио.
    """


    # Настройки модели и аудиовхода
    model_path = "model-small-ru"  # Путь к модели Vosk
    sample_rate = 16000  # Частота дискретизации (оптимально от 8k до 16k)
    device_index = 16  # Индекс устройства записи (микрофон)

    # Инициализация модели
    model = vosk.Model(model_path)
    audio_queue = queue.Queue()  # Очередь для передачи аудио данных между потоками

    def audio_callback(indata, frames, time, status):

        """
        Колбэк для записи аудио с помощью sounddevice.
        """

        if status:
            text_to_speech.speaker(f"Ошибка аудио входа: {status}", file=sys.stderr)
        audio_queue.put(bytes(indata))

    # Приветствие перед началом прослушивания
    text_to_speech.speaker("Я слушаю")

    # Настройка потока для записи аудио
    with sd.RawInputStream(samplerate=sample_rate, blocksize=12000, device=device_index, 
                           dtype='int16', channels=1, callback=audio_callback):
        recognizer = vosk.KaldiRecognizer(model, sample_rate)  # Создание объекта распознавания

        while True:
            # Получаем данные из очереди
            audio_data = audio_queue.get()

            # Проверяем, распознана ли полная фраза
            if recognizer.AcceptWaveform(audio_data):
                # Извлекаем текст из результата
                result = json.loads(recognizer.Result())  # Преобразуем результат в словарь
                text = result.get("text", "")  # Получаем распознанный текст
                return text
#            else:
#                print(recognizer.PartialResult())