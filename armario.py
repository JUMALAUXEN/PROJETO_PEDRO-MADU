import os
roupas = []

def finalizar_app():
    os.system("clear")  
    print("Finalizando o app\n")

def voltar_menu_principal():
    input("Digite uma tecla para voltar ao menu principal: ")

def mostrar_subtitulo(texto):
    os.system("clear")  
    linha = '-' * len(texto)
    print(linha)
    print(texto)
    print()

def escolher_opcoes():
    mostrar_subtitulo("𝐆𝐮𝐚𝐫𝐝𝐚 𝐫𝐨𝐮𝐩𝐚\n")
    print("1 - Cadastrar roupa")
    print("2 - Listar roupas")
    print("3 - Excluir roupa")
    print("4 - Sair\n")

def opcao_invalida():
    mostrar_subtitulo("Opção inválida\n".ljust(20))
    voltar_menu_principal()

def listar_roupas():
    mostrar_subtitulo('Listando as Roupas'.ljust(20))
    if not roupas:
        print("Nenhuma roupa cadastrada.")
        return
    
    print("Número:".ljust(10), "Nome:".ljust(20), "Modelo:".ljust(20), "Cor:".ljust(15), "Tamanho:".ljust(10))
  
    for i, roupa in enumerate(roupas, start=1):
        nome = roupa['nome']
        modelo = roupa['modelo']
        cor = roupa['cor']
        tamanho = roupa['tamanho']
        print(f'{str(i).ljust(10)} {nome.ljust(20)} {modelo.ljust(20)} {cor.ljust(15)} {tamanho.ljust(10)}')

def cadastrar_nova_roupa():
    nome = input("Digite o nome da roupa: ")
    modelo = input(f'Digite o modelo da roupa {nome}: ')
    cor = input(f'Digite a cor da roupa {nome}: ')
    tamanho = input(f'Digite o tamanho da roupa {nome}: ')
    dados_da_roupa = {'nome': nome, 'modelo': modelo, 'cor': cor, 'tamanho': tamanho}
    roupas.append(dados_da_roupa)
    print(f"Você cadastrou a roupa: {nome}")

def excluir_roupa():
    listar_roupas()
    if not roupas:
        voltar_menu_principal()
        return

    try:
        numero = int(input("Digite o número da roupa que deseja excluir: "))
        if 1 <= numero <= len(roupas):
            roupa_removida = roupas.pop(numero - 1)
            print(f"A roupa '{roupa_removida['nome']}' foi excluída com sucesso.")
        else:
            print("Número inválido. Nenhuma roupa foi excluída.")
    except ValueError:
        print("Digite um número válido.")
    except IndexError:
        print("Número inválido. Nenhuma roupa foi excluída.")

def chamar_nome_do_app():
    print("""𝐆𝐮𝐚𝐫𝐝𝐚 𝐫𝐨𝐮𝐩𝐚""")

def main():
    while True:
        try:
            escolher_opcoes()
            opcao_digitada = int(input("Digite uma opção: "))
            if opcao_digitada == 1:
                print("Você vai cadastrar uma nova roupa\n")
                cadastrar_nova_roupa()
                voltar_menu_principal()
            elif opcao_digitada == 2:
                listar_roupas()
                voltar_menu_principal()
            elif opcao_digitada == 3:
                excluir_roupa()
                voltar_menu_principal()
            elif opcao_digitada == 4:
                print("Você saiu do aplicativo\n")
                finalizar_app()
                break
            else:
                opcao_invalida()
        except ValueError:
            print("Digite um número.")
            voltar_menu_principal()

if __name__ == "__main__":
    chamar_nome_do_app()
    main()


