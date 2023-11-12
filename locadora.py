import os 

carros = [ 
        ("Toyota Yaris ", 153), 
        ("Chevrolet Onix", 90),
        ("Citroen C4", 168),
        ("Hyndai Hb20s", 161),
        ("Hyndai Tucson", 732),
        ("Renault Kwid", 80),
        ("Fiat Argo", 91),
        ("Jeep Renegade", 183)
        ]
alugados = []  

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))

mostrar_lista_de_carros(carros)        

while True:
    os.system("clear") 
    print("--------------------") 
    print("Locadora de carros!")
    print("--------------------") 
    print("O que deseja fazer?") 
    print("0 - Mostrar portifólio | 1 - Alugar carro | 2 - Devolver carro")
    op = int(input())

    os.system("clear")
    if op == 0:
        pass

    elif op == 1:
        pass

    elif op == 2:
        pass

    print("") 
    print("=========")
    print("0 - CONTINUAR | 1 - SAIR")
    if float(input()) == 1:
        break

  