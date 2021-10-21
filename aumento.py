#declaração função aumento
def aumento():
    #recebimento do salario atual
    salario = float(input("Digite seu salario:\n"))
    #verificação sobre qual taxa de aumento será utilizada
    if(salario > 1250.00):
        #aumento de 10%
        salario *= 1.10
    else:
        #aumento de 15%
        salario *= 1.15

    #retorno do valor do no console
    print("O novo salario será de R$ {:.2f}".format(salario))

if (__name__ == "__main__"):
    aumento()