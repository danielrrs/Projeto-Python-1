import advinha
import forca

def escolhe_jogo():

   print("*****************************************************")
   print("***************Escolha o seu jogo!******************")
   print("*****************************************************")

   print("(1) Forca (2) Adivinha")

   jogo = int(input("Qual jogo?"))

   if(jogo == 1):
      print("Jogando Forca")
      forca.jogar()
      
   elif(jogo == 2):
      print("Jogando Advinha")
      advinha.jogar()
      
if(__name__ == "__main__"):
   escolhe_jogo()   
