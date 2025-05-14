Matriz = [[0] *4 for _ in range(4)]
Matriz[0][0] = 0 
Matriz[0][1] = 1
Matriz[0][2] = 0
Matriz[0][3] = 1

Matriz[1][0] = 0 
Matriz[1][1] = 0
Matriz[1][2] = 1
Matriz[1][3] = 0

for contador1 in range(4):
    for contador2 in range(4):
        print(Matriz[contador1][contador2],end='')
    print()