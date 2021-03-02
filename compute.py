#importando a biblioteca para usar o valor de pi
import math

#variavel para salvar a resposta da operação escolhida
answer = int(input("Digite 1 para converter para graus, ou 2 para radianos: "))

#validação da opção de cálculo
if answer == 1:

    x = float(input("Informe o valor para conversão: "))  #variável que recebe o valor informado pelo usuário para ser convertido
    y = round(x * (180/math.pi), 2)                       #cálculo da operação
    print(f"{x} convertido é igual a {y} graus")          #imprime a resposta

else:

    x = float(input("Informe o valor para conversão: "))
    y = round(x * (math.pi / 180), 4)
    print(f"{x} convertido é igual a {y} radianos")
