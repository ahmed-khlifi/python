from googletrans import Translator

def main():
    text = input("\033[1;32;40m Translate your text :")
    dest = input('print language :')
    print(p(text, dest))

def p(text , dest):
    t = Translator()
    detect = t.detect(text)
    return f" the language you wrote is  {detect.confidence*100}% {detect.lang}"
    #return t.translate(text, dest=dest).text

if __name__ == "__main__":
    main()