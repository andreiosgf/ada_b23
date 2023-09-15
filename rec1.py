def printFunc(test):
    if test<1:
        return
    else:
        print(f'Entra a la función donde test= {test} \t')
        printFunc(test-1)
        print(f'Regresa a la función donde test= {test} \t')
        return


if __name__=='__main__':
    test=3
    printFunc(test)