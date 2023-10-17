lista1 = [1,2,4] 
lista2 = [1,3,4]
def organizarLista():
    lista3 = lista1 + lista2
    tamanho = len(lista3)
    lista4 = []
    # i = 0, i = 1, ... , i = 5 
    for i in range(tamanho):
        # j = 0, ... , j = 5
        for j in range(0,tamanho-i-1):
            # 1 > 2, 2 > 4, 4 > 1
            # 1 > 3, 1> 4, 3>1
            # 2 > 1
            if lista3[j] > lista3[j+1]:
                #  4,1 = 1,4
                # 1,2,1,4,3,4
                # 3,1 = 1,3
                #1,2,1,3,4,4
                # 2,1 = 1,2
                # 1,1,2,3,4,4
                lista3[j], lista3[j+1] = lista3[j+1],lista3[j]
    print(lista3)
organizarLista()