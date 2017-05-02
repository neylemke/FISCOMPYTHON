import sys
import random
import pickle

x=randint(1,8)
dic={'enunciado':r"Qual é a área de um círculo de raio "+str(int)+"m?",
     'alternativas': [
                     str(3.14*x^2) ,str(2*3.14*x^2),'i',-str(3.14*x^2),'42'], 
     'gabarito':str(3.14*x^2),
     'dica':'Elimine as alternativas absurdas!'}
random.shuffle(dic['alternativas'])
with open('zxy456.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)