# Fator R

Ferramenta de automação para cálculo do Fator R e alteração salarial no sistema Thomas Reuters Domínio - Folha de Pagamento.

## Requisitos

- Python 3.12+
- Windows

## Instalação

```bash
pip install -e .
```

## Uso

Execute o programa:

```bash
python main.py
```

O programa irá solicitando as informações necessárias:
- Código(s) da(s) empresa(s) (separados por vírgula)
- Competência inicial (MM/AAAA)
- Competência final (MM/AAAA)
- Data da alteração salarial (DD/MM/AAAA)

## Dependências

- pyautogui
- pandas
- pillow
- opencv-python
- pyscreeze
- screeninfo
- xlrd