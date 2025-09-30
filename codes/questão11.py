def sort_stack(stack):
    aux = []
    while stack:
        temp = stack.pop()
        while aux and aux[-1] > temp:
            stack.append(aux.pop())
        aux.append(temp)
    while aux:
        stack.append(aux.pop())
    return stack


stack = [5, 30, 25, 10, 15, 20]
print("Original:", stack)

sorted_stack = sort_stack(stack)
print("Ordenada:", sorted_stack)
