'''
install googletrans:
 pip install googletrans
'''
from googletrans import Translator

def main():
    text = input("Text :")
    dest = input('language :')
    print(t(text, dest))

def t(text , dest):
    try:
        t = Translator()
        detect =f" the language you wrote is  {t.detect(text).confidence*100}% {t.detect(text).lang}"
        translated = t.translate(text, dest=dest).text
        message = f"{detect} \n translation : \n {translated}"
        return (message) 
    except ValueError:
        print("write a valide language please.")
        main()

if __name__ == "__main__":
    main()