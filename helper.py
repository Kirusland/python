import pyaudio
import speech_recognition as sr

r = sr.Recognizer()

while True:
    with sr.Microphone(device_index=1) as source:
        print("Скажите что-нибудь ...")
        audio = r.listen(source)

    speech = r.recognize_google(audio, language="ru_RU").lower()
    print("Вы сказали: " + speech)

    if speech == "привет":
        print("Привет")
    elif speech == "пока":
        print("До свидания")
        break
    else:
        print("Я вас не понимаю, повторите пожалуйста")
