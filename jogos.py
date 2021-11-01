#!/usr/bin/env python
# coding: utf-8

# In[3]:


import jogoforca
import jogoadivinhacao

def escolhe_jogo():

    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca e (2) Adivinhação")

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogando Forca")
        jogoforca.jogar()

    elif (jogo == 2):
        print("Jogando Adivinhação")
        jogoadivinhacao.jogar()

    else:
        print ("Você não escolheu as opções corretamente.")

if (__name__=="__main__"):
    escolhe_jogo()


# In[ ]:





# In[ ]:




