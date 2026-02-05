from time import sleep
from dataclasses import dataclass
from copy import deepcopy
import random
import os

@dataclass
class Bloco:
    index:int = 0
    n1:int = 0
    n2:int = 0
    n3:int = 0
    n4:int = 0

@dataclass
class Cache:
    index: int
    bloco:Bloco
    LFU:int
    first:int
    LRU:int

def main():

    '''Função principal para funcionamento do sistema'''
    #Programa inicia
    print('='*50)
    print("")
    print(f'{"ACESSANDO MEMÓRIA!":^50}')
    print("")
    print('='*50)
    print("")

    print(f'{"["+"="*8+"]":<25}'+ "40%")
    sleep(1)
    
    print(f'{"["+"="*12+"]":<25}' +"60%")
    sleep(1)
    
    print(f'{"["+"="*20+"]":<25}'+"98%" )
    sleep(1)

    print(f'{"["+"="*22+"]":<25}'+"100%" )
    print("")
    
    print(f'{"SISTEMA PRONTO !":^50}')
    print("")
    continuar_operando = input("Tecle ENTER para iniciar:")
    
    os.system("cls") #Windowns -> serve para limpar o terminal, porém muda o comando dependendo do S.O
    #os.system('clear') #linux

    #Mensagem de opções
    print('=' * 50)
    print("")
    print(f'{"MEMÓRIA INICIADA, BEM VINDO !":^50}')
    print("")   
    print('=' * 50)

    global política

    print("=" * 50)
    print("")
    print(f'{"SELECIONE A POLÍTICA DE SUBSTITUIÇÃO":^50}')
    print("")
    print("=" * 50)
    
    política = int(input('\n[ 1 ] -> (FIFO) \n[ 2 ] -> (LFU)\n[ 3 ] -> (LRU) \n\nDigite a política escolhida:'))

    while política not in [0,1,2]:
        print('Selecione um dos valores indicados!!!')
        política = int(input('\n[ 1 ] -> (FIFO) \n[ 2 ] -> (LFU)\n[ 3 ] -> (LRU) \n\nDigite a política escolhida:'))

    if política == 1:
        print("\nPOLÍTICA SELECIONADA: FIFO ( First IN First OUT)")
    elif política == 2 : 
        print("\nPOLÍTICA SELECIONADA: LFU ( Least Frequently Used)")
    elif política == 3 : 
        print("\nPOLÍTICA SELECIONADA: LRU ( Least Recently Used)")
    continuar_operando = input("Tecle ENTER para iniciar: ")
    
    os.system("cls")
    #os.system('clear')


    acao = 0
    #looping de ações

    while acao != 5:    
        print('='*50)
        print("")
        print(f'{"MENU PRINCIPAL":^50}')
        print("")
        print('='*50)

        print('\n[ 1 ] -> (BUSCAR DADO NA RAM) \n[ 2 ] -> (CONSULTAR CACHE)\n[ 3 ] -> (CONSULTAR RAM)\n[ 4 ] -> (SAIR DO PROGRAMA)\n')
        acao = int(input('QUAL AÇÃO DESEJA REALIZAR: '))
        os.system("cls")
        #os.system('clear')

        if acao == 1:
            print("="*50)
            print("")
            print(f'{"BUSCAR DADO NA RAM":^50}')
            print("")
            print("="*50)
            os.system('cls')
            dado_buscado = int(input('DIGITE O DADO A SER BUSCADO\n= '))
            Buscar_na_RAM(dado_buscado,ram,cache)
        elif acao == 2:
            print("=" * 91)
            print("")
            print(f'{"MEMÓRIA CACHE":^91}')
            print("")
            print("=" * 91)
            Exibir_CACHE(cache)
        elif acao == 3:
            print("=" * 48)
            print("")
            print(f'{"MEMÓRIA RAM":^50}')
            print("")
            print("=" * 48)
            Exibir_RAM(ram)
        elif acao == 4 :
            print("="*50)
            print("")
            print(f'{"FOI UM PRAZER, VOLTE SEMPRE !":^50}')
            print("")
            print("="*50)
            break
        else:
            print("="*50)
            print("")
            print(f'{"DIGITE APENAS OS CÓDIGOS CORRESPONDENTES !!":^50}')
            print("")
            print("="*50)
            print("")
            continuar_operando = input("Tecle ENTER para voltar ao Menu Principal:")
            os.system("cls")



            
def Buscar_na_RAM(dado:int,ram:list[Bloco],cache:list[Cache]):
    global tamanho_cache
    global política

    x = None
    for item in ram:
        if _checa_na_RAM(dado,item):
            x = deepcopy(item)
    
    if x == None:
        print('O dado não se encontra na RAM!!!')
        continuar_operando = input("Tecle ENTER para voltar ao menu principal: ")
    else:
        mudar = input('Deseja alterar o dado?\nS/s ou N/n\n=')

        if mudar == 'S' or mudar == 's':
            novo_dado = _criadados()
            print('Dado gerado:',novo_dado)
            while _checadados_bool(novo_dado,ram):
                novo_dado = _criadados()
            
            if x.n1 == dado:
                x.n1 = novo_dado
            if x.n2 == dado:
                x.n2 = novo_dado
            if x.n3 == dado:
                x.n3 = novo_dado
            if x.n4 == dado:
                x.n4 = novo_dado

        hit = hit_miss(x)

        if tamanho_cache < 4 and hit == False:
            tamanho_cache +=1
            Mapeamento(x)

        elif hit == False:
            bloco_retirado = sub(x,cache)
            print('BLOCO REMOVIDO:', bloco_retirado)
            Write_Back(ram,bloco_retirado)

        if hit == True:
            print('\nO dado:', dado, 'foi um HIT\n')
            continuar_operando = input("Tecle ENTER para voltar ao menu principal: ")
        else:
           print('\nO dado:', dado, 'foi um MISS\n')
           continuar_operando = input("Tecle ENTER para voltar ao menu principal: ")


    
    
        




