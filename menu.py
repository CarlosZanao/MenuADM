import os
class Menu: 
    #Função para mostrar as opções do menu
    def mostraMenu(self):
        #vetor com todas as opçoes do menu
        listaMenu = ["Impressoras","Rede","Opções Acessibilidade","Adicionar Novo Hardware","Adicionar/Remover Programas",
        "Propriedades de Data/Hora","Propriedades de Vídeo","FindFast","Pasta Fontes","Propriedades da Internet","Propriedades do Joystick",
        "Propriedades do Teclado","Microsoft Exchange(ou Windows Messaging)","Microsoft Mail Post Office","Propriedades do Modem",
        "Propriedades do Mouse","Propriedades de Multimídia","Propriedades da Rede","Propriedades de Senha","Placa do PC",
        "Gerenciamento de Energia (Windows 95)","Gerenciamento de Energia (Windows 98)","Pasta Impressoras","Configurações Regionais",
        "Scanners e Câmeras","Propriedades de Som","Propriedades do Sistema","SAIR"]
        #cabeçalho
        print("#################################################################################################")
        print("#                                       MENU ADM                                                #")
        print("#################################################################################################")
        
        #Laço de repetição onde as opçoes são impressas em tela com base no vetor listaMenu
        num = 1
        for x in listaMenu:
            print("  "+str(num) + ") " + x)
            num += 1
        
        print("-------------------------------------------------------------------------------------------------\n")

    #Função que realiza a execução do comando escolhido
    def executaOpcao(self,opcao):
        #Vetor com a lista de comandos onde o indice -1 coresponte ao numero de opção impresso na função listaMenu
        listaOpcoes = ["control printers","control Ncpa.cpl","control access.cpl","control sysdm.cpl add new hardware",
        "control appwiz.cpl","control timedate.cpl","control desk.cpl","control findfast.cpl","control fonts","control inetcpl.cpl",
        "control joy.cpl","control main.cpl keyboard","control mlcfg32.cpl","control wgpocpl.cpl","control modem.cpl","control main.cpl",
        "control mmsys.cpl","control Ncpa.cpl","control password.cpl","control main.cpl pc card (PCMCIA)",
        "control main.cpl power","control powercfg.cpl","control printers","control intl.cpl","control sticpl.cpl",
        "control mmsys.cpl sounds","control sysdm.cpl","exit"]

        #executa a função desejada 
        comando = listaOpcoes[int(opcao)-1]
        os.system(comando)
        
        
        
    