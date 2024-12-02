print('***Cajero automatico***')

salir=False
saldo_inicial=1000
while not salir:
    print('Menu:\n'
          '\t1. Depositar\n'
          '\t2. Retirar\n'
          '\t3. Consultar saldo')
    opcion=int(input('Que opcion escoges?'))

    if opcion==1:
        depositar=float(input('Cuanto dinero quieres depositar?'))
        saldo_inicial+=depositar
    elif opcion==2:
        depositar = float(input('Cuanto dinero quieres sacar?'))
        if(depositar>saldo_inicial):
            print('Saldo insuficiente')
        else:
            saldo_inicial-=depositar
    elif opcion==3:
        print(f'Saldo actual: {saldo_inicial}')

    else:
        print('Opcion invalida')
