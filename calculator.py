import funcoes as func

print('Seja bem-vindo ao calculator-BR')
nome_1 = ()
nome_2 = ()
nome_1 = (input('Qual é o seu primeiro nome? ')) 
nome_2 = (input('Qual é o seu segundo nome?' ))


question = ""    
while question != 'n':
        numero_1 = int(input('Digite seu primeiro valor: '))
        operador = str(input('Digite qual será o operador de preferência: '))
        numero_2 = int(input('Digite seu segundo valor: '))
        if operador == "+":
                resultado_1 = func.somar(numero_1, numero_2)
                print('O resultado foi equivalente a: {}'.format(resultado_1))
                
        elif operador == "-":
                resultado_2 = func.subtrair(numero_1, numero_2)
                print('O resultado foi equivalente a: {}'.format(resultado_2))

        elif operador == "/":
                resultado_3 = func.dividir(numero_1, numero_2)
                print('O resultado foi equivalente a: {}'.format(resultado_3))

        elif operador == "*":
                resultado_4 = func.multiplicar(numero_1, numero_2)
                print('O resultado foi equivalente a: {}'.format(resultado_4))

        elif operador == "media":
                print('você quis dizer media?')
                resultado_5 = func.media_valores(numero_1, numero_2)
                print('O resultado foi equivalente a: {}'.format(resultado_5))

        question = input('Deseja continuar com a operação? ')

else:
        print('Agradeço por sua atenção {}!'.format(nome_1  +  nome_2))