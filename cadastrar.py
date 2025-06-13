import pyautogui as py
from time import sleep
import pandas as pd


py.press('win')
sleep(3)
py.write('opera')
sleep(2)
py.press('enter')
sleep(4)
py.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
py.press('enter')
sleep(4)
py.click(x=653, y=391)
sleep(2)
py.write('automacaosimples@demo.com.br')
sleep(2)
py.press('tab')
py.write('123')
sleep(1.4)
py.press('enter')

tabela = pd.read_csv('produtos.csv')
print(tabela)
sleep(1.4)


for linha in tabela.index:
    py.click(x=737, y=277)
    sleep(2)

    codigo = tabela.loc[linha, 'codigo']
    py.write(codigo)

    py.press('tab')
    marca = tabela.loc[linha, 'marca']
    py.write(marca)

    py.press('tab')
    tipo = tabela.loc[linha, 'tipo']
    py.write(tipo)

    py.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    py.write(categoria)

    py.press('tab')
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    py.write(preco_unitario)

    py.press('tab')
    custo =  str(tabela.loc[linha, 'custo'])
    py.write(custo)

    py.press('tab')
    obs = str(tabela.loc[linha, 'obs'])

    if obs != 'nan':
        py.write(obs)

    py.press('tab')
    py.press('enter')

    py.scroll(10000)  
    sleep(1.4)
