def select_operation(operation,x,y):
    if (operation == '+'):
        return x + y
    elif (operation == '-'):
        return x - y
    elif (operation == '*'):
        return x * y
    elif (operation == '/'):
        return x / y
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1):
        row = list()
        for j in range(1,num_columns+1):
            if i==1 and j==1:
                row.append(1)
            elif i==1:
                row.append(j)
            elif j==1:
                row.append(i)
            else:
                row.append(round(select_operation(operation,i,j),2))
        print(row)
    return

print('Введите операцию (+,-,*,/):',end='')

operation = input()

print_operation_table(operation)