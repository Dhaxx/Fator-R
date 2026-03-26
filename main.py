import pyautogui
import time
from PIL import ImageGrab
from pathlib import Path
import shutil

def clicar_imagem(img, tentativas=5, confidence=0.8):
    for i in range(tentativas):
        pos = pyautogui.locateOnScreen(img, confidence=confidence)
        if pos:
            pyautogui.click(pyautogui.center(pos))
            pyautogui.click(pyautogui.center(pos))
            return True
        time.sleep(1)
    return False

# Cria a pasta "Fator R" na raiz do disco onde este script está
pasta_raiz_disco = Path(__file__).resolve().anchor
pasta_fator_r = Path(pasta_raiz_disco) / "Fator R"
pasta_fator_r.mkdir(parents=True, exist_ok=True)

# Limpa todo o conteúdo da pasta "Fator R" (arquivos e subpastas)
for item in pasta_fator_r.iterdir():
    if item.is_dir():
        shutil.rmtree(item)
    else:
        item.unlink()

# Detecta todos os monitores
screenshot = ImageGrab.grab(all_screens=True)
screenshot.save('todos_monitores.png')

empresas = '1104, 1105, 1106'#input("Digite o(s) código(s) (separados por vírgula): ")
dt_inicio = '12/2025'#input("Competência inicial (MM/AAAA): ")
dt_fim = '12/2025'#input("Competência final (MM/AAAA): ")

# chamada da função
if clicar_imagem("favoritos.png"):
    print("Clicou em Favoritos")
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('Relatórios')
    time.sleep(2)
    pyautogui.write('Diversos')
    pyautogui.press('enter')
    pyautogui.write('Cálculo Fator R')
    pyautogui.press('enter')
    time.sleep(2)
    
    clicar_imagem("campo1.png")
    pyautogui.write(empresas)

    pyautogui.press('tab')
    pyautogui.write(dt_inicio)
    pyautogui.press('tab')
    pyautogui.write(dt_fim)

    clicar_imagem("executar1.png")
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(4)
    clicar_imagem("exportar.png")
    pyautogui.press('enter')
    time.sleep(2)
    clicar_imagem("desktop.png")
    clicar_imagem("campo2.png")   
    pyautogui.write(f'Client {pasta_raiz_disco[0]}')
    print(f"Salvando em: Client {pasta_raiz_disco[0]}")
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.doubleClick(pyautogui.locateOnScreen("pasta.png", confidence=0.8))
    clicar_imagem("save.png")
    time.sleep(2)
    pyautogui.press('escape')
else:
    print("Não encontrou a imagem")