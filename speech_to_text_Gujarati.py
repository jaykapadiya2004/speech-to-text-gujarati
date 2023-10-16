import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()



while(True):

    try:

        with sr.Microphone() as source2 :
            recognizer.adjust_for_ambient_noise(source2, duration = 0.2)
            audio2 = recognizer.listen(source2)
            Mytext = recognizer.recognize_google(audio2 , language="gu-IN")
            Mytext = Mytext.lower()
            print("did you say :",Mytext)
    except sr.RequestError as e :
        print(f"Sorry , I encountered an error {e}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")

            

