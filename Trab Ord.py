from dataclasses import dataclass

@dataclass
class Retirado:
    offset:int
    tam: int
    

def main():

    with open('filmes.dat', 'r+w') as s:
        with open('operações.txt',"r") as o:

            global cabeçalho
            global filmes
            cabeçalho = int.from_bytes(s.read(4)) 
            led = [Retirado]
            operação = o.read()

            while operação != '':
                
                if operação == 'b':

                    s.read()

                    while o.read() != '\n':
                        cod += o.read()
                    
                    cod= int.from_bytes(cod)
                    busca(cod,s)
                
                elif operação == 'r':
                    
                    s.read()

                    print('Remoção do registro de chave: "',removido[0],'"\n')
                    while o.read() != '\n':
                        cod += o.read()
                    
                    cod= int.from_bytes(cod)
                    removido = remove(cod, s)

                    if removido == None:
                        print('Erro: Registro não encontrado !!!')
                    else:
                        print('Registro Removido!(',removido[1],') \n'
                              'Local: Offset =',removido[1],'bytes')

                elif operação == 'i':
                    
                    s.read()

                    while s.read() != "\n":
                        filme = s.decode(s.read())
                        tam += 1

                    insere(s,filme,led,tam)

            printa_led()


def printa_led(led:list[Retirado]):

    print("LED -> ")

    for i in range(0:len(led)-2):
        print('[Offset:', led[i].offset,', TAM:', led[i].tam,'] ->')
    
    print('[Offset:', led[i].offset,', TAM:', led[i].tam,'] -> FIM \n'
          'Total de',len(led),'espaços isponiveís\n '
          'A LED foi impressa com sucesso')


def leia_reg(arq) -> list | str:
    try:
        tam = int.from_bytes(arq.read())
        if tam > 0:
            s = arq.read(tam)
            return s.decode(),tam
    except OSError as e:
        print(f'Erro leia_reg: {e}')
    return ''    
        

def busca_seq(codigo:int, arq) -> list | None:
    reg, Offset= leia_reg(arq)[0].split(sep= '|'), int.from_bytes(leia_reg(arq)[1])

    while reg[0] != codigo:
        reg= leia_reg(arq)[0].split(sep= '|')
        Offset += leia_reg(arq)[1]
        tam = leia_reg(arq)[1]

    if reg == '':
        return None
    else:
        return [reg, Offset, tam]

def busca(arq) -> None:

    cod = arq.read()
    f = busca_seq(cod,arq)
    print('Buscando pelo filme de chave:',cod)
    print("CÓDIGO:",cod,'\n',
          "LOCAL = OFFSET:",f[1],'\n',
          "FILME:",f[0][1]+f[0][2]+f[0][3]+f[0][4]+f[0][5]+f[0][6],'\n')
    

def checa_led(cabecalho: int,arq) -> bool:

    arq.seek(0)
    c = int.from_bytes(arq.read(4))
    
    return cabecalho == c


def proximo_led(posicao:int, arq) -> int:


    arq.seek(posicao)
    proximo = ''

    while True:
        
        num = int.from_bytes(arq.read())

        if num != int:
            return int(proximo)

        else:
            proximo += arq.read().decode()

def gera_offset(cod:int,arq) -> list:

    arq.seek(4)
    reg, Offset = leia_reg(arq)[0], leia_reg(arq)[1]
    reg = reg.split(sep='|')

    while reg[0] != cod:
        Offset += leia_reg(arq)[1]
        reg = leia_reg(arq)[0]
        reg = reg.split(sep='|')
        tam = leia_reg(arq)[2]

    return Offset, tam


def ordena(lista:list[Retirado]) -> list[Retirado]:

    for i in range(len(lista)):
        minimo = indice_do_minimo(lista, i+1, len(lista)-1)
        if lista[i].offset > lista[minimo].offset:
            aux = lista[i]
            lista[i] = lista[minimo]
            lista[minimo] = aux
    return lista

def indice_do_minimo(lista: list, inicio: int, fim: int) -> int:
   
    minimo = inicio
    for i in range(inicio+1, fim+1):
        if lista[i].offset < lista[minimo].offset:
            minimo = i
    return minimo     

def reescreve_led(arq, lista: list[Retirado]):

    arq.seek(0)
    arq.write(0000+lista[0].offset) 
    for i in range(1:len(lista)):
    

        arq.seek(lista[i-1].offset)
        arq.write('*',lista[i].offset)

        if lista[i] == len(lista) - 1:
            arq.seek(lista[i].offset)
            arq.write('*',-1) 

def remove(cod:int, arq, lista:list[Retirado]) -> list:

    removido = busca_seq(cod, arq)[1]
    tam= busca_seq(cod,arq)[2]

    if removido == None:
        return None
    else:
        if checa_led(cabeçalho,arq):

            arq.seek(0)
            arq.write(0000 + removido)

            arq.seek(removido)
            arq.write('*',-1)
            
        else:
            arq.seek(0)
            cabeçalho = int.from_bytes(arq.read(4))
            proximo = proximo_led(cabeçalho,arq)
            offset = gera_offset(proximo,arq)[0]
            t = gera_offset(proximo, arq)[1]

            while proximo != -1:
                
                lista.append(Retirado(offset, t))
                proximo = proximo_led(proximo,arq)
                offset += gera_offset(proximo,arq)[0]
                t = gera_offset(proximo, arq)[1]

            lista.append(Retirado(removido,tam))
            lista = ordena(lista)
            reescreve_led(arq, lista)
        
        return [removido, tam]


def insere(arq, f:str, led:list[Retirado], tam:int):

    i=0

    while led[i].tam < tam:
        i += 1
    

    arq.seek(led[i-1].offset + 2)
    arq.write(led[i+1].offset)


    arq.seek(led[i].offset)
    arq.write(tam)
    arq.write(f)
    
    for i in range(led[i] - tam):

        arq.write("\0")

    
