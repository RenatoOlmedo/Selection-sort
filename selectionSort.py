def sort(data):
    posicaoSort = 0
    posicaoMenor = 0
    for i in data:
        menorValor = data[posicaoSort]
        counter = 0
        for z in data[posicaoSort:len(data)]:
            if(z < menorValor):
                menorValor = z
                posicaoMenor = posicaoSort + counter
            counter += 1
        temp = data[posicaoSort]
        data[posicaoMenor] = temp
        data[posicaoSort] = menorValor

        posicaoSort += 1
    return data

data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
print(sort(data))