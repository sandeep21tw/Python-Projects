# This is a simple program that converts the text to speech

from gtts import gTTS
import os


def main():
    print("\nThis program converts text to speech.")
    print("Either enter the text or type 'f_' for selecting a text file.")
    
    text = input("\nEnter text that you wanna convert to speech: ")
    
    if text == 'f_':
        url = input("\nPlease Enter the full url of the text file: ")
        with open(url, 'r') as f:
            text = f.read()
    

    output = gTTS(text, lang='en', slow=False)
    output.save("speech_test.wav")
    
    # play audio using os
    os.system("speech_test.wav")


main()
