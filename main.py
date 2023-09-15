import datetime
import pyautogui
import time

data_alvo = datetime.date(2073, 18, 15)
lista = ['']

# Obtém a data atual
data_atual = datetime.date.today()

# Verifica se a data atual é igual à data alvo
if data_atual == data_alvo:

    # aq tu vai preencher os dados essenciais
    destino = lista
    assunto = "teste123"
    msg = "teste321"

    #func bot
    pyautogui.press('win')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('https://mail.google.com/mail/u/0/#inbox?compose=new')
    pyautogui.press('enter')
    time.sleep(5)

    # n mexa no contador
    for i in lista:
        pyautogui.write(lista)
        pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(assunto)
    pyautogui.press('tab')
    pyautogui.write(msg)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'enter')
