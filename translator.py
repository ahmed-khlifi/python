from googletrans import Translator
from colorama import Fore


def main():
    text = input(Fore.BLUE + "Translate your text :")
    dest = input(Fore.BLUE + 'print language :')
    print(t(text, dest))

def t(text , dest):
    try:
        t = Translator()
        detect = Fore.WHITE + f" the language you wrote is  {t.detect(text).confidence*100}% {t.detect(text).lang}"
        translated = t.translate(text, dest=dest).text
        message = f"{detect} \n translation : \n {translated}"
        return (message) 
    except ValueError:
        print("write a valide language please.")
        main()

if __name__ == "__main__":
    main()