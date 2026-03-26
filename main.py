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

print("===[Variáveis para o Cálculo do Fator R]===")
empresas = '1104, 1105, 1106'#input("Digite o(s) código(s) (separados por vírgula): ")
dt_inicio = '12/2025'#input("Competência inicial (MM/AAAA): ")
dt_fim = '12/2025'#input("Competência final (MM/AAAA): ")

print("===[Variável para a alteração salarial]===")
dt_alteracao = '31/12/2025'#input("Data da alteração salarial (DD/MM/AAAA): ")

# chamada da função
if clicar_imagem("favoritos.png"):
    print("Clicou em Favoritos")
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('Relatórios')
    time.sleep(1)
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
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
    clicar_imagem("exportar.png")
    pyautogui.press('tab')
    pyautogui.press('p')
    time.sleep(2)
    clicar_imagem("export_opt.png")
    time.sleep(2)
    clicar_imagem("desktop.png")
    time.sleep(2)
    clicar_imagem("campo2.png")   
    pyautogui.write(f'Client {pasta_raiz_disco[0]}')
    print(f"Salvando em: Client {pasta_raiz_disco[0]}")
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.doubleClick(pyautogui.locateOnScreen("pasta.png", confidence=0.8))
    time.sleep(1)
    pyautogui.press('tab', presses=2)
    pyautogui.write(f'Fator R - {empresas}')
    clicar_imagem("save.png")
    time.sleep(4)
    clicar_imagem("salvar.png")
    time.sleep(3)
    pyautogui.press('escape')
    pyautogui.press('escape')

    # Inicia segunda etapa do processo Fator R - Alteração Salarial
    clicar_imagem("processos.png")
    pyautogui.press('down', presses=22)
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('enter')

    pyautogui.write(dt_alteracao)
    pyautogui.press('tab')
    pyautogui.write('ALTERACAO')
    pyautogui.press('tab', presses=2)
    pyautogui.press('down')
    pyautogui.press('tab', presses=8)

else:
    print("Não encontrou a imagem")