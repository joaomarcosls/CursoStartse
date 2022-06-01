#Inicio 
      #1. Ler (A,B)
      #2. Se (A>B)Então
      #3. Exibir("Os numeros são iguais")
      #4.   Senão Se (A>B) Então 
      #5.   Exibir (A)
      #6.   Senão
      #7.   Exibir(B)
      #8.   Fim Se 
      #9. Fim Se 
#Fim 

a = int(input("Diguite A:")) # converte o Numero recebido pelo input em Inteiro, so solicita 
b = int(input("Diguite B:"))# converte o Numero recebido pelo input em Inteiro

if a == b : 
    print("Os números são iguais:", a )
    
elif a > b :
    print("A",a)
else:
    print("B",b)   
