import pyautogui
import time
from PIL import ImageGrab
from pathlib import Path
import shutil
import pandas as pd

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
    df = pd.read_excel(f'{pasta_fator_r}/Fator R - {empresas}.xls', engine='xlrd')
    valores = ((df["valor_faturamento_nfse"] * 0.28) - df["inss_mes_anterior"]).tolist()
    valores_formatados = [f"{v:.2f}".replace(".", ",") for v in valores]
    return valores_formatados


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
empresas = '323,326,327'#input("Digite o(s) código(s) (separados por vírgula): ")
dt_inicio = '12/2025'#input("Competência inicial (MM/AAAA): ")
dt_fim = '12/2025'#input("Competência final (MM/AAAA): ")

print("===[Variável para a alteração salarial]===")
dt_alteracao = '31/12/2026'#input("Data da alteração salarial (DD/MM/AAAA): ")

# chamada da função
if clicar_imagem("favoritos.png"):
    print("Clicou em Favoritos")
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.write('Relatórios')
    time.sleep(2)
    pyautogui.write('Diversos')
    pyautogui.press('enter')
    pyautogui.write('Cálculo Fator R')
    pyautogui.press('enter')
    time.sleep(2)
    
    pyautogui.doubleClick(pyautogui.locateOnScreen("campo1.png", confidence=0.8))
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
    pyautogui.press('enter')
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
    time.sleep(2)
    clicar_imagem("empresas.png")
    time.sleep(0.1)
    # pyautogui.press('enter')                                

    time.sleep(2)

    clicar_imagem("nenhuma.png")
    pyautogui.doubleClick(pyautogui.locateOnScreen("empresa_input.png", confidence=0.8))

    for empresa in empresas.split(','):
        pyautogui.write(empresa.strip())
        pyautogui.press('tab', presses=8)
        pyautogui.hotkey('shift','space')

        for i in range(8):
            pyautogui.hotkey('shift', 'tab')
            time.sleep(0.1) # Aguarda 100ms entre cada tab

        pyautogui.doubleClick(pyautogui.locateOnScreen("empresa_input.png", confidence=0.8))

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
else:
    print("Não encontrou a imagem")