def Exibir_RAM(ram:list[Bloco]):
    '''
    Exibe a memória RAM
    '''
     
    print('='*48 + '\n')
    print("")

    for item in ram:
        print("• BLOCO: "+ f'{str(item.index):<4}' + " | ",   end="")  
        print(f'{item.n1:^6}',"|", end="")
        print(f'{item.n2:^6}',"|", end="")
        print(f'{item.n3:^6}',"|", end="")
        print(f'{item.n4:^6}',"|", )
        
    print("")
    print("="*48 + "\n")
    continuar_operando = input("Tecle ENTER para voltar ao menu principal")
    os.system("cls")
    #os.system("clear")
    

def Exibir_CACHE(cache:list[Cache]):
    '''
    Exibe a memória CACHE
    '''
    print('='*91 + '\n')
    print("")

    for item in cache:
        print("• CACHE: "+ f'{str(item.index):<4}' + " BLOCO -> " + f'{str(item.bloco.index):<4}' +" | " ,   end="")  
        print(f'{item.bloco.n1:^6}',"|", end="")
        print(f'{item.bloco.n2:^6}',"|", end="")
        print(f'{item.bloco.n3:^6}',"|", end="")
        print(f'{item.bloco.n4:^6}',"|", end="")
            
        print('   FIRST:',item.first,'  LFU:',item.LFU,'  LRU:',item.LRU) 

    print("")
    print("="*91 + "\n")
    continuar_operando = input("Tecle ENTER para voltar ao menu principal")
    os.system("cls")





#Funções de Substituição

def sub(bloco:Bloco,cache:list[Cache]) -> Bloco:
    global política

    def lru(cache:list[Cache]) -> Cache:
        menor = cache[0]
        for item in cache:
            if item.LRU < menor.LRU:
                menor = deepcopy(item)
            elif item.LRU == menor.LRU and item.first < menor.first:
                menor = deepcopy(item)

        for item in cache:
            if item.first > menor.first:
                item.first -= 1
            
        
        return menor
            
    def lfu(cache:list[Cache]) -> Cache:
        menor = cache[0]
        for item in cache:
            if item.LFU < menor.LFU:
                menor = deepcopy(item)
            elif item.LFU == menor.LFU and item.first < menor.first:
                menor = deepcopy(item)

        for item in cache:
            if item.first > menor.first:
                item.first -= 1
                
        return menor

    def fifo(cache:list[Cache]) -> Cache:
        
        for item in cache:
            if item.first != 1:
                item.first -= 1
            else:
                x = deepcopy(item)
        return x

    if política == 1:
        bloco_cache = fifo(cache)
    elif política == 2:
        bloco_cache = lfu(cache)
    else:
        bloco_cache = lru(cache)
        

    bloco_retirado = bloco_cache.bloco
    indice = bloco_cache.index
    cache[indice] = Cache(indice,bloco,1,4,bloco_cache.LRU)

    return bloco_retirado






#Função de Mapeamento
def Mapeamento(bloco:Bloco):
    global tamanho_cache
    indice = random.randint(0,3)
    while cache[indice].LFU != 0:
        indice = random.randint(0,3)
    inserir = Cache(indice,bloco,1,tamanho_cache,1)
    cache[indice] = inserir





#Função Write-Back
def Write_Back(ram:list[Bloco],bloco:Bloco):
    ram[bloco.index+1] = bloco


#HIT ou MISS
def hit_miss(bloco:Bloco) -> bool:
    '''
    Devolve TRUE para HIT e FALSE para MISS
    '''
    for item in cache:
        if item.bloco == bloco:
            item.LFU += 1
            item.LRU += 1
            return True
    
    return False



#Funções Auxiliares
def _criadados() -> int:
    número = random.randint(0,10000)
    return número

def _checadados_bool(número:int,ram:list[Bloco]) -> bool:
    for item in ram:
       if número == item.n1 or número == item.n2 or número == item.n3 or número == item.n4:
            return True
    return False

def _criablocos(bloco:Bloco,i:int) -> Bloco:
    bloco.n1 = _criadados()
    while _checadados_bool(bloco.n1,ram):
        bloco.n1 = _criadados()

    bloco.n2 = _criadados()
    while _checadados_bool(bloco.n2,ram):
        bloco.n2 = _criadados()

    bloco.n3 = _criadados()
    while _checadados_bool(bloco.n3,ram):
        bloco.n3 = _criadados()

    bloco.n4 = _criadados()
    while _checadados_bool(bloco.n4,ram):
        bloco.n4 = _criadados()

    bloco.index = i
    return bloco


def _checa_na_RAM(dado:int,bloco:Bloco) -> bool:
    return dado == bloco.n1 or dado == bloco.n2 or dado == bloco.n3 or dado == bloco.n4 

if __name__ == '__main__':

    #Variaveís auxiliares

    ram = [Bloco]
    cache = [Cache]
    cache = cache = [
        Cache(0, Bloco(0, 0, 0, 0, 0), 0, 0, 0),
        Cache(1, Bloco(0, 0, 0, 0, 0), 0, 0, 0),
        Cache(2, Bloco(0, 0, 0, 0, 0), 0, 0, 0),
        Cache(3, Bloco(0, 0, 0, 0, 0), 0, 0, 0)
    ]
    global tamanho_cache
    global política
    política = 0
    tamanho_cache = 0

    i=0
    while i != 300:
        novo_bloco = Bloco(0,0,0,0,0)
        ram.append(_criablocos(novo_bloco,i))
        i+=1
    



    main()    