# Passo: 1  entrar no sistema da empresa
# passo 2 fazer login
# passo 3 pegar importar a base de dados
# passo 4 cadastrar um produto
# passo 5 repetir o passo 4 até cadastrar todos os produtos

import pyautogui
import time

# pyautogui.click - clicar com mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinaçao de teclas exmplo(ctrl + c)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# Passo: 1  entrar no sistema da empresa
# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link (https://dlp.hashtagtreinamentos.com\python\intensivao\login)
pyautogui.write("https://dlp.hashtagtreinamentos.com\python\intensivao\login")
pyautogui.press("enter")

time.sleep(2)

# passo 2 fazer loginLogitech   Mouse   1   25.95
pyautogui.click(x=414, y=451)
pyautogui.write("felipe Mouse")

#passar para campo de senha


#apertar o botao
pyautogui.click(x=962, y=542)

time.sleep(3)
# passo 3 - importa a base de dados
import pandas

tb = pandas.read_csv("produtos.csv")

print(tb)
 
# passo 4 - cadastrar o produto

for linha in tb.index:
    
    #codigo
    pyautogui.click(x=659, y=252)
    codigo = str(tb.loc[linha, "codigo"])
    pyautogui.write(codigo)

    #marca
    marca = str(tb.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    #tipo
    tipo = str(tb.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)   

    #categoria
    categoria = str(tb.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    #preco_unitario
    preco = str(tb.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    #custo
    custo = str(tb.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    #obs
    
    obs = str(tb.loc[linha, "obs"])
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)
    
    #clicar no botao de enviar
    pyautogui.click(x=877, y=905) 
    pyautogui.click(x=877, y=905) 
    time.sleep(1)
    
    pyautogui.scroll(-5000)
    time.sleep(1)

    pyautogui.scroll(5000)