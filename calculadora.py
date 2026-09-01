num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

opc = 0 

while opc != 6:

    print(  '     [ 1 ] Somar\n'
            '     [ 2 ] Subtrair\n'   
            '     [ 3 ] Multiplicar\n' 
            '     [ 4 ] Dividir\n'      
            '     [ 5 ] Novos números\n'
            '     [ 6 ] Sair do programa\n')

    opc = int(input(' >>>>> Qual é a sua opção? '))

 
    if opc == 1:
        print(f'O resultado de {num1} + {num2} é {num1 + num2}')


    elif opc == 2:
        print(f'O resultado de {num1} - {num2} é {num1 - num2}')


 
    elif opc == 3:
        print(f'O resultado de {num1} x {num2} é {num1 * num2}')  
   
   
    elif opc == 4:
        
        if num2 == 0:
            print('Não é possível dividir por zero.')
        else:
            print(f'O resultado de {num1} / {num2} é {num1 / num2}')
       
    
    elif opc == 5:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))


    elif opc == 6: 
        print('Finalizando...\n=-==-==-==-==-==-==-==-==-==-=\nFim do programa! Volte sempre!')
    
    else: 
        print('Opção Inválida! Tente novamente.')
