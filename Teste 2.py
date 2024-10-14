
"""   Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre."""


StringV =input("Digite uma palavra: ")


cont = 0
for i in range(len(StringV)):
    if StringV[i] == "a" or StringV[i] == "A":
        cont += 1

    elif  StringV [i] == "a"or StringV[i]=='á' or StringV[i]=='ã' or StringV[i]=='â'and StringV[i] == "A"or StringV[i]=='á'or StringV[i]=='Ã'or StringV[i]=='Â':
        cont += 1
 

      
print(f"A letra 'a' aparece {cont}  vezes na palavra digitada.")