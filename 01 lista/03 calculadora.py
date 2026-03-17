import os
os.system("cls")


print("Escolha a operação")
print("1 - (+)")
print("2 - (-)")
print("3 - (X)")
print("4 - (/)")

Operação=input("número correspondente a operação: ")
if Operação == "1":
   print("Você escolheu adição")
   valor01 = float(input ("escreva o primeiro numero:"))
   valor02 = float(input ("escreva o segundo numero:"))
   Resultado = (valor01 + valor02)

   print("A sua somatoria deu:", Resultado)
   input("Pressione o <enter> para encerrar")
   
elif Operação =="2":
   print("Você escolheu Subtração")
   valor01 = float(input ("escreva o primeiro numero:"))
   valor02 = float(input ("escreva o segundo numero:"))
   Resultado = (valor01 - valor02)

   print("A sua somatoria deu:", Resultado)
   input("Pressione o <enter> para encerrar")

elif Operação =="3":
   print("Você escolheu Multiplicação")
   valor01 = float(input ("escreva o primeiro numero:"))
   valor02 = float(input ("escreva o segundo numero:"))
   Resultado = (valor01 * valor02)

   print("A sua somatoria deu:", Resultado)
   input("Pressione o <enter> para encerrar")

elif Operação =="4":
   print("Você escolheu Divisão")
   valor01 = float(input ("escreva o primeiro numero:"))
   valor02 = float(input ("escreva o segundo numero:"))
   Resultado = (valor01 / valor02)

   print("A sua somatoria deu:", Resultado)
   input("Pressione o <enter> para encerrar")

else:
   print("Opção inválida")
   input("Pressione <enter> para encerrar ")
