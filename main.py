from math import degrees
from operator import truediv
from string import whitespace

import cryptography.fernet
from cryptography.fernet import Fernet
import json
import os

from numpy.ma.core import append

def limparTerminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def salvarLogin(data, arquivo='data/login.json'):
    with open(arquivo, 'w') as file:
        json.dump(data, file)
def carregarLogin(arquivo='data/login.json'):
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
def salvarCredenciais(data, arquivo='data/credenciais.json'):
    with open(arquivo, 'w') as file:
        json.dump(data, file)
def carregarArquivos(arquivo='data/credenciais.json'):
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
def verificarLogin(login, nomeUsuario_input, senhaUsuario_input, arquivo='login.json'):
    for login in login:
        if login['nome'] == nomeUsuario_input and login['senha'] == senhaUsuario_input:
            return True
    return False

login = carregarLogin()
credenciais = carregarArquivos()
#inicio do programa
fimScript = 0
while fimScript == 0:
    decisao1 = int(input("Bem vindo ao gerenciador de credenciais! \n 1 - para fazer login \n 2 - para cadastrar \n :"))
    if decisao1 == 1:
        loginCorreto = False
        while loginCorreto == False:
            nomeUsuario = input("Digite seu usuario: ")
            senhaUsuario = input("Digite sua senha: ")
            if verificarLogin(login, nomeUsuario, senhaUsuario):
                print("Login com sucesso!")
                loginCorreto = True
            else:
                print("Nome de usuario ou senha incorretas, tente novamente.")
    if decisao1 == 2:
        nomeUsuario = input("Bem vindo! para iniciar, digite seu nome: ")
        senhaUsuario = input("Digite sua senha: ")
        login.append({'nome': nomeUsuario, 'senha': senhaUsuario})
        salvarLogin(login)

    limparTerminal()

    sairDoPrograma = 5
    while sairDoPrograma == 5:
        #print(f"Bem Vindo! {nomeUsuario} \n Menu: Selecione a opção que deseja!")
        sairDoPrograma = int(input(" 1 - Acesso as suas credenciais salvas \n 2 - Salvar nova credencial \n 3 - Editar credenciais \n 4 - Sair do programa \n :"))
        if sairDoPrograma == 4:
            fimScript = 1
        if sairDoPrograma == 1:
            print("Bem Vindo! estas sao suas credenciais salvas.")
        if sairDoPrograma == 2:
            criarCredencial = 0
            while criarCredencial == 0:
                print("Bem vindo! Aqui voce pode salvar novas credenciais.")
                input()