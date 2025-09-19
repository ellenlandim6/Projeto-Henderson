from colorama import Fore, init 
from pyfiglet import Figlet
from tqdm import tqdm
import time

init(autoreset=True) 

agenda = {
    "Família": [],
    "Amigos": [],
    "Trabalho": []
}

def mostrar_titulo(): 
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText("Agenda"))

def carregando(msg): 
    for _ in tqdm(range(30), desc=msg, ncols=60):
        time.sleep(0.1)

def mostrar_menu():
    print(Fore.YELLOW + "\n---MENU---")
    print("1. Adicionar contato")
    print("2. Listar contatos por categoria")
    print("3. Buscar contato (nome ou telefone)")
    print("4. Sair") 

def adicionar_contato():  
    print("Categorias: Família, Amigos, Trabalho")
    categoria = input("Digite a categoria: ").capitalize()

    if categoria in agenda:
        nome = input("Nome do contato: ")
        telefone = input("Telefone do contato: ")
        agenda[categoria].append([nome, telefone]) 
        carregando("Salvando")
        print(Fore.GREEN + "Contato adicionado com sucesso")
    else:
        print(Fore.RED + "Categoria inválida")

def listar_contatos(): 
    print("Categorias: Família, Amigos, Trabalho")
    categoria = input("Digite a categoria: ").capitalize()

    if categoria in agenda:
        if not agenda[categoria]:
            print("Nenhum contato nessa categoria")
        else:
            print(Fore.BLUE + f"\nContatos em {categoria}:")
            for i, contato in enumerate(agenda[categoria], 1): 
                print(f"{i}. {contato[0]} - {contato[1]}") 
    else:
        print(Fore.RED + "Categoria inválida")

def buscar_contato():
    busca = input("Digite o nome ou telefone para buscar: ").lower()
    encontrados = [] 

    for categoria, contatos in agenda.items():  
        for contato in contatos:
            if busca in contato[0].lower() or busca in contato[1]:
                encontrados.append((categoria, contato))

    if encontrados:
        print(Fore.CYAN + "\nContatos encontrados: ")
        for cat, cont in encontrados:
            print(f"{cont[0]} - {cont[1]} (Categoria: {cat})")
    else:
        print(Fore.RED + "Nenhum contato encontrado.") 

def main():
    mostrar_titulo()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            buscar_contato()
        elif opcao == "4":
            print(Fore.MAGENTA + "Saindo da agenda...")
            break
        else:
            print(Fore.RED + "Opção inválida. Tente novamente") 

main()
