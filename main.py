import pyautogui
import time
from pathlib import Path
import shutil
import pandas as pd
from PIL import ImageGrab
from screeninfo import get_monitors

def clicar_imagem(img, tentativas=5, confidence=0.8):
    for i in range(tentativas):
        pos = pyautogui.locateOnScreen(img, confidence=confidence)
        if pos:
            pyautogui.click(pyautogui.center(pos))
            pyautogui.click(pyautogui.center(pos))
            return True
        time.sleep(1)
    return False

def gerar_novos_salarios():
    df = pd.read_excel(f'{pasta_fator_r}/Fator R - {empresas}.xls', engine='xlrd').sort_values('geempre_nome_emp').reset_index(drop=True)
    valores = ((df["valor_faturamento_nfse"] * 0.28) - df["inss_mes_anterior"]).tolist()
    valores_formatados = [f"{v:.2f}".replace(".", ",") for v in valores]
    return valores_formatados

def ir_para_lateral_esquerda(img, confidence=0.5, offset_x=10, offset_y=440):

    # captura todos os monitores
    screenshot = ImageGrab.grab(all_screens=True)

    # tenta localizar a imagem
    pos = pyautogui.locate(img, screenshot, confidence=confidence)

    if not pos:
        print(f"[ERRO] Imagem não encontrada: {img}")
        return False

    x, y = pyautogui.center(pos)

    # pega info dos monitores
    monitors = get_monitors()

    # origem global do screenshot
    min_x = min(m.x for m in monitors)
    min_y = min(m.y for m in monitors)

    # corrige coordenadas
    real_x = x + min_x
    real_y = y + min_y

    # encontra o monitor correto
    monitor_atual = None
    for m in monitors:
        if (m.x <= real_x <= m.x + m.width) and (m.y <= real_y <= m.y + m.height):
            monitor_atual = m
            break

    if not monitor_atual:
        print("[ERRO] Monitor não identificado")
        return False

    # move para lateral esquerda do monitor
    destino_x = monitor_atual.x + offset_x
    destino_y = monitor_atual.y + offset_y

    pyautogui.moveTo(destino_x, destino_y)
    return True

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

print("===[Variáveis para o Cálculo do Fator R]===")
empresas = input("Digite o(s) código(s) (separados por vírgula): ")
dt_inicio = input("Competência inicial (MM/AAAA): ")
dt_fim = input("Competência final (MM/AAAA): ")

print("===[Variável para a alteração salarial]===")
dt_alteracao = input("Data da alteração salarial (DD/MM/AAAA): ")

# chamada da função
pyautogui.hotkey('win', 'down')
time.sleep(1)
pyautogui.hotkey('alt', 'r', 'up')
# pyautogui.press('up')
time.sleep(0.5)
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('Relatórios')
time.sleep(2)
pyautogui.write('Diversos')
pyautogui.press('enter')
pyautogui.write('Cálculo Fator R')
pyautogui.press('enter')
time.sleep(2)

pyautogui.press('delete', presses=20)
pyautogui.write(empresas)

pyautogui.press('tab')
pyautogui.write(dt_inicio)
pyautogui.press('tab')
pyautogui.write(dt_fim)

pyautogui.press('tab', presses=3)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)  

ir_para_lateral_esquerda("logo.png", confidence=0.5)
pyautogui.click()
time.sleep(1)

pyautogui.press('enter')
pyautogui.press('p')
time.sleep(1)

pos = pyautogui.locateOnScreen("salvar_relatorio.png", confidence=0.5)
pyautogui.moveTo(pos.left + 360, pos.top + 80)
pyautogui.click()
pyautogui.press('enter')

time.sleep(2)
pyautogui.press('tab', presses=4, interval=0.5)
pyautogui.press('down')
time.sleep(0.5)
pyautogui.press('down')
pyautogui.write(f'Client {pasta_raiz_disco[0]}')
print(f"Salvando em: Client {pasta_raiz_disco[0]}")
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('tab', presses=3)
time.sleep(0.2)
pyautogui.write('Fator R')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('tab', presses=2, interval=0.5)
pyautogui.write(f'Fator R - {empresas}.xls')
pyautogui.press('tab', presses=2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.press('p')
pyautogui.press('tab')
time.sleep(0.2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('escape')
pyautogui.press('escape')

# Inicia segunda etapa do processo Fator R - Alteração Salarial
pyautogui.hotkey('alt', 'p')
time.sleep(0.5)
pyautogui.press('up', presses=10)
pyautogui.press('right')
pyautogui.press('down')
pyautogui.press('enter')

pyautogui.write(dt_alteracao)
pyautogui.press('tab')
pyautogui.write('ALTERACAO')
pyautogui.press('tab', presses=2)
pyautogui.press('down')
time.sleep(1)

for i in range(6):
    pyautogui.hotkey('shift', 'tab')
    time.sleep(0.1) # Aguarda 100ms entre cada tab
time.sleep(0.1)
pyautogui.press('enter')                                

time.sleep(2)

pyautogui.press('tab', presses=6, interval=0.1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('tab', presses=6, interval=0.1)

for empresa in empresas.split(','):
    pyautogui.write(empresa.strip())
    pyautogui.press('tab', presses=8)
    pyautogui.hotkey('shift','space')

    for i in range(8):
        pyautogui.hotkey('shift', 'tab')
        time.sleep(0.1) # Aguarda 100ms entre cada tab

    pyautogui.press('backspace', presses=20)

pyautogui.press('tab')
pyautogui.press('enter')

for i in range(2):
    pyautogui.hotkey('shift', 'tab')
    time.sleep(0.1) # Aguarda 100ms entre cada tab

pyautogui.press('enter')
pyautogui.press('enter')
time.sleep(2)

valores = gerar_novos_salarios()

for valor in valores:
    pyautogui.write(str(valor))
    pyautogui.press('tab')