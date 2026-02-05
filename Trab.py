from dataclasses import dataclass
from enum import Enum, auto
from os import system


class Classificação(Enum):
    ALUNO=auto()
    SERVIDORMENORIGUAL3=auto()
    SERVIDORMAIOR3=auto()
    DOCENTE=auto()
    EXTERNO=auto()

class Pagamento(Enum):
    PIX=auto()
    DINHEIRO=auto()
    CARTÃO=auto()


@dataclass
class Ticket:
    classificação:Classificação
    pagamento:Pagamento
    quantidade:int

Vendas:list[Ticket]=[]

def registro(Vendas:list,x1:int,x2:int,x3:int) -> list:
    '''
    Esta Função recebe uma lista de vendas e 3 variáveis que possuem o registro da pessoa e registra a venda dentro da lista

    Exemplos:
    >>> registro([],1,1,1)
    ====================================================
    Total= R$ 5
    <BLANKLINE>
    Confirmar a venda?
    S ou N
    <BLANKLINE>
    =[]
    >>> registro([Ticket(Classificação.DOCENTE,Pagamento.PIX,1)],1,1,1)
    ====================================================
    Total= R$ 5
    <BLANKLINE>
    Confirmar a venda?
    S ou N
    <BLANKLINE>
    =[Ticket(classificação=<Classificação.DOCENTE: 4>, pagamento=<Pagamento.PIX: 1>, quantidade=1)]
    '''


    if x1 ==1:
        x1=Classificação.ALUNO
    elif x1 ==2:
        x1=Classificação.SERVIDORMENORIGUAL3
    elif x1 ==3:
        x1=Classificação.SERVIDORMAIOR3
    elif x1 ==4:
        x1=Classificação.DOCENTE
    elif x1 ==5:
        x1=Classificação.EXTERNO


    if x1 == Classificação.ALUNO or x1== Classificação.SERVIDORMENORIGUAL3:
        preçodavenda = int(x3 * 5)
    elif x1 == Classificação.SERVIDORMAIOR3 or x1==Classificação.DOCENTE:
        preçodavenda = int(x3 * 10)
    elif x1 == Classificação.EXTERNO:
        preçodavenda = int(x3 * 19)


    if x2 ==1:
        x2=Pagamento.PIX
    elif x2 ==2:
        x2=Pagamento.DINHEIRO
    elif x2 ==3:
        x2=Pagamento.CARTÃO

    venda = Ticket(x1, x2, x3)
    print('====================================================\nTotal= R$',preçodavenda)
    print('\nConfirmar a venda?\nS ou N\n')
    ação2=input('=')



    if ação2 == 'S':
        Vendas.append(venda)
        return(Vendas)
    else:
        return(Vendas)



