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

print("--------------------") 
print("Locadora de carros!")
print("--------------------") 

def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))

mostrar_lista_de_carros(carros)      