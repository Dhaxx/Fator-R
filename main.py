import pyautogui
import time
from PIL import ImageGrab

def clicar_imagem(img, tentativas=5, confidence=0.8):
    for i in range(tentativas):
        pos = pyautogui.locateOnScreen(img, confidence=confidence)
        if pos:
            pyautogui.click(pyautogui.center(pos))
            pyautogui.click(pyautogui.center(pos))
            return True
        time.sleep(1)
    return False

# Detecta todos os monitores
screenshot = ImageGrab.grab(all_screens=True)
screenshot.save('todos_monitores.png')

empresas = input("Digite o(s) código(s) (separados por vírgula): ")

# chamada da função
if clicar_imagem("favoritos.png"):
    print("Clicou em Favoritos")
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.write('Relatórios')
    time.sleep(2)
    pyautogui.write('Diversos')
    pyautogui.press('enter')
    pyautogui.write('Cálculo Fator R')
    pyautogui.press('enter')
    time.sleep(2)
    
    # Mantem Ctrl e Shift pressionados enquanto envia Right para selecionar.
    # segura Ctrl e Shift
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('right')
else:
    print("Não encontrou a imagem")