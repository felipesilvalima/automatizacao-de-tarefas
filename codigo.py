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

pyautogui.PAUSE = 1

# Passo: 1  entrar no sistema da empresa
# abrir o navegador
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")

# entrar no link (https://dlp.hashtagtreinamentos.com\python\intensivao\login)
pyautogui.write("https://dlp.hashtagtreinamentos.com\python\intensivao\login")
pyautogui.press("enter")

time.sleep(2)

# passo 2 fazer loginLogitech   Mouse   1   25.95
pyautogui.click(x=686, y=372)
pyautogui.write("felipesilvalima200@gmail.com")

#passar para campo de senha
pyautogui.press("tab")
pyautogui.write("felipesilva123")

#apertar o botao
pyautogui.click(x=922, y=554)

time.sleep(3)
# passo 3 - importa a base de dados
import pandas

tabe = pandas.read_csv("produtos.csv")

print(tabe)
 
# passo 4 - cadastrar o produto

for linha in tabe.index:
    
    #codigo
    pyautogui.click(x=659, y=252)
    codigo = (str(tabe.loc[linha, "codigo"]))
    pyautogui.write(codigo)

    #marca
    marca = (str(tabe.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(marca)

    #tipo
    tipo = (str(tabe.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(tipo)   

    #categoria
    categoria = (str(tabe.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(categoria)
 

    #preco_unitario
    preco = (str(tabe.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(preco)
    pyautogui.PAUSE = 1
    #custo
    custo = (str(tabe.loc[linha,"custo"]))
    pyautogui.press("tab")  
    pyautogui.PAUSE = 1
    pyautogui.write(custo)
    pyautogui.PAUSE = 1
    #obs
    
    obs = (str(tabe.loc[linha, "obs"]))
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)
    
    #clicar no botao de enviar
    pyautogui.click(x=845, y=917) 
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(2)
    
    pyautogui.scroll(-5000)
    time.sleep(2)

    pyautogui.scroll(5000)