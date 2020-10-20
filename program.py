from menu import Menu
import os

menu = Menu()
menu.mostraMenu()
opcao = input(" Escolha uma opcão: ")
menu.executaOpcao(opcao)
os.system("exit")



