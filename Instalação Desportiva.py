import time, winsound, os
from datetime import datetime


# é o titulo inicial do programa
print("-"*72)
titulo="seja bem vindo ao programa controle de acesso ás instalações desportivas"
print(titulo.upper())
data = str(datetime.now())
print(f'DATA DO SISTEMA:{data}')
time.sleep(1)
print("-"*72)

fichas_dos_atletas=[]


def cadastrar_Atletas():

    while True:
        nome = input("Digite o nome do atleta: ")
        if len(nome) == 1 or nome == "":
            print("..................")
            print("Nome invalido!--> (tente nome com > 1 caracter e !null)")
            print("..................")

        # verificar si a somente letras
        else:
            for i in range(len(nome)):
                if (ord(nome[i])) in range(65, 91) or (ord(nome[i])) in range(97, 123)\
                        or (ord(nome[i])) in range(191, 256):
                    continue
                else:
                    print("Nome só pode conter letras ou hífens")
                    break
            if (ord(nome[i])) in range(65, 91) or (ord(nome[i])) in range(97, 123) \
                    or (ord(nome[i])) in range(191, 256):
                break

    while True:
        numero_de_BI = (input("Digite o numero de BI do atleta: "))
        if numero_de_BI == "" or int(len(numero_de_BI)) > 6 or int(len(numero_de_BI)) < 6:
            print("Numero de BI ínvalido tem que tem 6 digitos!")
        # verificar si a somente numeros
        else:
            for i in range(len(numero_de_BI)):
                if(ord(numero_de_BI [ i ]) in range(48,58)):
                    continue

                else:
                    print("Numero BI Invalido,so pode conter numeros!")
                    break
            if(ord(numero_de_BI[i]) in range(48,58)):
                int(numero_de_BI)
                break

    while True:
        morada=input("Digite a morada do atleta: ")
        if len(morada) == 1 or morada == "":
           print("..................")
           print("morada invalida!")
           print("..................")
        elif morada != '':
            print(f'{morada} morada aceite!')
            break

    while True:
        # prazo de validade definida 3meses ~~~92dias
        ano = input("entre com o ano do atestado medico")
        mes = input("entre com o mês do atestado medico")
        dia = input("entre com o dia do atestado medico")
        data_do_atestado = datetime(int(ano), int(mes), int(dia))
        agora = datetime.now()
        data_de_validade_do_atestado_medico = agora - data_do_atestado
        if int(data_de_validade_do_atestado_medico.days) > 92:
            print("data do Atestado medico invalido pazo max 92 dias!")
        else:
            print(f"Acesso garatido data do atestado esta valido!{data_de_validade_do_atestado_medico}<{92}")
            break

    contacto_telefonico = input("Digite o contacto telefonico do Atleta:")
    desporto = input("Digite o desporto que desejas praticar?")

    ficha_do_atleta = {
        'nome': nome,
        'numero_de_BI': numero_de_BI,
        'morada':  morada,
        'data_de_validade_do_atestado_medico': data_de_validade_do_atestado_medico,
        'contacto_telefonico': contacto_telefonico,
        'desporto': desporto
    }

    fichas_dos_atletas.append(ficha_do_atleta)
    print("Atleta cadastrado com sucesso!")


def lista_atletas():
    print("Ficha dos Atletas")
    print("nome ".center(15), end="")
    print("numero_de_BI".center(16), end="")
    print("morada ".center(12), end="")
    print("data_de_validade_do_atestado_medico ".center(8), end="")
    print("contacto_telefonico ".center(30), end="")
    print("desporto".center(22))

    for atletas in fichas_dos_atletas:
        print(str(atletas['nome']).center(14), end='')
        print(str(atletas['numero_de_BI']).center(16), end='')
        print(str(atletas['morada']).center(12), end='')
        print(str(atletas['data_de_validade_do_atestado_medico']).center(25), end='')
        print(str(atletas['contacto_telefonico']).center(50), end="")
        print(str(atletas['desporto']).center(1))

    nome_arquivo = "estalacao.txt"
    if os.path.exists(nome_arquivo):

        arquivo = open(nome_arquivo, 'w+t', encoding="utf-8")
        arquivo.write(str("Ficha dos Atletas"))
        arquivo.write(str(str("nome ")).center(15))
        arquivo.write(str(str("numero_de_BI ")).center(15))
        arquivo.write(str(str("morada ")).center(15))
        arquivo.write(str(str("data_de_validade_do_atestado_medico ")).center(15))
        arquivo.write(str(str(" contacto_telefonico")).center(15))
        arquivo.write(str(str("desporto ")).center(15))

        for atleta in fichas_dos_atletas:

            arquivo.write(str(+"\n"+atleta['nome']+"\n").center(14))
            arquivo.write(str(atleta['numero_de_BI']).center(14))
            arquivo.write(str(atleta['morada']).center(14))
            arquivo.write(str(atleta['data_de_validade_do_atestado_medico']).center(14))
            arquivo.write(str(atleta['contacto_telefonico']).center(14))
            arquivo.write(str(atleta['desporto']).center(14))
            arquivo.close()


def mostrar_menu():
    print("...Actividades desportivas disponiveis...")
    print("1-Futebol,atletismo,Voleibol,Ciclismo,Canoagem,Basketball\n0-Sair\n")


def ficha_menu():
    print("...Menu Acesso...")
    print("1-CADASTRAR ATLETAS\n2-MOSTRAR A FICHA DO DIRIGENTE DESPORTIVO\n0-Sair")


while True:
    mostrar_menu()
    acesso_desportivo = int(input("Escolha o tipo de desporto que desejas praticar!"))
    if acesso_desportivo == 1:
        while True:
            print("Acesso a estalação desportiva")
            time.sleep(0.5)
            print("Aviso tecnico Para desporto digite Futebol,atletismo,Voleibol,Ciclismo,Canoagem,Basketball"
                  .upper())
            winsound.Beep(1000, 500)
            time.sleep(0.5)
            ficha_menu()
            opcao_do_sistema = int(input("Escolha uma opcao do sistema!"))
            if opcao_do_sistema == 1:
                cadastrar_Atletas()
            elif opcao_do_sistema == 2:
                if len(fichas_dos_atletas) > 0:
                    lista_atletas()
                else:
                    print("Não há atletas na lista do dirigente,tente por favor! cadastrar Atletas")
            elif opcao_do_sistema == 0:
                print("saindo do Menu do sistema...")
                break
            else:
                print("opcao invalida,tente{1-2-0}!")

    elif acesso_desportivo == 0:
        print("Saindo do sistema.....")
        exit()
    else:
        print("Acesso desportivo invalido!")
