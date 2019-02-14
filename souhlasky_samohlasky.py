"""Ze vstupního souboru zjistí počet samohlásek a souhlásek."""


with open("text.txt", "r", encoding="utf-8") as f:
    obsah = f.read()

#převod na malá písmena pro jednodušší počítání
text = obsah.lower()


#seznam samohlasek
samohlasky = ["a", "e", "i", "o", "u", "y", "á", "é", "ě", "í", "ó", "ú", "ů", "ý"]
sam = 0

#výpočet samohlásek v textu
for i in text:
    if i in samohlasky:
        sam = sam + 1

print("Počet samohlásek je: ", sam)


#seznam souhlasek
souhlasky = ["b", "c", "d", "f", "g", "h", "ch", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "z", "č", "ď", "ň", "ř", "š", "ť", "ž"]
souh = 0

#výpočet počtu souhlásek v textu
for i in text:
    if i in souhlasky:
        souh = souh + 1

print("Počet souhlásek je: ", souh)
