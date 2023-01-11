import pyautogui
import time
from ahk import AHK

def wyjeb_ze_spawna():
    sprawdz_marmurek()
    sprawdz_buffy()
    print("LOKALIZUJE NIEBIESKIE GÓWNO")
    ahk.key_down('t')
    time.sleep(3)
    ahk.key_up('t')
    ahk.key_down('f')
    time.sleep(2)
    ahk.key_up('f')
    niebieskiegowno = pyautogui.locateCenterOnScreen("niebieskiegowno.png", confidence=0.80)
    while not niebieskiegowno:
        ahk.key_down('e')
        time.sleep(0.5)
        ahk.key_up('e')
        niebieskiegowno = pyautogui.locateCenterOnScreen("niebieskiegowno.png", confidence=0.80)
    print("NIEBIESKIE GÓWNO ZNALEZIONE")
    pyautogui.moveTo(niebieskiegowno)
    print("WYJEBA ZE SPAWNA")
    ahk.key_down('w')
    time.sleep(4)
    ahk.key_up('w')


def znajdz_i_zbij_metina():
    sprawdz_marmurek()
    sprawdz_buffy()
    print("ZNAJDUJE I ZBIJAM METINA")
    metin = pyautogui.locateCenterOnScreen("metin.png", confidence=0.75)
    while not metin:
        ahk.key_press('e')
        metin = pyautogui.locateCenterOnScreen("metin.png", confidence=0.75)
    print(metin)
    pyautogui.moveTo(metin)
    pozycja_nazwy_metina = pyautogui.position()
    pozycja_metina = pozycja_nazwy_metina[1] +130
    pyautogui.moveTo(pozycja_nazwy_metina[0], pozycja_metina)
    pyautogui.click(button='left')
    metin_opis = pyautogui.locateCenterOnScreen("metin3.png", confidence=0.65)
    while not metin_opis:
        metin_opis = pyautogui.locateCenterOnScreen("metin3.png", confidence=0.65)
    time.sleep(8)

def zbij_fale_przeciwnikow():
    sprawdz_marmurek()
    sprawdz_buffy()
    print("ZBIJAM FALE PRZECIWNIKÓW")
    metin = pyautogui.locateCenterOnScreen("metin.png", confidence=0.65)
    while not metin:
        ahk.key_down('e')
        ahk.key_down('space')
        ahk.key_down('w')
        time.sleep(5)
        ahk.key_up('e')
        ahk.key_down('d')
        time.sleep(6)
        ahk.key_press('2')
        ahk.key_up('d')
        metin = pyautogui.locateCenterOnScreen("metin.png", confidence=0.65)

    ahk.key_up('e')
    ahk.key_up('w')
    ahk.key_up('space')
    print(metin)


def zbij_bossy(nazwa_bossa):
    sprawdz_marmurek()
    sprawdz_buffy()
    print(f"ZBIJAM {nazwa_bossa.upper()}")
    boss = pyautogui.locateCenterOnScreen(f"{nazwa_bossa}.png", confidence=0.65)
    ahk.key_down('space')
    while not boss:
        time.sleep(2)
        ahk.key_press('2')
        boss = pyautogui.locateCenterOnScreen(f"{nazwa_bossa}.png", confidence=0.50)
    while boss:
        ahk.key_down('space')
        ahk.key_down("e")
        ahk.key_down("w")
        boss = pyautogui.locateCenterOnScreen(f"{nazwa_bossa}.png", confidence=0.50)
    ahk.key_up('space')
    ahk.key_up('e')
    ahk.key_up('w')

def zbij_komendantow():
    sprawdz_marmurek()
    sprawdz_buffy()
    print("Zbijam komendantow")
    boss = pyautogui.locateCenterOnScreen("zin.png", confidence=0.65)
    while not boss:
        time.sleep(2)
        ahk.key_press('2')
        boss = pyautogui.locateCenterOnScreen("zin.png", confidence=0.65)
    while boss:
        boss = pyautogui.locateCenterOnScreen("zin.png", confidence=0.65)
        ahk.key_press("2")
        ahk.key_down("space")
        ahk.key_down("e")
        ahk.key_down("w")
        time.sleep(2)
    ahk.key_up('space')
    ahk.key_up('e')
    ahk.key_up('w')
def ponow_wyprawe():
    sprawdz_marmurek()
    sprawdz_buffy()
    print('NAKURWIAM ZNOW')
    przycisk = pyautogui.locateCenterOnScreen(f"ponow_wyprawe.png", confidence=0.75)
    pyautogui.moveTo(przycisk)
    time.sleep(1)
    pyautogui.click(button="left")
def sprawdz_marmurek():
    ahk.key_press("f2")
    ahk.key_press("f5")
    print("Sprawdzam marmurek")

def sprawdz_buffy():
    print("Sprawdzam buffa")
    buff = pyautogui.locateCenterOnScreen("buff.png", confidence=0.65)
    if not buff:
        ahk.key_press("f1")
        print("Zalaczam buffa")

ahk = AHK()
pyautogui.getWindowsWithTitle("Glevia2")[0].activate()
time.sleep(1)

# brak_kluczy = pyautogui.locateCenterOnScreen("f3.png", confidence=0.65)
def lataj_dunga():
    sprawdz_marmurek()
    wyjeb_ze_spawna()
    znajdz_i_zbij_metina()
    zbij_fale_przeciwnikow()
    znajdz_i_zbij_metina()
    zbij_komendantow()
    # ahk.key_up("space")
    # zbij_bossy('komendanci')
    # zbij_bossy('komendanci')
    # ahk.key_press('a')
    time.sleep(3)
    ahk.key_up('space')
    ahk.key_down('t')
    time.sleep(2)
    ahk.key_up('t')
    znajdz_i_zbij_metina()
    zbij_fale_przeciwnikow()
    znajdz_i_zbij_metina()
    zbij_bossy('dowodca')
    znajdz_i_zbij_metina()
    zbij_bossy('smok')
    ahk.key_down('space')
    time.sleep(25)
    ahk.key_up('space')
    print("DUNG ZROBIONY")
    ponow_wyprawe()
while True:
    lataj_dunga()