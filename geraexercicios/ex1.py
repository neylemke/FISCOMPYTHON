import sys
import random
import pickle
dic={'enunciado':r"Qual é a área de um círculo de raio 1m?",
     'alternativas': ['3.14','2','i','-7','42'], 'gabarito':'3.14',
     'dica':'Elimine as alternativas absurdas!'}
random.shuffle(dic['alternativas'])
with open('ex1.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(dic, f, pickle.HIGHEST_PROTOCOL)