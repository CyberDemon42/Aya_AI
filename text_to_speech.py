import torch
import sounddevice as sd
import time

def speaker(text):


    """
    Озвучивает переданный текст с использованием модели Silero TTS.

    Параметры:text (str): Текст для озвучивания.
    """


    # Конфигурация
    language = 'ru'  # Язык модели (русский)
    model_id = 'ru_v3'  # ID модели Silero TTS
    sample_rate = 48000  # Частота дискретизации
    speaker_name = 'baya'  # Имя диктора: 'aidar', 'baya', 'kseniya', 'xenia', 'random'
    put_accent = True  # Добавлять ли акцент в тексте
    put_yo = True  # Заменять ли "е" на "ё" в тексте
    device = torch.device('cpu')  # Используемый девайс (CPU или GPU)

    # Загрузка модели
    model, _ = torch.hub.load(
        repo_or_dir='snakers4/silero-models',  # Репозиторий модели
        model='silero_tts',  # Имя модели
        language=language,  # Язык
        speaker=model_id  # ID модели
    )
    model.to(device)

    # Генерация аудио из текста
    audio = model.apply_tts(
        text=text,
        speaker=speaker_name,
        sample_rate=sample_rate,
        put_accent=put_accent,
        put_yo=put_yo
    )

    # Воспроизведение озвученного текста
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / sample_rate + 0.5)  # Ждём окончания воспроизведения (с небольшим запасом)
    sd.stop()