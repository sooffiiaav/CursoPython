

def fun_recursiva(numero):

    if numero == 1:
        print(numero, end=' ') #1
    else:
        fun_recursiva(numero-1)
        print(numero, end=' ')


resultado=fun_recursiva(2)