def Impressão(Vendas:Ticket):
    '''
    Esta função vai imprimir dois gráficos, total de tickets vendidos e a renda total a partir da lista de vendas registradas.

    Exemplos:
    >>> Impressão([Ticket(Classificação.ALUNO,Pagamento.PIX,1)])
    RELATÓRIO DE VENDAS:
    <BLANKLINE>
    ====================================================
    A renda foi de R$ 5
    Foram vendidos 1 tickets no total
    ====================================================
    <BLANKLINE>
    <BLANKLINE>
    GRÁFICO PESSOA X TICKET
    <BLANKLINE>
    Alunos [ ==========]  100 %
    <BLANKLINE>
    Servidor<=3 [ ]  0 %
    <BLANKLINE>
    Servidor>3 [ ]  0 %
    <BLANKLINE>
    Docente [ ]  0 %
    <BLANKLINE>
    Externo [ ]  0 %
    <BLANKLINE>
    <BLANKLINE>
    GRÁFICO PAGAMENTO X RENDA
    <BLANKLINE>
    PIX [ ==========]  100 %
    <BLANKLINE>
    Dinheiro [ ]  0 %
    <BLANKLINE>
    Cartão [ ]  0 %
    <BLANKLINE>
    >>> Impressão([Ticket(Classificação.ALUNO,Pagamento.PIX,1),Ticket(Classificação.SERVIDORMENORIGUAL3,Pagamento.CARTÃO,1)])
    RELATÓRIO DE VENDAS:
    <BLANKLINE>
    ====================================================
    A renda foi de R$ 10
    Foram vendidos 2 tickets no total
    ====================================================
    <BLANKLINE>
    <BLANKLINE>
    GRÁFICO PESSOA X TICKET
    <BLANKLINE>
    Alunos [ =====]  50 %
    <BLANKLINE>
    Servidor<=3 [ =====]  50 %
    <BLANKLINE>
    Servidor>3 [ ]  0 %
    <BLANKLINE>
    Docente [ ]  0 %
    <BLANKLINE>
    Externo [ ]  0 %
    <BLANKLINE>
    <BLANKLINE>
    GRÁFICO PAGAMENTO X RENDA
    <BLANKLINE>
    PIX [ =====]  50 %
    <BLANKLINE>
    Dinheiro [ ]  0 %
    <BLANKLINE>
    Cartão [ =====]  50 %
    <BLANKLINE>
    >>> Impressão([Ticket(Classificação.ALUNO,Pagamento.PIX,10), Ticket(Classificação.SERVIDORMENORIGUAL3,Pagamento.DINHEIRO,2), Ticket(Classificação.DOCENTE,Pagamento.CARTÃO,4), Ticket(Classificação.EXTERNO,Pagamento.DINHEIRO,4)])
    RELATÓRIO DE VENDAS:
    <BLANKLINE>
    ====================================================
    A renda foi de R$ 176
    Foram vendidos 20 tickets no total
    ====================================================
    <BLANKLINE>
    <BLANKLINE>
    GRÁFICO PESSOA X TICKET
    <BLANKLINE>
    Alunos [ =====]  50 %
    <BLANKLINE>
    Servidor<=3 [ =]  10 %
    <BLANKLINE>
    Servidor>3 [ ]  0 %
    <BLANKLINE>
    Docente [ ==]  20 %
    <BLANKLINE>
    Externo [ ==]  20 %
    <BLANKLINE>
    <BLANKLINE>
    GRÁFICO PAGAMENTO X RENDA
    <BLANKLINE>
    PIX [ ===]  30 %
    <BLANKLINE>
    Dinheiro [ =====]  50 %
    <BLANKLINE>
    Cartão [ ==]  20 %
    <BLANKLINE>
    '''             

    #Variaveis de contador para os gráficos

    ticket5 = 0
    ticket10 = 0
    ticket19 = 0
    pagapix = 0
    pagadin = 0
    pagacart = 0
    GA = 0
    GTA=0
    GSMENOR3 = 0
    GTSMENOR3=0
    GSMAIOR3 = 0
    GTSMAIOR3 = 0
    GD = 0
    GTD = 0
    GE = 0
    GTE = 0

    #Analisando a tabela e dando valor aos contadores
    #Contadores para o primeiro gráfico
    for item in Vendas:
        if item.classificação == Classificação.ALUNO or item.classificação == Classificação.SERVIDORMENORIGUAL3:
            ticket5 = ticket5 + item.quantidade
            if item.classificação == Classificação.ALUNO:
                GA += 1
                GTA = GTA + item.quantidade
            else:
                GSMENOR3 += 1
                GTSMENOR3 = GTSMENOR3 + item.quantidade
        elif item.classificação == Classificação.SERVIDORMAIOR3 or item.classificação==Classificação.DOCENTE:
            ticket10 = ticket10 + item.quantidade
            if item.classificação == Classificação.SERVIDORMAIOR3:
                GSMAIOR3 += 1
                GTSMAIOR3 = GTSMAIOR3 + item.quantidade
            else:
                GD += 1
                GTD = GTD + item.quantidade
        else:
            ticket19 = ticket19 + item.quantidade
            GE += 1
            GTE = GTE + item.quantidade

    #Contadores para o segundo gráfico

    for item in Vendas:
        if item.classificação == Classificação.ALUNO or item.classificação == Classificação.SERVIDORMENORIGUAL3:
            valorticket=5
        elif item.classificação == Classificação.DOCENTE or item.classificação == Classificação.SERVIDORMAIOR3:
            valorticket=10
        elif item.classificação == Classificação.EXTERNO:
            valorticket=19


        if item.pagamento == Pagamento.PIX:
            pagapix = pagapix + (item.quantidade * valorticket)
        elif item.pagamento == Pagamento.DINHEIRO:
            pagadin = pagadin + (item.quantidade * valorticket)
        elif item.pagamento == Pagamento.CARTÃO:
            pagacart = pagacart + (item.quantidade * valorticket)




    valortickettotal= (ticket5*5) + (ticket10*10) + (ticket19*19)
    tickettotal = ticket5+ticket10+ticket19


    

    print('RELATÓRIO DE VENDAS:\n\n====================================================')
    print('A renda foi de R$',valortickettotal,'\nForam vendidos',tickettotal,'tickets no total')
    print('====================================================\n\n')


    #Começo Grafico Pessoa X Ticket
    
    porcentagemGA = round(((GTA*10) / tickettotal))
    porcentagemGME3 = round(((GTSMENOR3*10) / tickettotal))
    porcentagemGMA3 = round(((GTSMAIOR3*10) / tickettotal))
    porcentagemGD = round(((GTD*10) / tickettotal))
    porcentagemGE = round(((GTE*10) / tickettotal))
    graficos = [porcentagemGA,porcentagemGME3,porcentagemGMA3,porcentagemGD,porcentagemGE]


    print('GRÁFICO PESSOA X TICKET\n')
    print('Alunos [',('='*porcentagemGA)+'] ',porcentagemGA*10,'%\n')
    print('Servidor<=3 [',('='*porcentagemGME3)+'] ',porcentagemGME3*10,'%\n')
    print('Servidor>3 [',('='*porcentagemGMA3)+'] ',porcentagemGMA3*10,'%\n')
    print('Docente [',('='*porcentagemGD)+'] ',porcentagemGD*10,'%\n')
    print('Externo [',('='*porcentagemGE)+'] ',porcentagemGE*10,'%\n')

    #Fim Grafico Pessoa X Ticket 

    #Começo Grafico Pagamento X Renda

    porcentagemGP = round(((pagapix*10) / valortickettotal))
    porcentagemGDIN = round(((pagadin*10) / valortickettotal))
    porcentagemGC = round(((pagacart*10) / valortickettotal))

    print('\nGRÁFICO PAGAMENTO X RENDA\n')
    print('PIX [',('='*porcentagemGP)+'] ',porcentagemGP*10,'%\n')
    print('Dinheiro [',('='*porcentagemGDIN)+'] ',porcentagemGDIN*10,'%\n')
    print('Cartão [',('='*porcentagemGC)+'] ',porcentagemGC*10,'%\n')

    #Fim Grafico Pagamento X Renda



def main():
    print('!!!SISTEMA DE TICKETS DO RU!!!\nSelecione uma ação: \n(1)- Registrar Venda\n(2)- Exibir Relatório de Vendas')

    ação = int(input('\n='))
    while ação == 1 or ação == 2:
        if ação ==1:
            
            print('====================================================\nDigite a Situação da Pessoa\n==================================================== \n\n1= Aluno\n2= Servidormenorigual3\n3=Servidormaior3\n4=Docente\n5=Externo \n')
    
            x1= int(input('='))
    
            
    
            print('====================================================\nQuantos tickets?\n==================================================== \n')
            x3 = int(input('='))
    
            
    
            print('====================================================\nQual a forma de Pagamento?\n==================================================== \n\n1= PIX \n2= Dinheiro \n3= Cartão\n')
            x2=int(input('='))

    
            registro(Vendas,x1,x2,x3)
    
        elif ação ==2:
            Impressão(Vendas)

        print('\n\nSELECIONE UMA AÇÃO !!! \n(1)- Registrar Venda\n(2)- Exibir Relatório de Vendas')
        ação = int(input('\n='))

if __name__ =='__main__':
    main()