import pandas as pd

def near(num):
    ###########################################################
    #LER ARQUIVO
    data = pd.read_csv('names2012.txt', sep=",", header=None)
    data.columns = ["name", "sex", "births"]

    ###########################################################
    #MEDIA FEMININA
    feminino = data[data['sex']=='F']
    media_fem = feminino.mean()
    fem = media_fem[0]

    #MEDIA MASCULINA
    masculino = data[data['sex']=='M']
    media_masc = masculino.mean()
    masc = media_masc[0]

    ###########################################################
    #COLUNA MEAN BY SEX
    data['mean by sex']=0

    #recoloquei valores da media
    data['mean by sex'][0:len(feminino)-1]=fem
    data['mean by sex'][len(feminino):]=masc

    ###########################################################
    #MEAN DISTANCCE    
    data['sex mean distance'] = 0

    for i in range(len(feminino)-1):
        data['sex mean distance']=(data['births']-fem)

    for i in range(len(data[len(feminino):])):
        data['sex mean distance']=(data['births']-masc)

    ###########################################################
    #REDEFININDO OS VALORES PARA POSITIVOS    
    #transformei os números em positivos
    vetor = data['sex mean distance'].values
    vetor2 = list(vetor)

    
    for i in list(range(len(data))):
        if vetor2[i] < 0:
            vetor2[i] = vetor2[i]*(-1)
        i+=1
        
    #devolvi os números para o dataframe
    data['sex mean distance']=vetor2

    ###########################################################
    #CALCULEI O MENOR VALOR
    lista = []

    data['answer']=0

    for i in list(range(len(data))):
        lista.append(data['sex mean distance'][i]-num)
    i+=1

    for i in list(range(len(data))):
        if lista[i]<0:
            lista[i]=lista[i]*(-1)
        i+=1

    data['answer']=lista

    menor = data.sort_values('answer')
    
    ###########################################################
    #COLOQUEI A RESPOSTA P/ HOMEM E MULHER
    masculino1 = menor[menor['sex']=='M']
    masc_lista = list(masculino1['name'])
    answer_masc = masc_lista[0]

    feminino1 = menor[menor['sex']=='F']
    fem_lista = list(feminino1['name'])
    answer_fem = fem_lista[0]

    return(answer_masc, answer_fem)
