from googletrans import Translator
from colorama import Fore
def main():
    text = input(Fore.BLUE + "Translate your text :")
    dest = input(Fore.BLUE + 'print language :')
    print(p(text, dest))

def p(text , dest):
    t = Translator()
    detect = Fore.WHITE + f" the language you wrote is  {t.detect(text).confidence*100}% {t.detect(text).lang}"
    translated = t.translate(text, dest=dest).text
    message = f"{detect} \n translation : \n {translated}"
    return (message) 

if __name__ == "__main__":
    main()